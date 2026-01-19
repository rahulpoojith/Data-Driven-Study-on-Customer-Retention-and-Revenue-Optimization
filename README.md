# A Data-Driven Study on Customer Retention and Revenue Optimization

## 📌 Overview
This project presents an end-to-end analytical study focused on evaluating customer retention strategies using controlled experimentation. The objective is to determine whether a specific retention intervention leads to measurable improvements in customer retention and to support objective, data-driven business decision-making.

The project emphasizes:
- Correct KPI design and metric definitions
- Proper aggregation at the correct data grain
- Statistical validation using A/B testing
- Clear separation between analysis and reporting
- Business-oriented interpretation of results

---

## 🎯 Business Context
Customer retention is a critical driver of long-term profitability across industries. Retention initiatives—such as discounts, offers, or incentives—often incur real financial costs. Deploying such strategies without empirical evidence can lead to revenue leakage and ineffective campaigns.

Organizations therefore rely on **controlled experiments (A/B testing)** to evaluate whether commonly used retention offers actually reduce churn before scaling them broadly.

---

## ❓ Problem Statement
**Does offering a 10% monthly bill discount reduce customer churn compared to no retention offer?**

The goal of this study is not to prove success, but to objectively evaluate whether this specific intervention delivers measurable impact and to support a clear business decision.

---

## 🧪 Experiment Design & Hypothesis

### Retention Intervention Tested
- **Intervention:** 10% monthly bill discount  
- **Duration:** Three billing cycles (one quarter)  
- **Control Group:** No retention offer  

---

### Hypothesis Tested (Single Hypothesis)

- **Null Hypothesis (H₀):**  
  Offering a 10% monthly bill discount does **not** reduce customer churn compared to the control group.

- **Alternative Hypothesis (H₁):**  
  Offering a 10% monthly bill discount **reduces** customer churn compared to the control group.

This is a **one-sided hypothesis**, aligned with the business objective of churn reduction.

---

## 📊 Key Performance Indicator (KPI)

### Primary KPI
- **Churn Rate**  
  Defined as the proportion of customers who churned during the observation period.

All metrics are evaluated at the **customer level**, matching the unit of randomization and ensuring valid statistical inference.

---

## 🧠 Analytical Approach
1. KPI definition and data-grain validation  
2. SQL-based aggregation and metric computation  
3. Statistical validation using A/B testing  
4. Business-oriented interpretation of results  

---

## ✅ Key Findings
- No statistically or practically significant difference in churn was observed between the control and treatment groups.
- The observed variation in churn rates is consistent with random noise rather than a true intervention effect.

---

## 📌 Business Recommendation
Based on the experimental results:
- A blanket **10% bill discount** should **not** be scaled as a general retention strategy.
- Future experimentation should focus on:
  - Targeted retention offers for high-risk or high-value customers
  - More differentiated incentive designs
  - Longer or staged evaluation windows where appropriate

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
- KPI-first analytical thinking
- Correct handling of metric grain
- Proper application of A/B testing principles
- Statistical rigor in hypothesis testing
- Clear translation of analytical results into business decisions

---

## 📝 Notes
This project is intended as a methodological case study. The emphasis is on analytical rigor, statistical validity, and objective decision-making rather than producing a positive experimental outcome.
