import pandas as pd
import numpy as np

# Load datasets
customers = pd.read_csv("Datasets/customers.csv")
campaign_assignment = pd.read_csv("Datasets/campaign_assignment.csv")

# Billing cycles (Quarter)
billing_cycles = pd.to_datetime([
    "2025-01-01",
    "2025-02-01",
    "2025-03-01"
])

# Track active customers
active_customers = set(customers["customer_id"])

activity_records = []

# Index customers for fast lookup
customer_lookup = customers.set_index("customer_id")

for month in billing_cycles:
    for _, row in campaign_assignment.iterrows():

        customer_id = row["customer_id"]

        # Skip already churned customers
        if customer_id not in active_customers:
            continue

        tenure = customer_lookup.loc[customer_id, "tenure_months"]

        # Base churn depends on tenure (new users churn more)
        base_churn_prob = np.clip(
            0.06 - 0.0008 * tenure,
            0.015,
            0.08
        )

        # Treatment effect is partial, not uniform
        if row["experiment_group"] == "B":
            churn_prob = base_churn_prob * np.random.uniform(0.75, 0.9)
            upgrade_prob = np.random.uniform(0.04, 0.07)
        else:
            churn_prob = base_churn_prob
            upgrade_prob = np.random.uniform(0.02, 0.04)

        churned = np.random.rand() < churn_prob
        upgraded = np.random.rand() < upgrade_prob

        base_revenue = np.random.randint(400, 1200)

        # Discount applies only if active
        revenue = base_revenue * 0.9 if row["experiment_group"] == "B" else base_revenue

        activity_records.append([
            customer_id,
            month,
            churned,
            upgraded,
            round(revenue, 2)
        ])

        if churned:
            active_customers.remove(customer_id)

customer_activity = pd.DataFrame(
    activity_records,
    columns=[
        "customer_id",
        "activity_month",
        "churned",
        "upgraded",
        "revenue"
    ]
)

customer_activity.to_csv("Datasets/customer_activity.csv", index=False)
print("customer_activity.csv created successfully")