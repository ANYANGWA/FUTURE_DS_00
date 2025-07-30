# sales_analysis.py

import pandas as pd

# Sample data
data = {
    'Product': ['Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop'],
    'Units Sold': [100, 80, 60, 90, 95],
    'Unit Price': [300, 800, 200, 310, 820]
}

df = pd.DataFrame(data)

# Calculate total sales
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Summary
summary = df.groupby('Product').agg({'Total Sales': 'sum', 'Units Sold': 'sum'})

print("Sales Summary by Product:")
print(summary)