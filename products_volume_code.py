# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# DBTITLE 1,Volume Code Workspace — workspace.retail.products
# MAGIC %md
# MAGIC # Volume Code Workspace — workspace.retail.products
# MAGIC
# MAGIC This notebook is the **coding workspace for the `products` volume**:
# MAGIC
# MAGIC `/Volumes/workspace/retail/products`
# MAGIC
# MAGIC Everything coded here works with the files stored in this volume (raw CSVs + exported table data) — so each volume has its own dedicated notebook and the user is never confused about where the data lives.

# COMMAND ----------

# DBTITLE 1,List Files in This Volume
# ============ THIS VOLUME ============

volume_path = "/Volumes/workspace/retail/products"

print(f"Files in volume: {volume_path}\n")

volume_files = dbutils.fs.ls(volume_path)

for f in volume_files:
    print(f"• {f.name} ({f.size} bytes)")

# COMMAND ----------

# DBTITLE 1,Load CSV from Volume
# ============ LOAD CSV FROM THIS VOLUME ============

csv_files = [
    f.name for f in volume_files
    if f.name.endswith(".csv")
]

if csv_files:

    csv_file_path = f"{volume_path}/{csv_files[0]}"

    print("Loading CSV file:", csv_file_path, "\n")

    volume_df = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .csv(csv_file_path)

    display(volume_df)

else:

    print("No CSV files found in this volume yet.")
    volume_df = None

# COMMAND ----------

# DBTITLE 1,Show Tables in workspace.retail
# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.retail;

# COMMAND ----------

# DBTITLE 1,List Tables + Descriptions → Fetch (Interactive)
# ============ FETCH A TABLE FROM workspace.retail (INTERACTIVE) ============

# ---- 1. How many tables are there in the schema? ----

tables_df = spark.sql("SHOW TABLES IN workspace.retail")

table_names = [row["tableName"] for row in tables_df.collect()]

print(f"There are {len(table_names)} tables in workspace.retail:\n")

for name in table_names:
    print(f"  • {name}")

# ---- 2. What are their descriptions? ----

info_df = spark.sql("""
    SELECT table_name, comment
    FROM workspace.information_schema.tables
    WHERE table_schema = 'retail'
""")

print("\nTable descriptions:\n")

for row in info_df.collect():

    description = row["comment"] or "no description given"

    print(f"  • {row['table_name']}: {description}")

# ---- 3. Ask the user which table to fetch ----

table = input("\nEnter the table name to fetch: ")

full_table = f"workspace.retail.{table}"

# ---- 4. Fetch the table ----

volume_df = spark.sql(f"SELECT * FROM {full_table}")

display(volume_df)

# COMMAND ----------

# DBTITLE 1,Your Code Area
# ============ YOUR CODE AREA ============
# Write any analysis / transformation on this volume's data here

# Example:
# volume_df.groupBy("Customer_name").count().show()