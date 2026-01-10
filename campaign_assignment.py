import pandas as pd
import numpy as np

# Load customers data
customers = pd.read_csv("Datasets/customers.csv")

n_customers = len(customers)

campaign_assignment = pd.DataFrame({
    "customer_id": customers["customer_id"],
    "experiment_group": np.random.choice(["A", "B"], n_customers),
    "offer_type": "10% Bill Discount",
    "assignment_date": "2025-01-01"
})

campaign_assignment.to_csv("Datasets/campaign_assignment.csv", index=False)
print("campaign_assignment.csv created successfully")