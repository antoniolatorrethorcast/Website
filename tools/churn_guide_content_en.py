"""English guide: how to predict customer churn in banking, insurance and telco (2026-11-24). Translation of churn_guide_content.py.
Example figures = the ones thorcast.ai already publishes in its use-case videos, with the same label
(illustrative / simulated / case). No client names or prices."""

FILE = "how-to-predict-customer-churn-banking-insurance-telco.html"
DATE = "2026-11-24"

TITLE = "How to predict customer churn in banking, insurance and telco — Thorcast.AI"
DESC = ("A guide to churn models for banking, insurance and telco: how to define churn, which data to use, how to measure "
        "against your contact capacity and how to turn the score into a profitable campaign.")
H1 = "How to predict customer churn in banking, insurance and telco: a practical 2026 guide"
TAG = "GUIDE"
META = "Thorcast.AI · Updated November 24, 2026 · 8 min read"
CRUMB = "How to predict customer churn in banking, insurance and telco"
ABOUT = "Customer churn prediction"

INTRO = (
    "<p>Most churn guides are written for subscription software companies. In banking, insurance and telecommunications the "
    "problem is different: customers rarely announce that they are leaving, churn is not always a formal cancellation and the "
    "retention team has a fixed capacity of calls, offers or visits. This guide is for analytics, risk, CRM and retention "
    "teams in those industries.</p>"
    "<p>The core idea: a churn model is not measured by how many departures it predicts, but by how much value it keeps with "
    "the contacts you can already make. The example figures in this guide come from the cases we show on video at "
    "thorcast.ai, with the same label they carry there (case, illustrative example or simulated).</p>"
)

DEF_H = "First, define what “leaving” means in your industry"
DEF_P = ("<p>The definition of the event (the <em>target</em>) shapes the result more than the algorithm. Write it down before "
         "looking at the data, with a clear horizon: “leaves within the next 60 or 90 days”, measured from the date you would make the contact.</p>")
DEFS = [
    ("Banking and retail finance",
     "There is rarely a formal closure: the customer stops using the card, moves their payroll or empties the account. Define churn as "
     "closure or as a sustained drop in activity or balance (for example, no transactions for 90 days), and separate voluntary churn "
     "from cancellation due to default, which belongs in a collections model."),
    ("Life and health insurance",
     "The event is the lapse or surrender of the policy. Timing matters: the first years of a policy concentrate a large share of "
     "lapses, so it pays to model persistency by policy age and not just “cancels yes or no”."),
    ("General insurance and brokers",
     "Churn happens mainly at renewal: the customer doesn't renew or switches to another insurer. The natural horizon is the weeks "
     "before expiry, when a call can still change the decision."),
    ("Telco",
     "In postpaid, the event is porting out or disconnection. In prepaid there is no disconnection: the customer stops topping up. "
     "Define churn by inactivity (for example, 30 days without a top-up or usage) and treat migration from postpaid to prepaid "
     "separately, since it is not always a loss."),
]

DATA_H = "Which data predicts churn"
DATA = [
    "<strong>Recent behavior.</strong> Changes more than levels: a drop in usage, balance, top-ups or transactions over the last few weeks says more than the yearly average.",
    "<strong>Relationship with the company.</strong> Tenure, products held, complaints, customer service calls, service failures and changes of plan or coverage.",
    "<strong>Price and terms.</strong> Rate or premium increases, the end of a promotional period, the expiry of a contract or a lock-in period.",
    "<strong>External context.</strong> The profile of the area where the customer lives, the quality of their email and phone and their digital footprint are signals your systems don't have, and they help most when your own history is short.",
    "<strong>Watch out for information leakage.</strong> Any variable recorded after the customer decided to leave (a porting request, a call to cancel) makes the model look perfect in the lab and fail in production.",
]

MEASURE_H = "Measure the model against your contact capacity"
MEASURE = (
    "<p>Accuracy is misleading: if 3% of customers leave, a model that says “nobody leaves” is 97% accurate. What matters is how "
    "many real churners you find within the capacity your team can contact. Rank the portfolio by score, take the top N (your "
    "capacity) and count how many of them actually left in the test sample, split by time.</p>"
    "<p>This is what the differences look like in the cases we publish:</p>"
)
CASES = [
    ("Mobile telco (case on video)", "With the same 200,000 contacts, Thorcast's model finds 132,000 of the customers who would leave, versus 102,000 for the current model. Gini rises from 0.44 to 0.60."),
    ("Life insurance (simulated example)", "In the riskiest 20%, the current model found 12.5 real cancellations per 100; Thorcast found 16.5 with internal data and 18.5 adding enriched data."),
    ("Insurance brokers (example)", "With the same capacity of 240,000 contacts, the current model finds 88,000 of the 160,000 policies that would leave; Thorcast finds 105,000."),
    ("Auto insurance, renewal (illustrative scenario)", "With the same capacity of 50,000 calls, 40% of the customers chosen by the current method would leave; of those chosen by Thorcast, 60%. That keeps about US$2.8 million more in premium per year."),
]

