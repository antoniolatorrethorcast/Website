"""FAQ (EN/ES) and comparison pages, built from the scoring-crediticio-ia.html template. Run from the repo root: python3 tools/build_compare_faq.py
Edit the text in tools/faq_content.py and tools/compare_content.py. Product claims must already be published on thorcast.ai."""
import html, json, re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from faq_content import FAQ_EN, FAQ_ES
from compare_content import COMPARE

BASE = "https://thorcast.ai/"
OG = BASE + "assets/images/og-image.png"
ORG = {"@type": "Organization", "@id": BASE + "#organization", "name": "Thorcast.AI", "url": BASE,
       "logo": BASE + "assets/images/thorcast-logo.webp", "email": "info@thorcast.ai"}
EXTRA_CSS = ('<style>.cmp-table{width:100%;border-collapse:collapse;margin:8px 0 40px;font-size:14px}'
             '.cmp-table th,.cmp-table td{border:1px solid var(--border-dark);padding:12px 14px;text-align:left;vertical-align:top;color:#b0b8c8;line-height:1.6}'
             '.cmp-table th{color:var(--text-white);background:var(--bg-card);font-weight:700}'
             '.cmp-table td:first-child{color:var(--text-white);font-weight:600;width:24%}'
             '.cmp-wrap{overflow-x:auto}'
             '.faq-item{border-top:1px solid var(--border-dark);padding:22px 0}'
             '.faq-item h2{font-size:19px;margin:0 0 10px}'
             '.article-body .faq-item p{margin:0}'
             '.src{font-size:12px!important;color:var(--text-gray)!important}</style>')

tpl = open("scoring-crediticio-ia.html", encoding="utf-8").read()


def one(pattern, repl, s):
    out, n = re.subn(pattern, lambda m: repl, s, count=1, flags=re.S)
    assert n == 1, pattern
    return out


