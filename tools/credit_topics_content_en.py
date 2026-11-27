"""English guides on two credit-risk searches (2026-11-26): credit cutoff optimization and reject inference analysis.
Worked examples use round, clearly labeled illustrative numbers (no client data). Thorcast facts = what thorcast.ai
already publishes (blog-12 for reject inference, the decision-layer text of the credit scoring guide). No prices."""

DATE = "2026-11-26"

CUTOFF = dict(
    FILE="credit-cutoff-optimization.html",
    TITLE="Credit Cutoff Optimization: Set the Optimal Score Cutoff (Calculator)",
    DESC=("Credit cutoff optimization step by step: the break-even PD formula, a worked example, a free cutoff calculator, "
          "cut-off rate vs bad rate, swap-set analysis and segment cutoffs."),
    H1="Credit cutoff optimization: how to set the score cutoff that maximizes profit",
    TAG="GUIDE",
    META="Thorcast.AI · Updated November 27, 2026 · 10 min read",
    MODIFIED="2026-11-27",
    DEF=("<strong>Credit cutoff optimization</strong> is choosing the score threshold that separates approved from declined "
         "applicants so that expected profit is as high as possible within the lender's risk appetite. The core rule: approve an "
         "applicant when their calibrated probability of default is below the <strong>break-even PD = margin ÷ (margin + loss)</strong>. "
         "<a href=\"#calculator\">Try the calculator</a>."),
    CRUMB="Credit cutoff optimization",
    ABOUT="Credit score cutoff optimization",
    SECTIONS=[
        (None,
         "<p>A credit model ranks applicants by risk. The <strong>cutoff</strong> turns that ranking into a decision: approve "
         "everyone above it, decline everyone below. It is the single number in the credit process that moves the most money, "
         "and it is often the one chosen with the least analysis. This guide explains how to set it with numbers, step by step, "
         "for risk, credit policy and finance teams in banks, lenders, fintechs and retail finance companies.</p>"
         "<p>The figures in the examples are <strong>illustrative</strong>: round numbers chosen to show the method, not data "
         "from any portfolio.</p>"),
        ("What the cutoff decides",
         "<p>Moving the cutoff trades two errors against each other. Set it higher and you approve fewer applicants and lose "
         "fewer loans to default, but you also turn away customers who would have paid. Set it lower and you capture more revenue "
         "at the price of more losses. The two numbers people usually look at are:</p><ul>"
         "<li><strong>Cut-off rate (approval rate):</strong> the share of applicants that score above the cutoff. A cut-off rate "
         "of 60% means six out of ten applicants are approved. Some teams use “cut-off rate” for the rejected share instead; "
         "say which one you mean in every report.</li>"
         "<li><strong>Bad rate of the approved:</strong> the share of approved loans expected to default within the outcome "
         "window (for example, 90 days past due within 12 months).</li></ul>"
         "<p>Neither number tells you where to stop. Profit does.</p>"),
        ("Step 1: the break-even probability of default",
         "<p>For a single applicant, approving makes sense when the expected gain is larger than the expected loss:</p>"
         "<p><strong>Expected profit = (1 − PD) × margin − PD × loss</strong></p>"
         "<p>where <em>PD</em> is the probability of default the model gives that applicant, <em>margin</em> is what you earn "
         "on a loan that is repaid (interest and fees net of funding and operating cost) and <em>loss</em> is what you lose on "
         "one that defaults (exposure × loss given default, net of recoveries). Setting the expected profit to zero gives the "
         "<strong>break-even PD</strong>:</p>"
         "<p><strong>Break-even PD = margin ÷ (margin + loss)</strong></p>"
         "<p>Illustrative example: a loan of 1,000 earns a margin of 150 if repaid and loses 650 if it defaults. The break-even "
         "PD is 150 ÷ 800 = 18.75%. Every applicant with a PD below 18.75% adds expected profit; every applicant above it "
         "destroys it. The optimal cutoff is the score where the PD crosses that line, provided the model is calibrated.</p>"),
        ("Step 2: a worked example",
         "<p>Take 10,000 applicants split into five risk bands of 2,000 each, with the same economics as above "
         "(illustrative numbers):</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Approve bands</th><th>Cut-off rate</th>"
         "<th>Bad rate of approved</th><th>Expected profit</th></tr></thead><tbody>"
         "<tr><td>A only (PD 2%)</td><td>20%</td><td>2.0%</td><td>268,000</td></tr>"
         "<tr><td>A–B (PD up to 5%)</td><td>40%</td><td>3.5%</td><td>488,000</td></tr>"
         "<tr><td>A–C (PD up to 10%)</td><td>60%</td><td>5.7%</td><td>628,000</td></tr>"
         "<tr><td>A–D (PD up to 18%)</td><td>80%</td><td>8.8%</td><td><strong>640,000</strong></td></tr>"
         "<tr><td>All (PD up to 32%)</td><td>100%</td><td>13.4%</td><td>428,000</td></tr>"
         "</tbody></table></div>"
         "<p>Profit peaks when approving bands A to D. Band D adds very little (12,000 across 2,000 loans) because its PD of "
         "18% sits just below the break-even of 18.75%; band E, at 32%, loses 212,000. Two lessons follow:</p><ul>"
         "<li>The bands near the break-even point decide almost nothing in profit but a lot in volume and risk. That is where "
         "risk appetite, capital and strategy come in.</li>"
         "<li>The optimum is fragile. If the loss on a default rises from 650 to 700, the break-even PD falls to 17.6% and band "
         "D turns negative: the best cutoff moves up to A–C. The cutoff has to follow the economics, not the other way round.</li></ul>"),
        ("Step 3: check the constraints",
         "<p>The profit-maximizing cutoff is the starting point, not the final answer. Before setting it, check:</p><ul>"
         "<li><strong>Risk appetite:</strong> a maximum bad rate or expected loss the board has approved.</li>"
         "<li><strong>Capital and funding:</strong> how much volume the balance sheet can take.</li>"
         "<li><strong>Volume targets:</strong> growth goals may justify approving a marginal band on purpose, with its cost made explicit.</li>"
         "<li><strong>Regulation and fairness:</strong> rules on affordability, responsible lending and explainable declines.</li>"
         "<li><strong>Calibration:</strong> the break-even logic only works if a predicted PD of 10% really means about 10 defaults "
         "in 100. Check calibration on recent, out-of-time data.</li></ul>"),
        ("Step 4: swap-set analysis when you change the model",
         "<p>When a new model replaces the current one, compare the two policies applicant by applicant, at the same "
         "cut-off rate:</p><ul>"
         "<li><strong>Swap-ins:</strong> applicants the new model approves and the old one declined.</li>"
         "<li><strong>Swap-outs:</strong> applicants the old model approved and the new one declines.</li></ul>"
         "<p>The new model is better if the swap-ins are less risky than the swap-outs. The catch: you only observe outcomes "
         "for the swap-outs, because the swap-ins were declined in the past. Their performance has to be estimated, which is "
         "exactly the job of <a href=\"reject-inference-analysis.html\">reject inference</a>, or measured with a small "
         "controlled test below the old cutoff.</p>"),
        ("Step 5: one cutoff or several",
         "<p>A single cutoff assumes every applicant has the same economics. Often they don't: margins, loan sizes and recoveries "
         "differ by product, channel and segment. Setting a cutoff per segment, each from its own break-even PD, usually adds "
         "profit at the same overall risk. Keep the number of segments small enough to explain and to monitor, and document why "
         "each one exists.</p>"),
        ("Step 6: review it on a schedule",
         "<p>A cutoff that was optimal six months ago may not be today. Review it when funding costs, prices, loss severity, "
         "the applicant mix or the macroeconomic outlook change, and at least every quarter. Monitor the approval rate, the "
         "early-default rate of recent vintages and the calibration of the score: a drift in any of them is a signal to "
         "recompute the cutoff.</p>"),
        ("Common mistakes",
         "<ul><li>Choosing the cutoff by approval rate (“we approve 60%”) with no link to economics.</li>"
         "<li>Using an uncalibrated score as if it were a probability.</li>"
         "<li>Measuring the new policy only on applicants the old policy approved.</li>"
         "<li>Keeping the same cutoff after prices or funding costs change.</li>"
         "<li>Setting the cutoff in a spreadsheet nobody can audit later.</li></ul>"),
        ("How Thorcast handles it",
         "<p>In Thorcast the step from score to decision is done with <strong>decision layers</strong>. The preconfigured "
         "<strong>Thorcast Decision Layers</strong> include the origination cutoff: you enter the economics of your policy, "
         "such as what you earn on a loan that is repaid and what you lose on one that defaults, and see approval, risk and "
         "profit at every cutoff, side by side. When the decision doesn't fit a standard layer, for example different rules "
         "by segment, you describe it to MJÖ in plain language and the agent builds a <strong>Customized Decision Layer</strong> "
         "for you to review and approve.</p>"
         "<p>The cutoff is then recalculated from the same inputs whenever the economics change, and the inputs and results "
         "stay documented for the risk committee and the validator.</p>"),
    ],
    FAQ=[
        ("What is credit cutoff optimization?",
         "It is the process of choosing the credit score threshold that maximizes expected profit within the lender's risk "
         "appetite, capital and regulatory constraints. It starts from the break-even probability of default, margin ÷ "
         "(margin + loss), and is checked with a profit table by score band."),
        ("What is a credit score cutoff?",
         "It is the score threshold that separates the applicants a lender approves from the ones it declines. Applicants "
         "scoring above the cutoff are approved, or sent to the next step of the process; the rest are declined."),
        ("What is the cut-off rate?",
         "Usually, the approval rate at a given cutoff: the share of applicants who score above it. Some teams use it for the "
         "share that is rejected, so always state the definition next to the number."),
        ("How do you calculate the optimal cutoff?",
         "Compute the break-even probability of default, margin ÷ (margin + loss), and approve the applicants whose calibrated "
         "PD is below it. Then adjust for risk appetite, capital, volume targets and regulation, and check the result with a "
         "profit table by score band."),
        ("How often should the cutoff be reviewed?",
         "Whenever the economics change (prices, funding cost, loss severity) or the applicant mix shifts, and at least "
         "quarterly. Track approval rate, early defaults and calibration to know when to recompute it."),
        ("What is the relationship between the cutoff and reject inference?",
         "Lowering the cutoff means approving applicants your past policy declined, whose outcomes you never observed. Reject "
         "inference estimates how they would have performed, so the new cutoff is not set on a biased sample."),
    ],
    MORE=[
        ("reject-inference-analysis.html", "Reject inference analysis: a step-by-step guide"),
        ("blog-03.html", "Beyond the score: why the cutoff decision is where the money is"),
        ("blog-12.html", "Reject inference in credit scoring: methods and pitfalls"),
        ("how-to-choose-credit-scoring-software.html", "How to choose credit scoring software"),
        ("ai-credit-scoring.html", "AI credit scoring with alternative data"),
        ("tutorials.html", "Video tutorials"),
    ],
)

