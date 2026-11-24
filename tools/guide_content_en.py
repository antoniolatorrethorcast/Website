"""English guide: how to choose credit scoring software (2026-11-24). Translation of guide_content.py.
Third-party facts = the ones verified for the comparison pages (tools/compare_content.py, 2026-11-23).
Thorcast facts = what thorcast.ai already publishes. No prices here."""

FILE = "how-to-choose-credit-scoring-software.html"
DATE = "2026-11-24"

TITLE = "How to choose credit scoring software: 2026 guide — Thorcast.AI"
DESC = ("A practical guide to choosing credit scoring software: the five types of tools, ten evaluation criteria, "
        "how to run a fair proof of concept and the red flags to watch for.")
H1 = "How to choose credit scoring software: a practical 2026 guide"
TAG = "GUIDE"
META = "Thorcast.AI · Updated November 24, 2026 · 10 min read"
CRUMB = "How to choose credit scoring software"
LABELS = ("Strength:", "Limit:", "A good fit if", ("Criterion", "What to ask", "Red flag"))
ABOUT = "Credit scoring software"

INTRO = (
    "<p>Choosing a credit scoring tool is a decision that lasts for years: it sets how fast you can launch a new model, "
    "how much risk you accept with every approval and how easily you can explain each decision to your regulator. "
    "This guide is for risk, analytics and credit teams at banks, lenders, fintechs, retail finance companies, insurers "
    "and telcos who are comparing options.</p>"
    "<p><strong>Transparency:</strong> this guide is written by Thorcast.AI, which is one of the vendors. That is why we "
    "say where Thorcast fits and where another tool is a better choice. Facts about other vendors come from their own "
    "websites and documentation, reviewed in November 2026, and we link the sources in our comparison pages.</p>"
)

BEFORE_H = "Before you look at vendors: define the problem"
BEFORE = [
    ("Which decision you want to improve", "Origination, behavior (credit line increases, renewals), collections or application fraud. Each has different data, horizons and metrics; a tool that is good for one is not always good for another."),
    ("Where you are starting from", "A bureau score, your own scorecard, manual rules or nothing. What you have today is the model you will compare everything new against."),
    ("Who will run the tool", "An experienced data science team, risk analysts who don't code, or a mix. This is the question that rules out the most options."),
    ("Where the data must live", "The vendor's cloud, your cloud or your own servers. If your policies don't allow data to leave, rule those options out from the start."),
    ("What your regulator requires", "Development and validation documentation, an explanation for every decline, periodic monitoring. Ask for real examples of those deliverables, not just the promise."),
]

TYPES_H = "The five types of tools"
TYPES_P = "<p>Almost everything you will find falls into one of these five families. Each has its place; the most common mistake is comparing tools from different families as if they solved the same problem.</p>"
TYPES = [
    ("1. In-house development in Python or R",
     "Your team builds with open-source libraries (for example scikit-learn, LightGBM, XGBoost or OptBinning for scorecards).",
     "Full control and zero license cost.",
     "Everything depends on people: data preparation, documentation, deployment and monitoring have to be built and maintained. Timelines are measured in months.",
     "you have a strong, stable data science team and time to build the platform around the models."),
    ("2. Traditional statistical suites",
     "The best-known example is SAS (Viya and Risk Modeling), with interactive grouping, weight of evidence, reject inference and automated documentation.",
     "The standard many validators and regulators are familiar with; maximum control over the classic scorecard.",
     "Requires a team trained in the tool; the full cycle of a new model usually takes weeks or months.",
     'your model governance is already built on that suite. See <a href="thorcast-vs-sas.html">Thorcast.AI vs SAS Viya</a>.'),
    ("3. AutoML and enterprise machine learning platforms",
     "For example DataRobot and H2O.ai: they train and compare many algorithms, explain predictions and deploy models for many use cases.",
     "A lot of modeling power and governance for data science teams running several AI projects.",
     "They are designed mainly for data scientists, and we found no built-in third-party data in their documentation: you bring the data.",
     'you have an experienced data science team and existing data pipelines. See <a href="thorcast-vs-datarobot.html">vs DataRobot</a> and <a href="thorcast-vs-h2o.html">vs H2O.ai</a>.'),
    ("4. Bureau scores and origination decision engines",
     "Generic bureau scores and rules engines to run the credit policy in real time.",
     "Fast to get started, with bureau data included.",
     "A generic score doesn't learn from your portfolio or your customers; customizing it is usually a separate project.",
     "you need to start deciding now, with little history of your own, or you already have the model and need an engine to run it."),
    ("5. Predictive analytics platforms with AI agents and built-in data",
     "The newest category, where Thorcast.AI sits: AI agents prepare the data and build the models from plain-language instructions, with built-in alternative data and decision layers that show the economic impact.",
     "From raw data to a model in production in hours, without needing a large data science team.",
     "They are newer than the traditional suites; ask to see the technical reports and test with your own data before deciding.",
     'you want your own production-grade models, to add alternative data and to cover more use cases with the same team. See <a href="who-is-it-for.html">who Thorcast.AI is for</a>.'),
]

