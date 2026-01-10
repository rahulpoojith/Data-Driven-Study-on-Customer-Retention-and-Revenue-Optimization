# A Data-Driven Study on Customer Retention and Revenue Optimization

## 📌 Overview
This project presents an end-to-end analytical study focused on evaluating customer retention strategies using controlled experimentation. The objective is to determine whether a retention intervention leads to measurable improvements in customer retention and revenue, and to support data-driven business decision-making.

The project emphasizes:
- Correct KPI design and metric definitions
- Proper aggregation at the correct data grain
- Statistical validation using A/B testing
- Clear separation between analysis and reporting
- Business-oriented interpretation of results

---

## 🎯 Business Context
Customer retention is a critical driver of long-term profitability across industries. Retention initiatives—such as discounts, offers, or incentives—often incur real financial costs. Deploying such strategies without evidence can lead to revenue leakage and ineffective campaigns.

Organizations therefore rely on **controlled experiments (A/B testing)** to answer questions such as:
- Does a retention intervention reduce churn?
- Does it improve customer retention?
- Does it have a meaningful impact on revenue?
- Are observed differences statistically significant or due to randomness?

This project demonstrates how such questions can be answered systematically using data.

---

## ❓ Problem Statement
**Does a retention intervention result in a measurable improvement in customer retention and revenue compared to no intervention?**

The goal of this study is not to prove success, but to objectively evaluate impact and support a clear business decision.

---

## 📊 Key Performance Indicators (KPIs)

### Primary KPIs (Decision Drivers)
- **Churn Rate**
- **Retention Rate**
- **ARPU (Average Revenue Per User)**
- **Upgrade Conversion Rate**

### Secondary KPIs (Validation & Interpretation)
- **Revenue Lift**
- **Statistical Significance (p-value)**
- **Confidence Interval**

All KPIs are evaluated at the **customer level**, matching the unit of randomization.

---

## 🧠 Analytical Approach
1. Metric design and grain definition  
2. SQL-based aggregation  
3. Statistical validation using A/B testing  
4. Visualization and business interpretation  

---

## ✅ Key Findings (Summary)
- No statistically or practically significant difference was observed between the control and treatment groups.
- Revenue-related metrics showed minimal variation.
- A blanket retention intervention is not recommended.

---

## 📌 Business Recommendation
Focus future experimentation on targeted retention strategies for high-risk or high-value customer segments rather than blanket offers.

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

## 📝 Notes
This project is intended as a methodological case study emphasizing analytical rigor and decision-making.
