import pandas as pd
import numpy as np


customer_data = pd.read_csv('olist_customers_dataset.csv')
product_data =pd.read_csv('olist_products_dataset.csv')
item_data = pd.read_csv('olist_order_items_dataset.csv')
geologic_data = pd.read_csv('olist_products_dataset.csv')
payment_data = pd.read_csv('olist_order_payments_dataset.csv')
reviews_data = pd.read_csv('olist_order_reviews_dataset.csv')
order_data = pd.read_csv('olist_orders_dataset.csv')
sellers_data = pd.read_csv('olist_sellers_dataset.csv')
translation = pd.read_csv('product_category_name_translation.csv')