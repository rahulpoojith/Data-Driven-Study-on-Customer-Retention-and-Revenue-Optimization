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

KPIs are designed hierarchically to reflect how business actions translate into outcomes.

### Primary KPIs (Decision Drivers)
- **Churn Rate**  
  Percentage of customers who exit during the analysis period.
- **Retention Rate**  
  Percentage of customers who remain active (derived from churn).
- **ARPU (Average Revenue Per User)**  
  Average revenue generated per active customer.
- **Upgrade Conversion Rate**  
  Percentage of customers who upgrade during the analysis period.

### Secondary KPIs (Validation & Interpretation)
- **Revenue Lift**
- **Statistical Significance (p-value)**
- **Confidence Interval**

All KPIs are evaluated at the **customer level**, matching the unit of randomization to ensure analytical and statistical correctness.

---

## 🧠 Analytical Approach

### 1️⃣ Metric Design & Data Grain
- Customer behavior is recorded at a **monthly level**
- KPIs are evaluated at a **customer level over a fixed analysis window**
- Terminal events such as churn are treated as binary outcomes per customer

This approach avoids double-counting and ensures consistent KPI interpretation.

---

### 2️⃣ Data Aggregation (SQL)
SQL is used to:
- Aggregate monthly activity into customer-level indicators
- Derive churn, retention, and revenue metrics
- Create reusable analytical views for downstream analysis and reporting

The SQL layer acts as the **single source of truth** for KPI computation.

---

### 3️⃣ Statistical Validation
A/B testing is used to compare outcomes between control and treatment groups.

Key principles applied:
- Customer-level aggregation before testing
- Appropriate statistical tests for binary outcomes
- Separation of effect size from statistical certainty

Statistical results are used to **validate decisions**, not to replace business judgment.

---

### 4️⃣ Visualization & Communication
Results are communicated using a focused reporting layer designed to answer:
1. Was the experiment valid?
2. Did key outcomes change?
3. What decision should be taken?

The emphasis is on clarity and decision-readiness rather than statistical complexity.

---

## ✅ Key Findings (Summary)
- No statistically or practically significant difference was observed between the control and treatment groups.
- Revenue-related metrics showed minimal variation across groups.
- The retention intervention did not justify a blanket rollout based on observed impact.

---

## 📌 Business Recommendation
Based on the experimental results:
- A broad retention intervention is **not recommended**
- Future experiments should focus on **targeted strategies** for high-risk or high-value customer segments
- Additional testing can explore alternative incentives or personalized offers

---

## 🗂️ Project Structure
Data-Driven-Study-on-Customer-Retention-and-Revenue-Optimization/
│
├── Datasets/              # Processed datasets used for analysis
├── sql/                   # SQL views and KPI aggregation logic
├── python/                # Data generation and statistical analysis scripts
├── notebooks/             # Exploratory and validation notebooks
├── powerbi/               # Reporting and dashboard artifacts
├── README.md
└── .gitignore



---

## 🧪 What This Project Demonstrates
- KPI-first analytical thinking
- Correct handling of metric grain
- Proper application of A/B testing principles
- Clean separation of analysis and reporting layers
- Business-focused interpretation of analytical results

---

## 📝 Notes
This project is intended as a methodological case study. The focus is on analytical rigor, clarity, and decision-making rather than domain-specific assumptions.
