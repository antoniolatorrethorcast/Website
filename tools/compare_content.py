"""Comparison pages. Thorcast claims = only what thorcast.ai already publishes.
Competitor claims = vendor pages verified 2026-11-23 (links in each page's sources line)."""

T_AGENTS = "Two built-in agents: <strong>NORA</strong> prepares data from plain-language instructions and <strong>MJÖ</strong> builds, compares and explains models. Every plan waits for your approval."
T_PREP = "NORA merges, cleans and engineers your tables; every step is checked by a deterministic validation engine. You get a versioned dataset, reproducible Python and a reusable Playbook."
T_AUTOML = "MJÖ plans the preprocessing, recommends variables, trains and compares several algorithms and presents the champion with Gini, KS and ROC."
T_ENRICH = "Built in: the Data Enrichment Network adds 3,000+ data points (261 model-ready signals) from an address, email or phone. Across 68 models in 12 countries it raised Gini by a median of 35% (<a href=\"faq.html#gini-uplift\">results by country</a>). Coverage depends on the country."
T_EXPLAIN = "Plain-language explanation from MJÖ and an audit-ready technical report. AI plans, validated code executes: same input, same result."
T_DECIDE = "Decision layers show approval, risk and economic impact for every cutoff; Champion–Challenger and batch scoring included."
T_DEPLOY = "Thorcast Cloud, on your premises, or in the app. Data preparation, training and scoring can run on your infrastructure."
T_START = "One-hour proof of concept with your own sample. Pricing not published; write to info@thorcast.ai."
T_FIT = "Banks, insurers, brokers, telcos and retailers that want production-grade models without a large data science team, or want their team to cover more use cases."

A = lambda url, txt: f'<a href="{url}" target="_blank" rel="noopener noreferrer">{txt}</a>'

