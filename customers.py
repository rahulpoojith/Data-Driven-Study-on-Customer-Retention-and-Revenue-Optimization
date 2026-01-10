import pandas as pd
import numpy as np

np.random.seed(42)

n_customers = 20000

customers = pd.DataFrame({
    "customer_id": range(1, n_customers + 1),
    "age": np.random.randint(21, 65, n_customers),
    "tenure_months": np.random.randint(1, 60, n_customers),
    "city": np.random.choice(
        ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad"],
        n_customers
    ),
    "plan_type": np.random.choice(
        ["Silver", "Gold", "Platinum"],
        n_customers,
        p=[0.4, 0.35, 0.25]
    ),
    "monthly_charge": np.random.randint(400, 1200, n_customers),
    "avg_data_usage_gb": np.round(
        np.random.uniform(5, 50, n_customers), 2
    )
})

customers.to_csv("Datasets/customers.csv", index=False)
print("customers.csv created successfully")