def page(fname, lang, title, desc, tag, h1, meta, body, cta_html, ld_main, crumb, alternates=None):
    url = BASE + fname
    s = tpl
    s = one(r'<html lang="[^"]+">', f'<html lang="{lang}">', s)
    s = one(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}</title>", s)
    for pat, val in [(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{html.escape(desc)}"/>'),
                     (r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>'),
                     (r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{html.escape(title)}"/>'),
                     (r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{html.escape(desc)}"/>'),
                     (r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{url}"/>'),
                     (r'<meta property="og:locale" content="[^"]*"/>', f'<meta property="og:locale" content="{"es_LA" if lang == "es" else "en_US"}"/>'),
                     (r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{html.escape(title)}"/>'),
                     (r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{html.escape(desc)}"/>')]:
        s = one(pat, val, s)
    # replace all JSON-LD with ours
    s = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", s, flags=re.S)
    ld = {"@context": "https://schema.org", "@graph": [ld_main, {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Thorcast.AI", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]}]}
    head_add = EXTRA_CSS + '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"
    if alternates:
        head_add += "".join(f'\n<link rel="alternate" hreflang="{h}" href="{BASE + f}"/>' for h, f in alternates)
    s = s.replace("</head>", head_add + "\n</head>", 1)
    back = "← Back to home" if lang == "en" else "← Volver al inicio"
    home = "index.html" if lang == "en" else "es.html"
    s = one(r'<a class="article-back" href="[^"]*">[^<]*</a>', f'<a class="article-back" href="{home}">{back}</a>', s)
    s = one(r'<div class="article-tag">.*?</div>', f'<div class="article-tag">{html.escape(tag, quote=False)}</div>', s)
    s = one(r'<h1 class="article-title">.*?</h1>', f'<h1 class="article-title">{html.escape(h1, quote=False)}</h1>', s)
    s = one(r'<div class="article-meta">.*?</div>', f'<div class="article-meta">{html.escape(meta, quote=False)}</div>', s)
    section = '<section id="article-body">\n<div class="article-body">\n' + body + '\n</div>\n' + cta_html + '\n</section>'
    s = one(r'<section id="article-body">.*?</section>', section, s)
    s = s.replace('src="assets/use-cases/', 'src="assets/use-cases/')  # no-op, template has no videos after body swap
    for bad in ("uc-grid\"><div", "Scoring crediticio con IA: más créditos"):
        assert bad not in s.split('<section id="article-body">')[1], (fname, bad)
    open(fname, "w", encoding="utf-8").write(s)
    print("wrote", fname, len(title), len(desc))


def cta(lang):
    if lang == "en":
        return ('<div class="article-footer-cta"><strong>Try it with your data</strong> — a proof of concept takes about an hour: we enrich a sample, train a challenger model and compare it with your current score. '
                '<a href="tutorials.html" style="color: var(--accent-blue); font-style: normal; font-weight: 700;">Watch the tutorials →</a>'
                ' · <a href="mailto:info@thorcast.ai" style="color: var(--accent-blue); font-style: normal; font-weight: 700;">info@thorcast.ai</a></div>')
    return ('<div class="article-footer-cta"><strong>Pruébalo con tus datos</strong> — una prueba de concepto toma alrededor de una hora: enriquecemos una muestra, entrenamos un modelo desafiante y lo comparamos con tu score actual. '
            '<a href="tutorials-es.html" style="color: var(--accent-blue); font-style: normal; font-weight: 700;">Ver los tutoriales →</a>'
            ' · <a href="mailto:info@thorcast.ai" style="color: var(--accent-blue); font-style: normal; font-weight: 700;">info@thorcast.ai</a></div>')


# ---------- FAQ
for lang, fname, items, title, desc, h1, tag, crumb, other in [
    ("en", "faq.html", FAQ_EN, "Thorcast.AI FAQ: AI predictive analytics platform",
     "Answers about Thorcast.AI: what it is, who it is for, which models it builds, where it runs, data enrichment, explainability, integrations and how to try it.",
     "Frequently asked questions", "FAQ", "FAQ", "Preguntas frecuentes en español"),
    ("es", "preguntas-frecuentes.html", FAQ_ES, "Preguntas frecuentes sobre Thorcast.AI — Thorcast.AI",
     "Respuestas sobre Thorcast.AI: qué es, para quién es, qué modelos construye, dónde corre, enriquecimiento de datos, explicabilidad, integraciones y cómo probarlo.",
     "Preguntas frecuentes", "PREGUNTAS FRECUENTES", "Preguntas frecuentes", "FAQ in English")]:
    body = "".join(f'<div class="faq-item"><h2>{html.escape(q)}</h2><p>{html.escape(a)}</p></div>' for q, a in items)
    other_f = "preguntas-frecuentes.html" if lang == "en" else "faq.html"
    comps = "".join(f'<li><a href="{c["file"]}">{html.escape(c["h1"])}</a></li>' for c in COMPARE)
    body += (f'<h2>{"Compare Thorcast" if lang == "en" else "Compara Thorcast (en inglés)"}</h2><ul>{comps}</ul>'
             f'<p><a href="{other_f}">{other} →</a></p>')
    ld = {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items], "publisher": ORG}
    page(fname, lang, title, desc, tag, h1, "Thorcast.AI", body, cta(lang), ld, crumb,
         alternates=[("en", "faq.html"), ("es", "preguntas-frecuentes.html"), ("x-default", "faq.html")])

# ---------- comparisons (EN)
for c in COMPARE:
    rows = "".join(f"<tr><td>{html.escape(k)}</td><td>{t}</td><td>{o}</td></tr>" for k, t, o in c["rows"])
    table = (f'<div class="cmp-wrap"><table class="cmp-table"><thead><tr><th></th><th>Thorcast.AI</th><th>{html.escape(c["name"])}</th></tr></thead>'
             f"<tbody>{rows}</tbody></table></div>")
    others = "".join(f'<li><a href="{o["file"]}">{html.escape(o["h1"])}</a></li>' for o in COMPARE if o is not c)
    body = "\n".join([c["intro"], "<h2>At a glance</h2>", table, c["choose"],
                      '<p class="src">' + c["sources"] + "</p>",
                      f'<h2>More comparisons</h2><ul>{others}<li><a href="faq.html">Thorcast.AI FAQ</a></li></ul>'])
    ld = {"@type": "WebPage", "name": c["h1"], "description": c["desc"], "url": BASE + c["file"], "inLanguage": "en",
          "dateModified": "2026-11-23", "publisher": ORG,
          "about": [{"@type": "SoftwareApplication", "name": "Thorcast.AI", "applicationCategory": "BusinessApplication", "url": BASE},
                    {"@type": "SoftwareApplication", "name": c["name"], "applicationCategory": "BusinessApplication", "url": c["url"]}]}
    page(c["file"], "en", c["title"], c["desc"], "COMPARISON", c["h1"], "Thorcast.AI · Updated November 2026",
         body, cta("en"), ld, c["h1"])
