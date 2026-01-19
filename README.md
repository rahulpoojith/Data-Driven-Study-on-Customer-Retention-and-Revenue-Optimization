# A Data-Driven Study on Customer Retention and Revenue Optimization

## 📌 Overview
This project presents an end-to-end analytical study focused on evaluating customer retention strategies using controlled experimentation. The objective is to assess whether a retention intervention leads to measurable improvements in customer retention and revenue, and to enable objective, data-driven business decisions.

The project emphasizes:
- KPI-first analytical thinking
- Correct metric definitions and data grain alignment
- Controlled experimentation (A/B testing)
- Statistical validation of outcomes
- Clear separation between analysis, aggregation, and reporting
- Business-oriented interpretation of results

---

## 🎯 Business Context
Customer retention is a critical driver of long-term profitability across industries. Retention initiatives—such as discounts, incentives, or loyalty offers—carry real financial costs and operational trade-offs.

Organizations therefore rely on controlled experiments (A/B testing) to validate whether such initiatives produce meaningful business impact before scaling.

---

## ❓ Problem Statement
**Does a retention intervention reduce customer churn and improve revenue compared to a control group?**

The goal of this analysis is to objectively evaluate impact—not to assume success—and to support clear business decisions.

---

## 🧪 Experiment Design & Hypotheses

### Experimental Design
- **Unit of randomization:** Customer  
- **Groups:**  
  - **Control (Group A):** No retention intervention  
  - **Treatment (Group B):** Retention intervention applied  
- **Observation window:** Fixed evaluation period  
- **Evaluation level:** Customer-level outcomes  

Randomization ensures the two groups are statistically comparable at baseline.

---

### Hypotheses Tested

#### Primary Hypothesis (Churn)
- **Null Hypothesis (H₀):**  
  The retention intervention does **not** reduce customer churn compared to the control group.

- **Alternative Hypothesis (H₁):**  
  The retention intervention **reduces** customer churn compared to the control group.

This is a **one-sided hypothesis**, aligned with the business objective of churn reduction.

---

#### Secondary Hypothesis (Revenue)
- **Null Hypothesis (H₀):**  
  There is **no difference** in average customer revenue between the treatment and control groups.

- **Alternative Hypothesis (H₁):**  
  The retention intervention leads to a **difference** in average customer revenue.

This is evaluated as a **two-sided hypothesis** due to natural revenue variability.

---

## 📊 Key Performance Indicators (KPIs)

### Primary KPIs
- Churn Rate
- Retention Rate
- ARPU (Average Revenue Per User)

### Secondary KPIs
- Revenue Lift
- Statistical Significance (p-value)
- Confidence Interval

All KPIs are evaluated at the **customer level**, matching the unit of experimentation.

---

## ✅ Final Results & Conclusion

### Churn Analysis
- The observed churn rates between the control and treatment groups were nearly identical.
- The statistical test produced a **high p-value**, indicating no evidence of churn reduction due to the intervention.

**Decision:**  
Fail to reject the null hypothesis for churn.  
There is no statistically significant evidence that the retention intervention reduced churn.

---

### Revenue Analysis
- Revenue differences between groups were small and inconsistent.
- Statistical testing did not indicate a meaningful or reliable revenue impact.

**Decision:**  
Fail to reject the null hypothesis for revenue.  
The intervention did not demonstrate a measurable revenue effect.

---

## 📌 Business Recommendation
Based on the experimental results:
- The tested retention intervention should **not** be scaled broadly.
- Future experiments should focus on:
  - Targeted offers for high-risk or high-value customers
  - More differentiated incentive designs
  - Longer observation windows where appropriate

---

## 🗂️ Project Structure
```
Data-Driven-Study-on-Customer-Retention-and-Revenue-Optimization/
├── Datasets/
├── sql/
├── python/
├── notebooks/
├── powerbi/
├── README.md
└── .gitignore
```

---

## 🧠 What This Project Demonstrates
- KPI-driven analytical design
- Correct handling of metric grain
- Proper application of A/B testing principles
- Statistical rigor in decision-making
- Clear translation of analytical results into business recommendations

---

## 📝 Notes
This project is intended as a methodological case study. The emphasis is on analytical rigor, statistical validity, and objective decision-making rather than producing a positive experimental outcome.