CRIT_H = "Ten criteria to evaluate, and what to ask each vendor"
CRIT = [
    ("Out-of-sample performance", "What Gini and KS does it get on a time-based split (vintages after the training period), not just on a random sample?",
     "They only show training results or a random split."),
    ("Alternative data", "What data can it add beyond mine, with what coverage in my country and on what legal basis?",
     "They talk about “thousands of variables” without stating the coverage in your country."),
    ("Explainability", "How do I explain an individual decline? What does it deliver for model validation?",
     "There is no sample technical report you can see before buying."),
    ("Reproducibility", "If I train twice on the same data, do I get the same model? Is the code or plan versioned?",
     "Results that change between runs with no explanation."),
    ("From score to decision", "Can I see approval, risk and profit at every cutoff?",
     "They deliver a score, and the policy is “up to you” in a separate spreadsheet."),
    ("Data preparation", "Who joins and cleans the source tables, and how long does it take?",
     "The demo always starts from a clean dataset, never from your real tables."),
    ("Deployment and where data lives", "Vendor cloud, your cloud or your servers? Can scoring run on my infrastructure?",
     "A single deployment option that doesn't meet your policies."),
    ("Monitoring and recalibration", "How do I detect that the model has degraded, and what does recalibrating it cost?",
     "Monitoring is a separate module or an integration project."),
    ("Who runs it", "Can a risk analyst who doesn't code build and maintain a model?",
     "Every change needs a data scientist or the vendor."),
    ("Total cost", "Licenses, data, integration, infrastructure and your team's hours over three years.",
     "They only quote the license, and data is charged separately, provider by provider."),
]

POC_H = "How to run a fair proof of concept"
POC = [
    "<strong>Use your own sample.</strong> With an identifier, the real outcome (for example, 90 days past due) and your current score. If you include email, phone and address, you can also measure what alternative data adds.",
    "<strong>Split by time, not at random.</strong> Train on the older applications and measure on the most recent ones. That is the closest thing to how the model will work in production.",
    "<strong>Compare against what you have today.</strong> The challenger has to beat your current score on the same test sample (Champion–Challenger), not a baseline model chosen by the vendor.",
    "<strong>Check the variables.</strong> Any variable that is only known after the loan is granted (payments, collections, account status) is information leakage and inflates the result.",
    "<strong>Measure in money.</strong> Beyond the Gini, ask for the approval rate and expected default at the cutoff you would use, and what that means in profit.",
    "<strong>Ask for the deliverables.</strong> The technical report, the reproducible code or plan and how it would be deployed. If it doesn't pass internal validation, the best Gini is worthless.",
]

