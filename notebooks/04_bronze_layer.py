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

for table_name, file_name in datasets.items():

    print(f"Loading: {table_name}")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(f"{base_path}/{file_name}")
    )

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(f"bronze_{table_name}")
    )

    print(f"✓ Created bronze_{table_name}")