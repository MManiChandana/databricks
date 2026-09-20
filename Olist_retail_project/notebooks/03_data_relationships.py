from pyspark.sql import functions as F

base_path = "/Volumes/workspace/default/pulsecart"

datasets = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}

dfs = {}

for name, file in datasets.items():
    dfs[name] = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(f"{base_path}/{file}")
    )

for name, df in dfs.items():
    print(f"\n{name.upper()}")
    print(df.columns)