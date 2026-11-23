#!/usr/bin/env python3
"""Build static Spanish and Portuguese copies of index, about and tutorials.

The site translates itself in the browser (THORCAST_I18N + JS), so search
engines and AI crawlers only see English. This script applies the same
dictionaries ahead of time and writes es.html / pt.html, about-es.html,
about-pt.html, tutorials-es.html and tutorials-pt.html.

Run it from the repo root after every change to index.html, about.html or
tutorials.html:   python3 tools/build_i18n_pages.py
Requires node (used only to read the dictionaries from the page script).
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://thorcast.ai/"
PAGES = ["index", "about", "tutorials"]
LANGS = {"es": "es", "pt": "pt-BR"}


def out_name(page, lang):
    if lang == "en":
        return "index.html" if page == "index" else f"{page}.html"
    return f"{lang}.html" if page == "index" else f"{page}-{lang}.html"


def url(page, lang):
    name = out_name(page, lang)
    return SITE if name == "index.html" else SITE + name


# Meta descriptions are not part of THORCAST_I18N; they live here.
META = {
    "index": {
        "es": "Analítica predictiva con IA para bancos, aseguradoras, telcos y retail en todo el mundo: modelos de scoring crediticio, fuga de clientes, fraude e inteligencia geográfica con datos enriquecidos.",
        "pt": "Análise preditiva com IA para bancos, seguradoras, telcos e varejo em todo o mundo: modelos de score de crédito, churn, fraude e inteligência geográfica com dados enriquecidos.",
    },
    "about": {
        "es": "La historia de Thorcast.AI: fundada por Antonio Latorre y Daniel Jiménez tras años construyendo IA predictiva para instituciones financieras.",
        "pt": "A história da Thorcast.AI: fundada por Antonio Latorre e Daniel Jiménez após anos construindo IA preditiva para instituições financeiras.",
    },
    "tutorials": {
        "es": "Tutoriales en video de Thorcast.AI: prepara datos con NORA, enriquécelos, construye y compara modelos, despliega el scoring y monitorea y recalibra paso a paso.",
        "pt": "Tutoriais em vídeo da Thorcast.AI: prepare dados com a NORA, enriqueça-os, construa e compare modelos, implante o scoring e monitore e recalibre passo a passo.",
    },
}

NODE_EXTRACT = r"""
const fs = require('fs'); const vm = require('vm');
const src = fs.readFileSync(0, 'utf8');
const noop = () => {};
const el = { classList: { toggle: noop, contains: () => false }, setAttribute: noop, addEventListener: noop };
const ctx = {
  window: {}, localStorage: { getItem: () => null, setItem: noop },
  NodeFilter: { SHOW_TEXT: 4, FILTER_REJECT: 2, FILTER_ACCEPT: 1 },
  document: { documentElement: {}, body: {}, title: '', querySelectorAll: () => [], querySelector: () => null,
              getElementById: () => null, addEventListener: noop,
              createTreeWalker: () => ({ nextNode: () => false }) },
  console,
};
vm.createContext(ctx);
vm.runInContext(src + '\n;globalThis.__out = JSON.stringify(THORCAST_I18N);', ctx);
process.stdout.write(ctx.__out);
"""


def extract_dict(page_src):
    scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", page_src, re.S)
    block = next(s for s in scripts if "const THORCAST_I18N" in s)
    res = subprocess.run(["node", "-e", NODE_EXTRACT], input=block, capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


TOKEN = re.compile(r"(<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>|<noscript\b.*?</noscript>|<[^>]+>)", re.S | re.I)
ATTRS = ("alt", "title", "aria-label", "placeholder")


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def translate_text(text, d):
    src = norm(html.unescape(text))
    if not src or src not in d:
        return text, False
    lead = re.match(r"^\s*", text).group(0)
    trail = re.search(r"\s*$", text).group(0)
    return lead + html.escape(d[src], quote=False) + trail, True


def translate_tag(tag, d):
    def rep(m):
        name, q, val = m.group(1), m.group(2), m.group(3)
        src = html.unescape(val)
        if src in d:
            return f'{name}={q}{html.escape(d[src], quote=True)}{q}'
        return m.group(0)
    return re.sub(r'\b(%s)=(["\'])(.*?)\2' % "|".join(ATTRS), rep, tag)


def rewrite_links(s, lang):
    for p in PAGES:
        s = re.sub(r'href="%s\.html(#[^"]*)?"' % p, lambda m, p=p: f'href="{out_name(p, lang)}{m.group(1) or ""}"', s)
    # blog cards: the JS swaps href to data-blog-<lang>; do it statically
    def blog(m):
        tag = m.group(0)
        alt = re.search(r'data-blog-%s="([^"]+)"' % lang, tag)
        if not alt:
            return tag
        return re.sub(r'href="[^"]*"', f'href="{alt.group(1)}"', tag, count=1)
    return re.sub(r"<a\b[^>]*data-blog-link[^>]*>", blog, s)


def hreflang_block(page):
    links = [f'<link rel="alternate" hreflang="en" href="{url(page, "en")}"/>']
    for lang, code in LANGS.items():
        links.append(f'<link rel="alternate" hreflang="{code}" href="{url(page, lang)}"/>')
    links.append(f'<link rel="alternate" hreflang="x-default" href="{url(page, "en")}"/>')
    return "\n".join(links)


LANG_NAV = """<script>/* i18n-nav */(function(){var m=%s;document.querySelectorAll('.lang-btn').forEach(function(b){b.addEventListener('click',function(e){var u=m[b.dataset.lang];if(!u||b.dataset.lang===%s)return;e.stopImmediatePropagation();try{localStorage.setItem('thorcast-lang',b.dataset.lang);}catch(x){}location.href=u+location.hash;},true);});})();</script>"""


def lang_map(page):
    m = {l: out_name(page, l) for l in ["en", *LANGS]}
    if m["en"] == "index.html":
        m["en"] = "./"
    return json.dumps(m)


def build(page, lang, src, d):
    parts = TOKEN.split(src)
    body_started = False
    hits = misses = 0
    out = []
    for part in parts:
        if part.startswith("<") and not part.startswith("<!--"):
            if re.match(r"<body\b", part, re.I):
                body_started = True
            if body_started and not re.match(r"<(script|style|noscript)\b", part, re.I):
                part = translate_tag(part, d)
            out.append(part)
        elif part.startswith("<!--"):
            out.append(part)
        else:
            if body_started:
                part, ok = translate_text(part, d)
                if norm(part):
                    hits += ok
                    misses += (not ok)
            out.append(part)
    s = "".join(out)

    code = LANGS[lang]
    s = re.sub(r'<html\b[^>]*lang="[^"]*"', lambda m: re.sub(r'lang="[^"]*"', f'lang="{code}"', m.group(0)), s, count=1)

    # head: title + meta + canonical + og:url + hreflang
    title_m = re.search(r"<title>(.*?)</title>", s, re.S)
    t_src = html.unescape(title_m.group(1)).strip()
    t_new = d.get(t_src, t_src)
    s = s.replace(title_m.group(0), f"<title>{html.escape(t_new, quote=False)}</title>", 1)
    for prop in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(r'(<meta %s content=")[^"]*(")' % prop, lambda m: m.group(1) + html.escape(t_new) + m.group(2), s)
    desc = META[page][lang]
    for prop in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'(<meta %s content=")[^"]*(")' % prop, lambda m: m.group(1) + html.escape(desc) + m.group(2), s)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url(page, lang) + m.group(2), s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url(page, lang) + m.group(2), s)
    s = re.sub(r'(<meta property="og:locale" content=")[^"]*(")', lambda m: m.group(1) + ("es_ES" if lang == "es" else "pt_BR") + m.group(2), s)
    s = re.sub(r'\n?<link rel="alternate" hreflang="[^"]*" href="[^"]*"/>', "", s)
    s = s.replace("</head>", hreflang_block(page) + "\n</head>", 1)

    # JS: this page is always <lang>; language buttons go to the other pages
    s = re.sub(r"let thorcastCurrentLang = (getStoredThorcastLang\(\) \|\| 'en'|'en');", f"let thorcastCurrentLang = '{lang}';", s, count=1)
    assert f"let thorcastCurrentLang = '{lang}';" in s, page
    s = re.sub(r"\n?<script>/\* i18n-(nav|redirect) \*/.*?</script>", "", s, flags=re.S)
    s = s.replace("</body>", LANG_NAV % (lang_map(page), json.dumps(lang)) + "\n</body>", 1)
    s = re.sub(r'(<button class="lang-btn)( active)?(" type="button" data-lang="(\w+)" aria-pressed=")(true|false)',
               lambda m: f'{m.group(1)}{" active" if m.group(4) == lang else ""}{m.group(3)}{"true" if m.group(4) == lang else "false"}', s)
    s = rewrite_links(s, lang)
    s = ("<!-- GENERATED by tools/build_i18n_pages.py from %s.html — do not edit by hand -->\n" % page) + s
    return s, hits, misses


REDIRECT = """<script>/* i18n-redirect */(function(){try{var l=localStorage.getItem('thorcast-lang'),m=%s;if(m[l])location.replace(m[l]+location.hash);}catch(e){}})();</script>"""


def patch_en(page, src):
    """Idempotent small edits to the English page: hreflang, stored-language
    redirect, and language buttons that navigate instead of translating."""
    s = re.sub(r'\n?<link rel="alternate" hreflang="[^"]*" href="[^"]*"/>', "", src)
    s = re.sub(r"\n?<script>/\* i18n-redirect \*/.*?</script>", "", s, flags=re.S)
    others = json.dumps({l: out_name(page, l) for l in LANGS})
    s = s.replace("</head>", hreflang_block(page) + "\n" + REDIRECT % others + "\n</head>", 1)
    s = s.replace("let thorcastCurrentLang = getStoredThorcastLang() || 'en';", "let thorcastCurrentLang = 'en';", 1)
    s = re.sub(r"\n?<script>/\* i18n-nav \*/.*?</script>", "", s, flags=re.S)
    s = s.replace("</body>", LANG_NAV % (lang_map(page), json.dumps("en")) + "\n</body>", 1)
    return s


def main():
    for page in PAGES:
        path = ROOT / f"{page}.html"
        src = patch_en(page, path.read_text(encoding="utf-8"))
        path.write_text(src, encoding="utf-8")
        dicts = extract_dict(src)
        for lang in LANGS:
            s, hits, misses = build(page, lang, src, dicts[lang])
            (ROOT / out_name(page, lang)).write_text(s, encoding="utf-8")
            print(f"{out_name(page, lang)}: {hits} text nodes translated, {misses} left as is")


if __name__ == "__main__":
    sys.exit(main())
