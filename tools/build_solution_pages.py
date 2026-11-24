"""English and Portuguese versions of the Spanish use-case pages. Run from the repo root:
python3 tools/build_solution_pages.py   (needs ffprobe for the video durations)
Text lives in tools/solution_content.py. Each page is built from its Spanish page, so layout,
styles, nav and footer stay identical; this script also adds hreflang links to the Spanish pages."""
import html, json, re, subprocess, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from solution_content import PAGES, SHARED, LANGS

BASE = "https://thorcast.ai/"
ORG = {"@type": "Organization", "@id": BASE + "#organization", "name": "Thorcast.AI", "url": BASE,
       "logo": BASE + "assets/images/thorcast-logo.webp", "email": "info@thorcast.ai"}
LANG_ATTR = {"es": "es", "en": "en", "pt": "pt-BR"}
LOCALE = {"en": "en_US", "pt": "pt_BR"}
LINK = 'style="color: var(--accent-blue); font-style: normal; font-weight: 700;"'
e = html.escape


def one(pattern, repl, s):
    out, n = re.subn(pattern, lambda m: repl, s, count=1, flags=re.S)
    assert n == 1, pattern
    return out


def duration(path):
    sec = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path])))
    return f"PT{sec // 60}M{sec % 60}S"


def with_alternates(s, p):
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"/>\n', "", s)
    files = {"es": p["es"], **p["files"]}
    links = "".join(f'<link rel="alternate" hreflang="{LANG_ATTR[l]}" href="{BASE + f}"/>\n' for l, f in files.items())
    links += f'<link rel="alternate" hreflang="x-default" href="{BASE + files["en"]}"/>\n'
    return s.replace("</head>", links + "</head>", 1)


for p in PAGES:
    es_src = open(p["es"], encoding="utf-8").read()
    for lang in LANGS:
        L, S, f = p[lang], SHARED[lang], p["files"][lang]
        url = BASE + f
        s = one(r'<html lang="[^"]+">', f'<html lang="{LANG_ATTR[lang]}">', es_src)
        s = one(r"<title>.*?</title>", f"<title>{e(L['title'], quote=False)}</title>", s)
        for pat, val in [(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{e(L["desc"])}"/>'),
                         (r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>'),
                         (r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{e(L["title"])}"/>'),
                         (r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{e(L["desc"])}"/>'),
                         (r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{url}"/>'),
                         (r'<meta property="og:locale" content="[^"]*"/>', f'<meta property="og:locale" content="{LOCALE[lang]}"/>'),
                         (r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{e(L["title"])}"/>'),
                         (r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{e(L["desc"])}"/>')]:
            s = one(pat, val, s)
        page_ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "WebPage", "name": L["h1"], "description": L["desc"], "url": url, "inLanguage": LANG_ATTR[lang], "publisher": ORG,
             "about": {"@type": "SoftwareApplication", "name": "Thorcast.AI", "applicationCategory": "BusinessApplication", "url": BASE}},
            {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Thorcast.AI", "item": BASE},
                                                            {"@type": "ListItem", "position": 2, "name": L["crumb"], "item": url}]}]}
        vids, cards = [], []
        for v, (ct, cs), name, desc in zip(p["videos"], L["cards"], L["vnames"], L["vdescs"]):
            mp4, cover = f"assets/use-cases/{v}.{lang}.mp4", f"assets/use-cases/{v}-cover.{lang}.webp"
            assert os.path.exists(mp4) and os.path.exists(cover), v
            vids.append({"@type": "VideoObject", "name": name, "description": desc, "thumbnailUrl": BASE + cover, "uploadDate": "2026-11-20",
                         "duration": duration(mp4), "contentUrl": BASE + mp4, "inLanguage": LANG_ATTR[lang]})
            cards.append(f'<div class="uc-card"><video controls preload="none" playsinline poster="{cover}" src="{mp4}" aria-label="{e(ct)}"></video>'
                         f"<h3>{e(ct)}</h3><p>{e(cs)}</p></div>")
        lds = re.findall(r'<script type="application/ld\+json">.*?</script>', s, flags=re.S)
        assert len(lds) == 2
        for ld in lds:
            new = page_ld if "VideoObject" not in ld else {"@context": "https://schema.org", "@graph": vids}
            s = s.replace(ld, '<script type="application/ld+json">' + json.dumps(new, ensure_ascii=False) + "</script>", 1)
        s = with_alternates(s, p)
        hero = (f'\n<a class="article-back" href="{S["home"]}">{S["back"]}</a>\n<div class="article-tag">{e(L["tag"])}</div>\n'
                f'<h1 class="article-title">{e(L["h1"])}</h1>\n<div class="article-meta">{S["meta"]}</div>\n')
        s = one(r'(<section id="article-hero">).*?(</section>)', '<section id="article-hero">' + hero + "</section>", s)
        others = [(q["files"][lang], q[lang]["crumb"]) for q in PAGES if q is not p]
        body = "\n".join([
            '<div class="article-body">', L["intro"], f'<h2>{S["solve_h"]}</h2>', "<ul>\n" + "\n".join(f"<li>{x}</li>" for x in L["solve"]) + "\n</ul>",
            f'<h2>{S["videos_h"]}</h2>', '<div class="uc-grid">' + "".join(cards) + "</div>",
            f'<h2>{S["build_h"]}</h2>', "<ul>\n" + "\n".join(f"<li>{x}</li>" for x in S["build"]) + "\n</ul>", f'<p>{S["build_p"]}</p>',
            f'<h2>{S["data_h"]}</h2>', f'<p>{S["data_p"]}</p>',
            '<div class="sig-grid">\n' + "\n".join(f'<div class="sig"><b>{n}</b><p>{t}</p></div>' for n, t in S["sigs"]) + "\n</div>",
            f'<h2>{L["extra"][0]}</h2>', L["extra"][1],
            f'<h2>{S["more_h"]}</h2>', "<ul>" + "".join(f'<li><a href="{h}">{e(t)}</a></li>' for h, t in L["more"]) + "</ul>",
            f'<h2>{S["others_h"]}</h2>', "<ul>" + "".join(f'<li><a href="{h}">{e(t)}</a></li>' for h, t in others) + "</ul>",
            "</div>",
            f'<div class="article-footer-cta"><strong>{S["cta_lead"]}</strong> — {L["cta"]} <a href="{S["tutorials"]}" {LINK}>{S["cta_link"]}</a>'
            f' · <a href="mailto:info@thorcast.ai" {LINK}>info@thorcast.ai</a></div>'])
        s = one(r'<section id="article-body">.*?</section>', '<section id="article-body">\n' + body + "\n</section>", s)
        open(f, "w", encoding="utf-8").write(s)
        print("wrote", f, len(L["title"]), len(L["desc"]))
    open(p["es"], "w", encoding="utf-8").write(with_alternates(es_src, p))
