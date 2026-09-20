# Olist Retail Project — Project Requirements

## 1. Project Objective

The objective of the Olist Retail Project is to build an end-to-end data engineering and analytics platform using the Brazilian E-Commerce Public Dataset by Olist.

The platform will transform raw e-commerce datasets into clean, validated, analytics-ready data that can support business intelligence and decision-making.

---

## 2. Primary Goals

The project should:

1. Ingest multiple raw CSV datasets.
2. Store raw data using Delta Lake.
3. Build a Bronze data layer.
4. Build a cleaned and standardized Silver layer.
5. Build business-oriented Gold datasets.
6. Implement data-quality checks.
7. Create customer, product, seller, revenue, and operational analytics.
8. Automate the pipeline using Databricks Workflows.
9. Provide analytical outputs for Databricks SQL and Power BI.
10. Maintain the project using Git and GitHub.

---

## 3. Source Data

The project uses nine Olist datasets:

```text
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

---

## 4. Data Engineering Requirements

### Bronze Layer

The Bronze layer must:

* Preserve source data.
* Store datasets as Delta tables.
* Maintain the source structure as much as practical.
* Provide a reliable foundation for downstream transformations.

### Silver Layer

The Silver layer must:

* Standardize data types.
* Convert timestamp columns correctly.
* Handle missing values according to defined rules.
* Identify duplicate records.
* Standardize column naming.
* Validate relationships between datasets.
* Create useful derived fields.
* Enrich product categories using the translation dataset.
* Calculate delivery-related metrics.

### Gold Layer

The Gold layer should contain business-ready analytical datasets covering:

* Revenue
* Customers
* Products
* Sellers
* Orders
* Delivery performance
* Customer reviews
* Payments

---

## 5. Data Quality Requirements

The project should measure data quality rather than silently removing problematic records.

Checks should include:

* Null-value detection
* Duplicate detection
* Invalid data types
* Invalid foreign-key relationships
* Invalid timestamps
* Negative or invalid financial values
* Missing product relationships
* Missing seller relationships
* Order consistency
* Delivery-date consistency

The project should maintain measurable quality metrics where practical.

---

## 6. Business Intelligence Requirements

The project should support analysis of:

### Revenue

* Total revenue
* Revenue by month
* Revenue by category
* Average order value
* Payment behavior

### Customers

* Total customers
* Repeat customers
* Customer purchase frequency
* Customer revenue contribution
* Customer segmentation

### Products

* Product/category performance
* Revenue contribution
* Order volume
* Product characteristics

### Sellers

* Seller order volume
* Seller revenue
* Seller geographic distribution
* Delivery performance

### Operations

* Delivery duration
* Late deliveries
* Estimated vs actual delivery
* Freight cost analysis

### Customer Experience

* Review-score distribution
* Review scores by category
* Review scores vs delivery performance

---

## 7. Technology Requirements

The project will use:

* Python
* PySpark
* SQL
* Databricks
* Delta Lake
* Databricks Workflows
* Git
* GitHub
* Power BI

---

## 8. Repository Requirements

The GitHub repository should contain:

```text
notebooks/
sql/
docs/
README.md
```

Raw datasets should not be committed to GitHub.

---

## 9. Productionization Requirements

The final project should include:

* Automated workflow execution
* Pipeline monitoring
* Data-quality monitoring
* Reproducible transformations
* Clear documentation
* Git-based version control

---

## 10. Expected Final Outcome

The completed project should demonstrate the ability to take a real-world multi-table e-commerce dataset and build a structured data platform capable of supporting both engineering workloads and business analytics.
