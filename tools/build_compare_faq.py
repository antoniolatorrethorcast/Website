"""FAQ (EN/ES) and comparison pages, built from the scoring-crediticio-ia.html template. Run from the repo root: python3 tools/build_compare_faq.py
Edit the text in tools/faq_content.py and tools/compare_content.py. Product claims must already be published on thorcast.ai."""
import html, json, re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from faq_content import FAQ_EN, FAQ_ES, FAQ_PT
from compare_content import COMPARE, LANGS, UI, WHY, ENRICH_WHY, T, LABELS, FAQ, fname as cfile

BASE = "https://thorcast.ai/"
OG = BASE + "assets/images/og-image.png"
ORG = {"@type": "Organization", "@id": BASE + "#organization", "name": "Thorcast.AI", "url": BASE,
       "logo": BASE + "assets/images/thorcast-logo.webp", "email": "info@thorcast.ai"}
EXTRA_CSS = ('<style>.cmp-table{width:100%;border-collapse:collapse;margin:8px 0 40px;font-size:14px}'
             '.cmp-table th,.cmp-table td{border:1px solid var(--border-dark);padding:12px 14px;text-align:left;vertical-align:top;color:#b0b8c8;line-height:1.6}'
             '.cmp-table th{color:var(--text-white);background:var(--bg-card);font-weight:700}'
             '.cmp-table td:first-child{color:var(--text-white);font-weight:600;width:24%}'
             '.cmp-wrap{overflow-x:auto}'
             '.faq-item{border-top:1px solid var(--border-dark);padding:22px 0;scroll-margin-top:90px}'
             '.faq-item h2{font-size:19px;margin:0 0 10px}'
             '.article-body .faq-item p{margin:0}'
             '.src{font-size:12px!important;color:var(--text-gray)!important}</style>')

tpl = open("scoring-crediticio-ia.html", encoding="utf-8").read()
tpl = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"/>\n', "", tpl)  # the template's own language links


def one(pattern, repl, s):
    out, n = re.subn(pattern, lambda m: repl, s, count=1, flags=re.S)
    assert n == 1, pattern
    return out