DEC_H = "From score to decision: decision layers"
DEC = (
    "<p>A score, however good, doesn't decide anything on its own. The business question is different: whom do I approve, "
    "how much default do I accept and how much do I gain or lose with that policy. Ask each vendor to show you that bridge "
    "between statistics and decisions, with your numbers, not just a Gini.</p>"
    "<p>At Thorcast that bridge is the <strong>decision layers</strong>: they take the predictive statistics the platform "
    "produces and turn them into concrete business decisions, with their economic impact calculated. There are two ways to use them:</p>"
    "<ul>"
    "<li><strong>Thorcast Decision Layers.</strong> Layers preconfigured in the app for the most common decisions, such as "
    "the origination cutoff. You enter the economics of your policy (for example, what you earn on a loan that is repaid "
    "and what you lose on one that defaults) and see approval, risk and profit at every cutoff, side by side.</li>"
    "<li><strong>Customized Decision Layers.</strong> When your decision doesn't fit a standard layer (a fixed number of "
    "contacts, different rules by segment or costs specific to your operation), you describe the rule to MJÖ in plain "
    "language and the agent builds a layer tailored to you. You review and approve it before using it.</li>"
    "</ul>"
    "<p>The result is in the language of the business: how many applications you approve, how much default you expect and "
    "how much profit each alternative generates. The decision no longer depends on interpreting statistical metrics, and "
    "whoever decides can compare scenarios and choose for themselves.</p>"
)

FLAGS_H = "Red flags"
FLAGS = [
    "A Gini far above what is usual for your portfolio: more often it is information leakage than an extraordinary model.",
    "Results with no time-based split and no comparison against your current model.",
    "Alternative data with no documented coverage in your country.",
    "A black box with no per-application explanation and no documentation for the validator.",
    "“Top 10” rankings with no methodology: some sites charge for placement and don't mark which products paid. Use them as a starting list, never as an evaluation.",
]

FIT_H = "Where Thorcast.AI fits, and where it doesn't"
FIT_P = "<p>Thorcast.AI is a predictive analytics platform with AI agents. For credit scoring, this is what it brings:</p>"
NOT_FIT = [
    "Your model governance is built on SAS and your validators expect its deliverables: there, SAS is the most natural choice.",
    "Your data science team wants a platform to build and govern many kinds of AI and their own agents: look at DataRobot or H2O.ai.",
    "You only need a generic score and a rules engine to start deciding tomorrow, without building a model of your own.",
]
NOT_FIT_P = "<p>It may not be the best option if:</p>"

FAQ_H = "Frequently asked questions"
FAQ = [
    ("What is credit scoring software?",
     "It is the tool used to build, validate, deploy and monitor the model that estimates the probability that a customer won't pay. It ranges from open-source libraries to platforms that cover the whole cycle, from the data to the decision."),
    ("Machine learning or a traditional scorecard?",
     "It depends on what validation requires. Machine learning models usually discriminate better; a scorecard is easier to explain variable by variable. The practical approach is to try both on your data and choose with out-of-sample performance and explainability requirements on the table."),
    ("How much does alternative data improve a credit model?",
     "It depends on the country, the segment and the data you already have. In the experience of Thorcast's founding team, across 68 models in 12 countries, adding alternative data raised Gini by a median of 35%. The only way to know for your portfolio is to measure it in a proof of concept."),
    ("What is a decision layer?",
     "It is the part that turns a model's score into a business decision with economic impact: for each cutoff it shows how many applications are approved, how much default is expected and how much profit is left. In Thorcast you can use preconfigured layers (Thorcast Decision Layers) or ask MJÖ for a layer tailored to your business (Customized Decision Layers)."),
    ("How long does a proof of concept take?",
     "With traditional tools it is usually a project of several weeks. With Thorcast, a proof of concept on your own sample takes about an hour: the sample is enriched, a challenger model is trained and compared with your current score."),
]

MORE_H = "Keep reading"
MORE = [
    ("faq.html#gini-uplift", "Alternative data results by country"),
    ("blog-12.html", "Reject inference in credit scoring"),
    ("thorcast-vs-datarobot.html", "Thorcast.AI vs DataRobot"),
    ("thorcast-vs-h2o.html", "Thorcast.AI vs H2O.ai"),
    ("thorcast-vs-sas.html", "Thorcast.AI vs SAS Viya"),
    ("how-to-predict-customer-churn-banking-insurance-telco.html", "How to predict customer churn in banking, insurance and telco"),
    ("who-is-it-for.html", "Who Thorcast.AI is for"),
    ("tutorials.html", "Video tutorials"),
]
