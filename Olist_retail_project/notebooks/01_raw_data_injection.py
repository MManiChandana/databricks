from pyspark.sql import functions as F

base_path = "/Volumes/workspace/default/pulsecart"

files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

for file in files:
    path = f"{base_path}/{file}"
    
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(path)
    )
    
    print(f"\n{'='*70}")
    print(f"FILE: {file}")
    print(f"ROWS: {df.count()}")
    print(f"COLUMNS: {len(df.columns)}")
    print(f"{'='*70}")
    
    display(df.limit(5))
