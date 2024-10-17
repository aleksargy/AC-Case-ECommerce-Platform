# Sales Forecasting for an E-commerce Platform

## Overview

In this project, you will develop a sales forecasting model for an e-commerce platform in preparation for the upcoming holiday season. The goal is to forecast future sales based on historical data, analyse the impact of promotions, and provide recommendations for inventory management. Accurate forecasting will help the company avoid overstocking or understocking items, ensuring smooth operations and maximising profit during the high-demand season.

You will be provided with several datasets containing historical sales, product details, and past promotions. Your task is to analyse the data, build a predictive model, and offer actionable insights.

## Case Study

### Objective
The company needs an accurate prediction of sales for the upcoming holiday season. With a wide range of products and an active promotions strategy, the challenge is to understand how these factors influence sales and how best to allocate inventory. You are tasked with the following:
1. **Sales Forecasting**: Use historical data to predict sales trends for the holiday season.
2. **Promotion Effectiveness**: Evaluate the impact of past promotions on sales performance.
3. **Inventory Recommendations**: Offer insights on which products to prioritise in terms of stock management, based on your sales forecast.

### Datasets

1. **`sales.csv`**: Contains historical sales data, including:
   - `date`: The date of the sale.
   - `product_id`: The unique identifier for each product.
   - `quantity_sold`: Number of units sold.
   - `revenue`: Revenue generated from the sale.
   - `promotion_id`: The identifier for any promotion associated with the sale.

2. **`products.csv`**: Provides details on the products sold:
   - `product_id`: Unique identifier for each product.
   - `category`: Product category (e.g., electronics, clothing).
   - `price`: Sale price of the product.
   - `cost`: Cost to the company.
   - `stock_on_hand`: The current inventory level of the product.
   - `supplier`: Supplier information.

3. **`holiday_promotions.csv`**: Information on past holiday promotions, including:
   - `promotion_id`: Unique identifier for the promotion.
   - `promotion_type`: Type of promotion (e.g., percentage discount, buy-one-get-one).
   - `start_date`: Start date of the promotion.
   - `end_date`: End date of the promotion.
   - `discount_percentage`: Percentage discount applied during the promotion.
   - `ad_spend`: The advertising spend for the promotion.

### Key Questions

1. **How can historical trends be used to forecast future sales?**
   - Identify patterns in sales data and use these to build a time series model that predicts sales for the upcoming holiday season.

2. **How effective have past promotions been?**
   - Evaluate the success of various promotion types and their impact on sales. Which promotions resulted in the highest sales lift? Were there any that were less effective? Is the ad spend worthwhile?

3. **What products should the company prioritise in terms of inventory for the holiday season?**
   - Based on your forecast, provide inventory recommendations to ensure the company stocks enough high-demand items while avoiding overstocking low-demand products.

### Deliverables

1. **Sales Forecast Model**: Develop a model to predict future sales, incorporating seasonal trends and the impact of promotions.
2. **Promotion Impact Analysis**: Analyse the effectiveness of past promotions and provide insights on how they should influence future promotions.
3. **Inventory Recommendations**: Offer clear recommendations on stock levels for the holiday season based on the sales forecast.

### Optional Frontend
Optionally, you can develop a simple dashboard that allows stakeholders to:
- Explore the forecasted sales by product category.
- Visualise the effectiveness of past promotions.
- Get recommendations on inventory management for the holiday season.

## Expected Outcome

At the end of the project, you should be able to:
- Present a forecast for holiday sales, backed by data analysis.
- Demonstrate how past promotions impacted sales and how they should inform future decisions.
- Provide actionable recommendations for inventory management based on the sales forecast.