COMPARE = [
dict(
    file="thorcast-vs-datarobot.html", name="DataRobot", url="https://www.datarobot.com/",
    title="Thorcast.AI vs DataRobot: AutoML compared (2026)",
    h1="Thorcast.AI vs DataRobot",
    desc="An honest comparison of Thorcast.AI and DataRobot: AI agents, data preparation, AutoML, built-in data enrichment, explainability, deployment and when to choose each.",
    intro="""<p><strong>DataRobot</strong> is a broad enterprise AI platform that today positions itself around building, operating and governing AI agents, alongside its long-standing AutoML. <strong>Thorcast.AI</strong> is narrower: a predictive analytics platform for banks, insurers, telcos and retailers, where two AI agents take a model from raw data to a business decision, with alternative data built in.</p>
<p>Both run in the cloud or on your premises and both produce explainable models. The main differences are scope, who does the work, and where the extra data comes from.</p>""",
    rows=[
        ("What it is", "Predictive analytics platform with AI agents for credit, fraud, churn, cross-sell, pricing and geo use cases.", "Enterprise platform to build, operate and govern AI agents and predictive models across industries."),
        ("AI agents", T_AGENTS, "Agent Workforce Platform and agent builder for creating your own agents; AutoML and a GenAI workbench."),
        ("Data preparation", T_PREP, "Feature Discovery joins and aggregates your own related datasets into features."),
        ("AutoML", T_AUTOML, "Mature AutoML with leaderboards, monotonic constraints on some models and many algorithm families."),
        ("Built-in third-party data", T_ENRICH, "No native third-party data enrichment found; you bring your own data."),
        ("Explainability & documentation", T_EXPLAIN, "Prediction Explanations (SHAP, XEMP) and compliance documentation templates aimed at SR 11-7, exportable to .docx."),
        ("From score to decision", T_DECIDE, "Deployment, monitoring and governance of models and agents."),
        ("Deployment", T_DEPLOY, "Multi-tenant or single-tenant SaaS, self-managed VPC, or on-premise including air-gapped."),
        ("Getting started", T_START, "30-day free trial; pricing not published."),
        ("Best fit", T_FIT, "Large enterprises with data science teams that want one platform for many AI and agent projects."),
    ],
    choose="""<h2>When to choose DataRobot</h2>
<ul><li>You need one enterprise platform for many kinds of AI, including building and governing your own agents.</li>
<li>You have an experienced data science team and existing data pipelines, and you want to self-serve a 30-day trial.</li>
<li>You need SaaS, VPC or air-gapped deployment from a large vendor across many business units.</li></ul>
<h2>When to choose Thorcast.AI</h2>
<ul><li>Your priority is credit risk, fraud, churn, cross-sell or pricing models, and you want agents that do the data preparation and modeling for you.</li>
<li>Your current model is missing data: you want alternative data from an address, email or phone without buying and integrating a new provider.</li>
<li>You want the model to end in a business decision: cutoffs with economic impact, Champion–Challenger and monitoring.</li></ul>""",
    sources="Sources (DataRobot, checked November 2026): " + " · ".join([
        A("https://www.datarobot.com/", "datarobot.com"),
        A("https://www.datarobot.com/platform/deployment-self-managed/", "self-managed deployment"),
        A("https://www.datarobot.com/trial/", "trial"),
        A("https://docs.datarobot.com/en/modeling/analyze-models/understand/pred-explain/predex-overview.html", "prediction explanations"),
        A("https://docs.datarobot.com/en/modeling/analyze-models/compliance/compliance.html", "compliance documentation"),
        A("https://docs.datarobot.com/en/data/transform-data/feature-discovery/index.html", "Feature Discovery")]) +
        ". Vendor capabilities change; check their site for the latest. DataRobot is a trademark of its owner.",
),
dict(
    file="thorcast-vs-h2o.html", name="H2O.ai", url="https://h2o.ai/",
    title="Thorcast.AI vs H2O.ai Driverless AI compared (2026)",
    h1="Thorcast.AI vs H2O.ai",
    desc="An honest comparison of Thorcast.AI and H2O.ai Driverless AI: AI agents, AutoML, built-in data enrichment, explainability, deployment and when to choose each.",
    intro="""<p><strong>H2O.ai</strong> offers H2O AI Cloud, Driverless AI for AutoML and the open-source H2O-3 library, and positions itself as a sovereign AI platform you can run anywhere, from the cloud to fully air-gapped. <strong>Thorcast.AI</strong> is a predictive analytics platform for banks, insurers, telcos and retailers, where two AI agents take a model from raw data to a business decision, with alternative data built in.</p>
<p>Both are strong on automated modeling and explainability. They differ in who drives the work, in data enrichment, and in how much of the path to a business decision is covered.</p>""",
    rows=[
        ("What it is", "Predictive analytics platform with AI agents for credit, fraud, churn, cross-sell, pricing and geo use cases.", "AI platform (H2O AI Cloud) with Driverless AI for AutoML, generative AI tooling and open-source H2O-3."),
        ("AI agents", T_AGENTS, "H2O AI Super Agent and an Agents Builder (including Deep Research and Data Science agents)."),
        ("Data preparation", T_PREP, "Automatic feature engineering inside Driverless AI; data preparation otherwise done by your team."),
        ("AutoML", T_AUTOML, "Driverless AI AutoML with automatic feature engineering; open-source H2O AutoML in H2O-3."),
        ("Built-in third-party data", T_ENRICH, "No native third-party data found; its credit page asks you to bring your own bureau and alternative data."),
        ("Explainability & documentation", T_EXPLAIN, "Reason codes on every prediction (Shapley, K-LIME), AutoDoc for model risk review and disparate impact analysis."),
        ("From score to decision", T_DECIDE, "Model deployment and monitoring within H2O AI Cloud."),
        ("Deployment", T_DEPLOY, "Managed cloud, hybrid (your cloud, on-premise or air-gapped) and a government cloud."),
        ("Getting started", T_START, "H2O-3 is free and open source; enterprise platform by demo; pricing not published."),
        ("Best fit", T_FIT, "Data science teams that want a powerful AutoML engine and open-source options, often with sovereign or air-gapped requirements."),
    ],
    choose="""<h2>When to choose H2O.ai</h2>
<ul><li>Your data scientists want open-source building blocks (H2O-3) or a high-performance AutoML engine they drive themselves.</li>
<li>You need sovereign or fully air-gapped AI across many use cases, including generative AI.</li>
<li>You already have your bureau and alternative data integrated.</li></ul>
<h2>When to choose Thorcast.AI</h2>
<ul><li>You want agents to do the data preparation and modeling, with your team approving each plan instead of building pipelines.</li>
<li>You want alternative data from an address, email or phone included, without a separate data project.</li>
<li>You want the model to end in a decision: cutoffs with economic impact, Champion–Challenger and monitoring, in one place.</li></ul>""",
    sources="Sources (H2O.ai, checked November 2026): " + " · ".join([
        A("https://h2o.ai/platform/ai-cloud/", "H2O AI Cloud"),
        A("https://h2o.ai/solutions/use-case/credit-risk-scoring/", "credit risk scoring"),
        A("https://github.com/h2oai/h2o-3", "H2O-3 on GitHub"),
        A("https://aws.amazon.com/marketplace/pp/prodview-bx2r2kp7qw6m4", "Driverless AI on AWS Marketplace")]) +
        ". Vendor capabilities change; check their site for the latest. H2O.ai and Driverless AI are trademarks of their owner.",
),
dict(
    file="thorcast-vs-sas.html", name="SAS Viya", url="https://www.sas.com/en_us/software/viya.html",
    title="Thorcast.AI vs SAS Viya and SAS Risk Modeling (2026)",
    h1="Thorcast.AI vs SAS Viya",
    desc="An honest comparison of Thorcast.AI and SAS Viya / SAS Risk Modeling for credit risk and predictive models: agents, data, explainability, deployment and when to choose each.",
    intro="""<p><strong>SAS Viya</strong> is a unified data and AI platform, and <strong>SAS Risk Modeling</strong> (formerly SAS Credit Scoring) is its governed environment to develop, validate, deploy and monitor credit risk models. It is a long-standing standard in banking. <strong>Thorcast.AI</strong> is a predictive analytics platform where two AI agents take a model from raw data to a business decision, with alternative data built in.</p>
<p>SAS offers a full traditional credit-scorecard toolkit; Thorcast focuses on getting a production-grade model and a decision quickly, with less specialist effort.</p>""",
    rows=[
        ("What it is", "Predictive analytics platform with AI agents for credit, fraud, churn, cross-sell, pricing and geo use cases.", "Unified data and AI platform; Risk Modeling for credit risk model development and governance."),
        ("AI agents", T_AGENTS, "SAS Viya Copilot and other assistants, an agentic AI accelerator, and AI agents in SAS Intelligent Decisioning."),
        ("Data preparation", T_PREP, "Full data management and programming environment (SAS, Python, R) for your team."),
        ("AutoML", T_AUTOML, "Model Studio with automated pipeline generation and autotuning."),
        ("Credit-scorecard tooling", "Credit risk models with Gini, KS and ROC, cutoffs with economic impact, and Champion–Challenger.", "Interactive grouping, weight of evidence, monotonicity and stability checks, reject inference and automated documentation."),
        ("Built-in third-party data", T_ENRICH, "No native third-party data enrichment found on the Viya page; you bring your own data."),
        ("Explainability & documentation", T_EXPLAIN, "PD, ICE, LIME and Shapley explanations; central model repository with version control."),
        ("Deployment", T_DEPLOY, "Cloud, hybrid or on-premise; SAS Managed Cloud Services; dark-site (air-gapped) installs."),
        ("Getting started", T_START, "14-day free trial; pricing not published (several tiers, pay-as-you-go option)."),
        ("Best fit", T_FIT, "Banks with established SAS teams and processes that want maximum control over traditional scorecards."),
    ],
    choose="""<h2>When to choose SAS</h2>
<ul><li>Your risk team already works in SAS and your model governance is built around it.</li>
<li>You need the full traditional scorecard toolkit: interactive grouping, WoE, reject inference and the documentation your validators expect from SAS.</li>
<li>You want one vendor for data management, analytics and decisioning across the bank.</li></ul>
<h2>When to choose Thorcast.AI</h2>
<ul><li>You want a production-grade model in minutes instead of months, with agents doing the data preparation and modeling.</li>
<li>Your team is small, or you want to cover more use cases (fraud, churn, cross-sell, pricing) with the same people.</li>
<li>You want alternative data from an address, email or phone included, and the model to end in a decision with economic impact.</li></ul>""",
    sources="Sources (SAS, checked November 2026): " + " · ".join([
        A("https://www.sas.com/en_us/software/viya.html", "SAS Viya"),
        A("https://www.sas.com/en_ca/software/risk-modeling.html", "SAS Risk Modeling"),
        A("https://www.sas.com/en_us/software/viya/try-or-buy.html", "try or buy"),
        A("https://www.sas.com/en_ca/software/model-studio/features-list.html", "Model Studio"),
        A("https://www.sas.com/en_gb/news/press-releases/2026/april/innovate-viya-ai-assistants-agentic.html", "Viya AI assistants (2026)")]) +
        ". Vendor capabilities change; check their site for the latest. SAS and Viya are trademarks of SAS Institute Inc.",
),
]
