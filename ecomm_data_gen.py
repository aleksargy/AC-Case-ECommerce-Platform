import pandas as pd
import numpy as np
from datetime import timedelta

np.random.seed(42)

dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq='D')

num_products = 20
num_promotions = 8

# Product details
categories = ['Electronics', 'Clothing', 'Home Goods', 'Toys']
products = []
for i in range(1, num_products + 1):
    products.append([f"P{i:03}", np.random.choice(categories), np.random.uniform(10, 500), 
                     np.random.uniform(5, 300), np.random.randint(50, 1000), f"Supplier_{np.random.randint(1, 5)}"])

products_df = pd.DataFrame(products, columns=['product_id', 'category', 'price', 'cost', 'stock_on_hand', 'supplier'])

# Promotion details
promotion_types = ['Percentage Discount', 'Buy-One-Get-One', 'Free Shipping', 'Flash Sale']
promotions = []

# Promotions for holidays and non-holidays, some more effective than others
for i in range(1, num_promotions + 1):
    promotion_type = np.random.choice(promotion_types)
    # Holiday promotions are more effective
    start_date = np.random.choice(pd.date_range(start="2022-11-01", end="2022-12-31", freq='D') if i % 2 == 0 else pd.date_range(start="2022-03-01", end="2022-04-30", freq='D'))
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(start_date) + timedelta(days=np.random.randint(3, 10))
    discount = np.random.uniform(10, 50) if promotion_type == 'Percentage Discount' else 0
    ad_spend = np.random.uniform(1000, 10000)
    promotions.append([f"PR{i:02}", promotion_type, start_date.date(), end_date.date(), discount, ad_spend])

promotions_df = pd.DataFrame(promotions, columns=['promotion_id', 'promotion_type', 'start_date', 'end_date', 'discount_percentage', 'ad_spend'])

# Historical sales data with strong correlations for promotions
sales_data = []
for date in dates:
    for product in products_df['product_id']:
        # Base sales, slightly higher during holiday season (Nov-Dec)
        base_sales = np.random.poisson(5) + (3 if date.month in [11, 12] else 0)
        revenue = base_sales * products_df.loc[products_df['product_id'] == product, 'price'].values[0]
        promotion_id = None
        
        # Apply promotions and adjust sales
        for _, promo in promotions_df.iterrows():
            if promo['start_date'] <= date.date() <= promo['end_date']:
                promotion_id = promo['promotion_id']
                if promo['promotion_type'] == 'Percentage Discount':
                    base_sales += np.random.poisson(15)  # Boost during discounts
                elif promo['promotion_type'] == 'Buy-One-Get-One':
                    base_sales += np.random.poisson(10)  # Medium boost
                elif promo['promotion_type'] == 'Flash Sale':
                    base_sales += np.random.poisson(20)  # Large boost for Flash Sales
                elif promo['promotion_type'] == 'Free Shipping':
                    base_sales += np.random.poisson(5)   # Small boost for Free Shipping
                revenue = base_sales * products_df.loc[products_df['product_id'] == product, 'price'].values[0] * (1 - promo['discount_percentage'] / 100)
        
        sales_data.append([date.date(), product, base_sales, revenue, promotion_id])

sales_df = pd.DataFrame(sales_data, columns=['date', 'product_id', 'quantity_sold', 'revenue', 'promotion_id'])

# Save to CSV
sales_df.to_csv('data/sales.csv', index=False)
products_df.to_csv('data/products.csv', index=False)
promotions_df.to_csv('data/holiday_promotions.csv', index=False)