REJECT = dict(
    FILE="reject-inference-analysis.html",
    TITLE="Reject inference analysis: step-by-step guide with example — Thorcast.AI",
    DESC=("How to run a reject inference analysis in credit scoring: data you need, a worked parcelling example, how to "
          "choose the method, how to validate the result and what to document for model validation."),
    H1="Reject inference analysis: a step-by-step guide with a worked example",
    TAG="GUIDE",
    META="Thorcast.AI · Updated November 26, 2026 · 9 min read",
    CRUMB="Reject inference analysis",
    ABOUT="Reject inference in credit scoring",
    SECTIONS=[
        (None,
         "<p>An application scorecard learns from the loans you granted, but it is used on everyone who applies. "
         "<strong>Reject inference</strong> estimates how the declined applicants would have performed, so the new model is "
         "not trained only on the people your old policy let through. Our article on "
         "<a href=\"blog-12.html\">reject inference methods and pitfalls</a> explains why the problem exists and the main "
         "techniques. This guide is the practical part: how to run the analysis, step by step, with a worked example.</p>"
         "<p>The numbers in the example are <strong>illustrative</strong>, chosen to show the method.</p>"),
        ("Step 1: assemble the through-the-door sample",
         "<p>You need every application in the period, not just the loans:</p><ul>"
         "<li>An application identifier and date.</li>"
         "<li>The <strong>decision</strong>: approved or declined. Treat applicants who were approved but did not take the "
         "loan separately; they are neither good nor bad.</li>"
         "<li>The <strong>outcome</strong> for the approved ones, with a fixed definition and window (for example, 90 days past "
         "due within 12 months).</li>"
         "<li>The same predictor variables for approved and declined applicants, captured at application time.</li></ul>"
         "<p>If the declined applicants lack the variables, or were filtered out of the data warehouse, reject inference is not "
         "possible. Fixing that data gap is the first deliverable.</p>"),
        ("Step 2: build the preliminary score",
         "<p>Train a model on the approved applicants only (the “known good/bad” model), or use an existing score you trust. "
         "Its job is to rank the declined applicants by risk. Check that it ranks well on an out-of-time sample of approved "
         "applicants before using it to infer anything.</p>"),
        ("Step 3: infer the outcomes (worked parcelling example)",
         "<p>Score everyone, approved and declined, and group them into risk bands. For each band, take the observed bad rate "
         "of the approved applicants and assign the declined ones a higher bad rate, because within the same band they are "
         "usually riskier. Here the inflation factor is 1.5:</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Band</th><th>Approved</th>"
         "<th>Observed bad rate</th><th>Declined</th><th>Inferred bad rate (×1.5)</th><th>Inferred bads</th></tr></thead><tbody>"
         "<tr><td>1 (lowest risk)</td><td>4,000</td><td>2%</td><td>200</td><td>3%</td><td>6</td></tr>"
         "<tr><td>2</td><td>3,000</td><td>4%</td><td>400</td><td>6%</td><td>24</td></tr>"
         "<tr><td>3</td><td>2,000</td><td>7%</td><td>800</td><td>10.5%</td><td>84</td></tr>"
         "<tr><td>4</td><td>800</td><td>12%</td><td>1,200</td><td>18%</td><td>216</td></tr>"
         "<tr><td>5 (highest risk)</td><td>200</td><td>20%</td><td>1,400</td><td>30%</td><td>420</td></tr>"
         "<tr><td>Total</td><td>10,000</td><td>4.8%</td><td>4,000</td><td>18.8%</td><td>750</td></tr>"
         "</tbody></table></div>"
         "<p>In <em>parcelling</em>, 750 of the 4,000 declined applicants are labeled bad, at random within each band in those "
         "proportions, and the rest good. In <em>fuzzy augmentation</em>, every declined applicant enters twice, once as good "
         "and once as bad, weighted by the inferred probabilities. Either way, the training sample grows from 10,000 to 14,000 "
         "records and its bad rate rises from 4.8% to 8.8%, closer to the population the model will actually score.</p>"),
        ("Step 4: choose the method",
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Situation</th><th>Reasonable choice</th></tr></thead><tbody>"
         "<tr><td>Few declines, or the old policy was close to random in the region you care about</td><td>Train on approved only and document why</td></tr>"
         "<tr><td>A preliminary score you trust and enough applicants per band</td><td>Parcelling</td></tr>"
         "<tr><td>You want to carry the uncertainty instead of forcing hard labels</td><td>Fuzzy augmentation</td></tr>"
         "<tr><td>Bureau outcomes of declined applicants who got credit elsewhere</td><td>Use those real outcomes first, infer only the rest</td></tr>"
         "<tr><td>Room for a small controlled test below the cutoff</td><td>Run it: observed outcomes beat any inference</td></tr>"
         "</tbody></table></div>"),
        ("Step 5: set the parameters with care",
         "<ul><li><strong>Bands:</strong> quantile bands keep their sizes even; equal-width bands follow the score scale. Set a "
         "minimum number of records per band.</li>"
         "<li><strong>Inflation factor:</strong> justify it with what the business knows about declined applicants, or with "
         "bureau data. Test a range, not a single value.</li>"
         "<li><strong>Weight of the declined population:</strong> it controls how much the inference moves the final model.</li>"
         "<li><strong>Calibration and caps:</strong> calibrate the preliminary probabilities (Platt scaling or isotonic "
         "regression) and cap extreme values so they don't dominate.</li></ul>"),
        ("Step 6: validate the result",
         "<p>Reject inference cannot be validated on the inferred records themselves. These checks are what an analyst or "
         "validator should see:</p><ul>"
         "<li><strong>Test on real outcomes only.</strong> Inferred records go into training, never into the test set or a "
         "cross-validation test fold.</li>"
         "<li><strong>Compare with the approved-only model</strong> on the same out-of-time test sample: performance should "
         "not fall, and the ranking of the approved population should stay stable.</li>"
         "<li><strong>Sanity-check the inferred bad rate:</strong> above the approved bad rate in every band, rising with risk, "
         "and consistent with any bureau evidence.</li>"
         "<li><strong>Sensitivity:</strong> rerun with other inflation factors and weights. If the final model changes a lot, "
         "the inference is driving the result and needs a stronger justification.</li>"
         "<li><strong>Swap-set review:</strong> look at who the new model would approve that the old one declined, at the same "
         "approval rate. That is where the inference matters, and where the "
         "<a href=\"credit-cutoff-optimization.html\">cutoff decision</a> is made.</li></ul>"),
        ("Step 7: document the decision",
         "<p>Model validation will ask why the model approves profiles the old policy declined. Write down the declined population "
         "used, the preliminary score, the method and its parameters, the inferred bad rate per band, the comparison with the "
         "approved-only model and the reasons for the final choice, including the choice not to use reject inference.</p>"),
        ("How Thorcast handles it",
         "<p>In Thorcast, reject inference is an optional step between data preparation and modeling. It appears when the target "
         "is binary and a declined population has been declared, with an approval status column. It supports parcelling and "
         "fuzzy augmentation, with the preliminary score generated automatically or taken from an existing score, and settings "
         "for bands, banding method, minimum records per band, weight of the declined population, probability caps and "
         "calibration.</p>"
         "<p>Before anything changes, a preview compares the approved-only dataset with the augmented one: records, observed "
         "bads, inferred bads, bad rates and a summary per band, with warnings. You decide whether to use it. Inferred rows are "
         "used for training only, so every reported metric is computed on real outcomes.</p>"),
    ],
    FAQ=[
        ("What is reject inference analysis?",
         "It is the process of estimating how declined credit applicants would have performed and adding them to the training "
         "data, to correct the selection bias of a sample made only of approved loans."),
        ("Which reject inference method is best?",
         "There is no universal winner. Parcelling and fuzzy augmentation are the most used because they are explainable. "
         "Real outcomes, from bureau data or a controlled test, beat any inference when you can get them."),
        ("Does reject inference always improve the model?",
         "No. It replaces missing outcomes with assumptions, and the academic evidence on its gains is mixed. Use it as a "
         "documented, tested decision and compare it with the approved-only model on real outcomes."),
        ("What does “rejected by scoring” mean?",
         "It means an application was declined because its credit score fell below the lender's cutoff. The score estimates the "
         "risk of not repaying from the applicant's data; each lender sets its own cutoff, so the same person can be declined "
         "by one lender and approved by another."),
        ("Can inferred records be used to measure the model?",
         "No. They belong in training only. Measuring a model on inferred outcomes grades it on its own assumptions."),
    ],
    MORE=[
        ("blog-12.html", "Reject inference in credit scoring: methods and pitfalls"),
        ("credit-cutoff-optimization.html", "Credit cutoff optimization: how to set the score cutoff"),
        ("how-to-choose-credit-scoring-software.html", "How to choose credit scoring software"),
        ("ai-credit-scoring.html", "AI credit scoring with alternative data"),
        ("blog-07.html", "Explainable AI for credit scoring: what regulators ask"),
        ("tutorials.html", "Video tutorials"),
    ],
)