def page(fname, lang, title, desc, tag, h1, meta, body, cta_html, ld_main, crumb, alternates=None):
    url = BASE + fname
    s = tpl
    s = one(r'<html lang="[^"]+">', f'<html lang="{"pt-BR" if lang == "pt" else lang}">', s)
    s = one(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}</title>", s)
    for pat, val in [(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{html.escape(desc)}"/>'),
                     (r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>'),
                     (r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{html.escape(title)}"/>'),
                     (r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{html.escape(desc)}"/>'),
                     (r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{url}"/>'),
                     (r'<meta property="og:locale" content="[^"]*"/>', f'<meta property="og:locale" content="{ {"es": "es_LA", "pt": "pt_BR"}.get(lang, "en_US") }"/>'),
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
    s = s.replace("</body>", "<script>window.addEventListener('load',function(){var h=location.hash,e=h&&document.getElementById(h.slice(1));if(e)setTimeout(function(){e.scrollIntoView({behavior:'auto'});},150);});</script>\n</body>", 1)
    back = {"en": "← Back to home", "es": "← Volver al inicio", "pt": "← Voltar ao início"}[lang]
    home = {"en": "index.html", "es": "es.html", "pt": "pt.html"}[lang]
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
    if lang == "pt":
        return ('<div class="article-footer-cta"><strong>Teste com os seus dados</strong> — uma prova de conceito leva cerca de uma hora: enriquecemos uma amostra, treinamos um modelo desafiante e o comparamos com o seu score atual. '
                '<a href="tutorials-pt.html" style="color: var(--accent-blue); font-style: normal; font-weight: 700;">Ver os tutoriais →</a>'
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
     "Preguntas frecuentes", "PREGUNTAS FRECUENTES", "Preguntas frecuentes", "FAQ in English"),
    ("pt", "perguntas-frequentes.html", FAQ_PT, "Perguntas frequentes sobre a Thorcast.AI — Thorcast.AI",
     "Respostas sobre a Thorcast.AI: o que é, para quem é, que modelos constrói, onde roda, enriquecimento de dados, explicabilidade, integrações e como testar.",
     "Perguntas frequentes", "PERGUNTAS FREQUENTES", "Perguntas frequentes", "")]:
    def faq_item(item):
        q, a = item[0], item[1]
        if len(item) == 2:
            return f'<div class="faq-item"><h2>{html.escape(q)}</h2><p>{html.escape(a)}</p></div>'
        # long answer with a table: show the text without the inline country list, then the table
        m = re.search(r" (Median Gini uplift by country|Alza mediana de Gini por país|Aumento mediano do Gini por país)[^.]*\. [^.]*\.", a)
        lead, tail = (a[:m.start()], a[m.end():]) if m else (a, "")
        return (f'<div class="faq-item" id="gini-uplift"><h2>{html.escape(q)}</h2><p>{html.escape(lead)}</p>'
                f'{item[2]}<p class="src">{html.escape(tail.strip())}</p></div>')
    hub = {"en": ("Recommended topics", [("who-is-it-for.html", "Who Thorcast.AI is for: by industry, team and region"), ("how-to-choose-credit-scoring-software.html", "How to choose credit scoring software: a practical guide"), ("how-to-predict-customer-churn-banking-insurance-telco.html", "How to predict customer churn in banking, insurance and telco"), ("thorcast-vs-datarobot.html", "Thorcast.AI vs DataRobot"), ("thorcast-vs-h2o.html", "Thorcast.AI vs H2O.ai"), ("thorcast-vs-sas.html", "Thorcast.AI vs SAS Viya"), ("tutorials.html", "Video tutorials")]),
           "es": ("Temas recomendados", [("para-quien-es.html", "Para quién es Thorcast.AI: por industria, equipo y región"), ("como-elegir-software-scoring-crediticio.html", "Cómo elegir software de scoring crediticio: guía práctica"), ("como-predecir-churn-banca-seguros-telco.html", "Cómo predecir la fuga de clientes en banca, seguros y telco"), ("thorcast-vs-datarobot-es.html", "Thorcast.AI vs DataRobot"), ("thorcast-vs-h2o-es.html", "Thorcast.AI vs H2O.ai"), ("thorcast-vs-sas-es.html", "Thorcast.AI vs SAS Viya"), ("tutorials-es.html", "Tutoriales en video")]),
           "pt": ("Temas recomendados", [("para-quem-e.html", "Para quem é a Thorcast.AI: por setor, equipe e região"), ("como-escolher-software-de-credit-scoring.html", "Como escolher software de credit scoring: guia prático"), ("como-prever-churn-bancos-seguros-telecom.html", "Como prever o churn de clientes em bancos, seguros e telecom"), ("credit-scoring-com-ia.html", "Credit scoring com IA"), ("thorcast-vs-datarobot-pt.html", "Thorcast.AI vs DataRobot"), ("thorcast-vs-h2o-pt.html", "Thorcast.AI vs H2O.ai"), ("thorcast-vs-sas-pt.html", "Thorcast.AI vs SAS Viya"), ("tutorials-pt.html", "Tutoriais em vídeo")])}[lang]
    body = (f'<div class="article-footer-cta" style="margin:0 0 32px;font-style:normal"><strong>{hub[0]}</strong><ul style="margin:10px 0 0;padding-left:20px">'
            + "".join(f'<li style="margin:6px 0"><a href="{h}" style="color:var(--accent-blue);font-weight:700">{html.escape(t)}</a></li>' for h, t in hub[1]) + "</ul></div>")
    body += "".join(faq_item(it) for it in items)
    others = {"en": [("preguntas-frecuentes.html", "Preguntas frecuentes en español"), ("perguntas-frequentes.html", "Perguntas frequentes em português")],
              "es": [("faq.html", "FAQ in English"), ("perguntas-frequentes.html", "Perguntas frequentes em português")],
              "pt": [("faq.html", "FAQ in English"), ("preguntas-frecuentes.html", "Preguntas frecuentes en español")]}[lang]
    comps = "".join(f'<li><a href="{cfile(c["base"], lang)}">{html.escape(c[lang]["h1"])}</a></li>' for c in COMPARE)
    body += (f'<h2>{ {"en": "Compare Thorcast", "es": "Compara Thorcast", "pt": "Compare a Thorcast"}[lang] }</h2><ul>{comps}</ul>'
             + "".join(f'<p><a href="{h}">{t} →</a></p>' for h, t in others))
    ld = {"@type": "FAQPage", "inLanguage": "pt-BR" if lang == "pt" else lang, "mainEntity": [
        {"@type": "Question", "name": it[0], "acceptedAnswer": {"@type": "Answer", "text": it[1]}} for it in items], "publisher": ORG}
    page(fname, lang, title, desc, tag, h1, "Thorcast.AI", body, cta(lang), ld, crumb,
         alternates=[("en", "faq.html"), ("es", "preguntas-frecuentes.html"), ("pt-BR", "perguntas-frequentes.html"), ("x-default", "faq.html")])

# ---------- comparisons (EN / ES / PT)
for c in COMPARE:
    alts = [("en", cfile(c["base"], "en")), ("es", cfile(c["base"], "es")), ("pt-BR", cfile(c["base"], "pt")), ("x-default", cfile(c["base"], "en"))]
    for lang in LANGS:
        L, ui = c[lang], UI[lang]
        rows = "".join(f"<tr><td>{html.escape(LABELS[lang][k])}</td><td>{T[lang][k]}</td><td>{L['them'][k]}</td></tr>" for k in c["rows"])
        table = (f'<div class="cmp-wrap"><table class="cmp-table"><thead><tr><th></th><th>Thorcast.AI</th><th>{html.escape(c["name"])}</th></tr></thead>'
                 f"<tbody>{rows}</tbody></table></div>")
        choose = (f'<h2>{ui["when_them"].format(n=html.escape(c["name"]))}</h2><ul>' + "".join(f"<li>{x}</li>" for x in L["choose_them"]) + "</ul>"
                  f'<h2>{ui["when_us"]}</h2><ul>' + "".join(f"<li>{x}</li>" for x in WHY[lang] + [ENRICH_WHY[lang]]) + "</ul>")
        sources = ui["src"].format(n=c["name"]) + " · ".join(f'<a href="{u}" target="_blank" rel="noopener noreferrer">{t}</a>' for u, t in c["sources"]) + ui["tm"].format(tm=c["tm"][lang])
        others = "".join(f'<li><a href="{cfile(o["base"], lang)}">{html.escape(o[lang]["h1"])}</a></li>' for o in COMPARE if o is not c)
        body = "\n".join([L["intro"], f'<h2>{ui["glance"]}</h2>', table, choose, '<p class="src">' + sources + "</p>",
                          f'<h2>{ui["more"]}</h2><ul>{others}<li><a href="{FAQ[lang]}">{ui["faq"]}</a></li></ul>'])
        f = cfile(c["base"], lang)
        ld = {"@type": "WebPage", "name": L["h1"], "description": L["desc"], "url": BASE + f, "inLanguage": "pt-BR" if lang == "pt" else lang,
              "dateModified": c.get("date", "2026-11-23"), "publisher": ORG,
              "about": [{"@type": "SoftwareApplication", "name": "Thorcast.AI", "applicationCategory": "BusinessApplication", "url": BASE},
                        {"@type": "SoftwareApplication", "name": c["name"], "applicationCategory": "BusinessApplication", "url": c["url"]}]}
        page(f, lang, L["title"], L["desc"], ui["tag"], L["h1"], ui["meta"], body, cta(lang), ld, L["h1"], alternates=alts)

# ---------- "Who it's for" (EN / ES / PT)
from who_for_content import WHO, FILES as WHO_FILES
_alts = [("en", WHO_FILES["en"]), ("es", WHO_FILES["es"]), ("pt-BR", WHO_FILES["pt"]), ("x-default", WHO_FILES["en"])]
for lang, W in WHO.items():
    parts = [W["intro"], f'<h2>{W["ind_h"]}</h2>']
    parts += [f'<div class="faq-item"><h2>{html.escape(n)}</h2><p>{html.escape(t)}</p></div>' for n, t in W["industries"]]
    parts.append(f'<h2>{W["team_h"]}</h2><ul>' + "".join(f"<li><strong>{html.escape(n)}.</strong> {html.escape(t)}</li>" for n, t in W["teams"]) + "</ul>")
    parts += [f'<h2>{W["region_h"]}</h2>', W["region"]]
    parts.append(f'<h2>{W["notfit_h"]}</h2><ul>' + "".join(f"<li>{html.escape(x)}</li>" for x in W["notfit"]) + "</ul>")
    parts.append(f'<h2>{W["more_h"]}</h2><ul>' + "".join(f'<li><a href="{f}">{html.escape(t)}</a></li>' for f, t in W["more"]) + "</ul>")
    f = WHO_FILES[lang]
    ld = {"@type": "WebPage", "name": W["h1"], "description": W["desc"], "url": BASE + f, "inLanguage": "pt-BR" if lang == "pt" else lang,
          "publisher": ORG, "about": {"@type": "SoftwareApplication", "name": "Thorcast.AI", "applicationCategory": "BusinessApplication", "url": BASE},
          "audience": [{"@type": "BusinessAudience", "name": n} for n, _ in W["industries"]]}
    page(f, lang, W["title"], W["desc"], W["tag"], W["h1"], W["meta"], "\n".join(parts), cta(lang), ld, W["crumb"], alternates=_alts)

# ---------- Guides (ES / EN / PT): how to choose credit scoring software, how to predict churn
import guide_content, guide_content_en, guide_content_pt
import churn_guide_content, churn_guide_content_en, churn_guide_content_pt
_e = html.escape
_LANG_ATTR = {"es": "es", "en": "en", "pt": "pt-BR"}


def _alts(mods):
    return [(_LANG_ATTR[l], m.FILE) for l, m in mods.items()] + [("x-default", mods["en"].FILE)]


def _article_ld(M, lang):
    return {"@type": "Article", "headline": M.H1, "description": M.DESC, "url": BASE + M.FILE, "inLanguage": _LANG_ATTR[lang],
            "datePublished": M.DATE, "dateModified": M.DATE, "author": ORG, "publisher": ORG, "image": OG,
            "about": {"@type": "Thing", "name": M.ABOUT}}


_GUIDES = {"es": guide_content, "en": guide_content_en, "pt": guide_content_pt}
for lang, G in _GUIDES.items():
    pro, con, when, heads = G.LABELS
    _g = [G.INTRO, f"<h2>{G.BEFORE_H}</h2><ul>" + "".join(f"<li><strong>{_e(n)}.</strong> {_e(t)}</li>" for n, t in G.BEFORE) + "</ul>",
          f"<h2>{G.TYPES_H}</h2>", G.TYPES_P]
    for name, what, p_, c_, w_ in G.TYPES:
        _g.append(f'<div class="faq-item"><h2>{_e(name)}</h2><p>{what}</p><ul><li><strong>{pro}</strong> {_e(p_)}</li>'
                  f'<li><strong>{con}</strong> {_e(c_)}</li><li><strong>{when}</strong> {w_}</li></ul></div>')
    _rows = "".join(f"<tr><td>{_e(c)}</td><td>{_e(q)}</td><td>{_e(f)}</td></tr>" for c, q, f in G.CRIT)
    _g.append(f'<h2>{G.CRIT_H}</h2><div class="cmp-wrap"><table class="cmp-table"><thead><tr>' + "".join(f"<th>{h}</th>" for h in heads)
              + f"</tr></thead><tbody>{_rows}</tbody></table></div>")
    _g.append(f"<h2>{G.POC_H}</h2><ol>" + "".join(f"<li>{x}</li>" for x in G.POC) + "</ol>")
    _g.append(f"<h2>{G.DEC_H}</h2>{G.DEC}")
    _g.append(f"<h2>{G.FLAGS_H}</h2><ul>" + "".join(f"<li>{_e(x)}</li>" for x in G.FLAGS) + "</ul>")
    _g.append(f"<h2>{G.FIT_H}</h2>{G.FIT_P}<ul>" + "".join(f"<li>{x}</li>" for x in WHY[lang] + [ENRICH_WHY[lang]]) + "</ul>"
              + G.NOT_FIT_P + "<ul>" + "".join(f"<li>{_e(x)}</li>" for x in G.NOT_FIT) + "</ul>")
    _g.append(f"<h2>{G.FAQ_H}</h2>" + "".join(f'<div class="faq-item"><h2>{_e(q)}</h2><p>{_e(a)}</p></div>' for q, a in G.FAQ))
    _g.append(f"<h2>{G.MORE_H}</h2><ul>" + "".join(f'<li><a href="{f}">{_e(t)}</a></li>' for f, t in G.MORE) + "</ul>")
    page(G.FILE, lang, G.TITLE, G.DESC, G.TAG, G.H1, G.META, "\n".join(_g), cta(lang), _article_ld(G, lang), G.CRUMB, alternates=_alts(_GUIDES))

_CHURN = {"es": churn_guide_content, "en": churn_guide_content_en, "pt": churn_guide_content_pt}
for lang, C in _CHURN.items():
    _c = [C.INTRO, f"<h2>{C.DEF_H}</h2>{C.DEF_P}"]
    _c += [f'<div class="faq-item"><h2>{_e(n)}</h2><p>{_e(t)}</p></div>' for n, t in C.DEFS]
    _c.append(f"<h2>{C.DATA_H}</h2><ul>" + "".join(f"<li>{x}</li>" for x in C.DATA) + "</ul>")
    _c.append(f"<h2>{C.MEASURE_H}</h2>{C.MEASURE}<ul>" + "".join(f"<li><strong>{_e(n)}.</strong> {_e(t)}</li>" for n, t in C.CASES) + "</ul>")
    _c.append(f"<h2>{C.VALUE_H}</h2><ul>" + "".join(f"<li>{x}</li>" for x in C.VALUE) + "</ul>")
    _c.append(f"<h2>{C.DEC_H}</h2>{C.DEC}")
    _c.append(f"<h2>{C.MISTAKES_H}</h2><ul>" + "".join(f"<li>{_e(x)}</li>" for x in C.MISTAKES) + "</ul>")
    _c.append(f"<h2>{C.FIT_H}</h2><ul>" + "".join(f"<li>{x}</li>" for x in C.FIT) + "</ul>")
    _c.append(f"<h2>{C.FAQ_H}</h2>" + "".join(f'<div class="faq-item"><h2>{_e(q)}</h2><p>{_e(a)}</p></div>' for q, a in C.FAQ))
    _c.append(f"<h2>{C.MORE_H}</h2><ul>" + "".join(f'<li><a href="{f}">{_e(t)}</a></li>' for f, t in C.MORE) + "</ul>")
    page(C.FILE, lang, C.TITLE, C.DESC, C.TAG, C.H1, C.META, "\n".join(_c), cta(lang), _article_ld(C, lang), C.CRUMB, alternates=_alts(_CHURN))