VALUE_H = "Not every customer is worth the same, and not every one can be retained"
VALUE = [
    "<strong>Prioritize by value, not just by risk.</strong> Combining the probability of churn with the customer's future value (CLTV) "
    "puts first those who would take the most value with them. In an illustrative banking example, with the same 30,000 contacts the "
    "offer retains 1,500 customers with Thorcast versus 900 with the current model: about US$270k of CLTV kept per year.",
    "<strong>Look for the customers the action actually changes.</strong> Some customers will leave whatever you do, and others would stay "
    "anyway. The best use of your capacity is to contact the ones a call or an offer can retain, and to predict which incentive works for each.",
    "<strong>Measure with a control group.</strong> Leave part of the high-risk customers uncontacted. Without that group you don't know how "
    "many stayed because of the campaign and how many would have stayed anyway.",
]

DEC_H = "From score to campaign: decision layers"
DEC = (
    "<p>A churn model only creates value if it changes who gets contacted. That is why the last piece is the decision rule: with a fixed "
    "capacity, how many contacts to make, to whom and with which offer, and how much value each alternative keeps.</p>"
    "<p>At Thorcast that is handled by <strong>decision layers</strong>. <strong>Thorcast Decision Layers</strong> come preconfigured in "
    "the app: you enter the economics of your campaign and see the impact at every cutoff. When the rule is specific to your operation "
    "(a fixed number of calls per branch, different offers by segment, contact costs by channel), <strong>Customized Decision Layers</strong> "
    "let you describe it to MJÖ in plain language so it builds a layer tailored to you, which you review and approve. The result is in the "
    "language of the business: how many customers you retain and how much value you keep.</p>"
)

MISTAKES_H = "Common mistakes"
MISTAKES = [
    "Training on a random split instead of a time-based one: the model looks better than it will perform.",
    "Defining churn with data that arrives late (the formal closure) when the customer had already left months earlier.",
    "Measuring with accuracy or Gini alone, without looking at how many churners fall within the contact capacity.",
    "Contacting every high-risk customer with the same offer, without looking at value or likelihood to respond.",
    "Launching the campaign without a control group and then being unable to prove the result.",
    "Not monitoring the model: changes in pricing, competition or customer mix degrade it within a few months.",
]

FIT_H = "How Thorcast does it"
FIT = [
    "<strong>NORA</strong> prepares the data: you tell it in plain language what you need (clean, join tables, build the target) and it proposes a plan you approve; every step goes through a deterministic validation engine.",
    "<strong>The Data Enrichment Network</strong> turns an email, a phone or an address into new signals: more than 3,000 data points, condensed into 261 model-ready signals.",
    "<strong>MJÖ</strong> builds and compares the models and presents the best one, with standard metrics and an audit-ready technical report.",
    "<strong>Decision layers</strong> turn the score into a campaign with economic impact, preconfigured or tailored to you.",
    "<strong>Deployment and monitoring</strong> in Thorcast Cloud, on your premises or in the app, with recalibration when the population changes.",
]

FAQ_H = "Frequently asked questions"
FAQ = [
    ("What is a churn model?",
     "It is a predictive model that estimates, for each customer, the probability of leaving within a defined horizon (for example, the next 90 days). It is used to rank the portfolio and decide whom to contact first with the retention actions available."),
    ("How far in advance can churn be predicted?",
     "It depends on the industry and the data, but the goal is to get there before the customer makes the decision: weeks ahead in telco and banking, and before expiry in general insurance. A horizon that is too short leaves little room to act; one that is too long loses precision."),
    ("Does it work for prepaid telco?",
     "Yes, but churn is defined by inactivity (no longer topping up or using the service) because there is no formal disconnection. Recent usage data and external signals are especially useful when the operator has little information about the customer."),
    ("What is a decision layer in a retention campaign?",
     "It is the rule that turns the score into whom to contact, with which offer and with what economic impact. In Thorcast you can use preconfigured layers (Thorcast Decision Layers) or ask MJÖ for one tailored to your operation (Customized Decision Layers)."),
]

MORE_H = "Keep reading"
MORE = [
    ("customer-churn-prediction-model.html", "Customer churn model with AI (with videos by industry)"),
    ("how-to-choose-credit-scoring-software.html", "How to choose credit scoring software: a practical guide"),
    ("faq.html#gini-uplift", "Alternative data results by country"),
    ("who-is-it-for.html", "Who Thorcast.AI is for"),
    ("tutorials.html", "Video tutorials"),
]
