# Olist Retail Project — Data Architecture

## 1. Architecture Overview

The Olist Retail Project follows a layered data architecture based on the Bronze, Silver, and Gold pattern.

```text
                 OLIST DATASET
                       │
                       ▼
                RAW CSV FILES
                       │
                       ▼
              ┌─────────────────┐
              │  BRONZE LAYER   │
              │   Raw Delta     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  SILVER LAYER   │
              │ Clean + Validate│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   GOLD LAYER    │
              │ Business Models │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      Databricks SQL          Power BI
```

---

## 2. Source Layer

The source layer contains the original Olist CSV datasets stored in a Databricks Volume.

Storage location:

```text
/Volumes/workspace/default/pulsecart
```

Source datasets:

```text
customers
geolocation
order_items
order_payments
order_reviews
orders
products
sellers
category_translation
```

The original raw files are kept separate from the GitHub repository.

---

## 3. Bronze Layer

The Bronze layer converts the raw CSV files into Delta tables.

Current tables:

```text
bronze_customers
bronze_orders
bronze_order_items
bronze_payments
bronze_reviews
bronze_products
bronze_sellers
bronze_geolocation
bronze_category_translation
```

The Bronze layer is intended to provide a stable representation of the source data for downstream processing.

---

## 4. Core Data Relationships

```text
CUSTOMERS
    │
    │ customer_id
    ▼
ORDERS
    │
    ├───────────────► PAYMENTS
    │                    │
    │                    └── order_id
    │
    ├───────────────► REVIEWS
    │                    │
    │                    └── order_id
    │
    └───────────────► ORDER_ITEMS
                         │
                         ├── product_id ──► PRODUCTS
                         │
                         └── seller_id ───► SELLERS

PRODUCTS
    │
    │ product_category_name
    ▼
CATEGORY_TRANSLATION

CUSTOMERS
    │
    │ customer_zip_code_prefix
    ▼
GEOLOCATION

SELLERS
    │
    │ seller_zip_code_prefix
    ▼
GEOLOCATION
```

---

## 5. Silver Layer

The Silver layer is responsible for transforming raw Bronze data into reliable analytical data.

Major operations include:

### Standardization

* Consistent column names
* Correct numeric types
* Correct timestamp types
* Consistent categorical values

### Data Quality

* Null detection
* Duplicate detection
* Referential-integrity checks
* Invalid-value checks
* Date consistency checks

### Business Transformations

Examples include:

```text
delivery_days
delivery_delay_days
is_delivered_late
order_revenue
customer_order_count
customer_total_spend
```

The exact transformations will be defined during implementation based on the source data.

---

## 6. Gold Layer

The Gold layer will contain business-focused analytical models.

Potential Gold datasets include:

```text
gold_revenue_monthly
gold_customer_360
gold_product_performance
gold_seller_performance
gold_delivery_performance
gold_customer_experience
gold_payment_analysis
gold_data_quality
```

These datasets will be optimized for analytical queries and dashboard consumption.

---

## 7. Analytical Domains

### Revenue Intelligence

Focuses on:

* Revenue trends
* Average order value
* Category revenue
* Payment behavior

### Customer Intelligence

Focuses on:

* Customer lifetime value
* Purchase frequency
* Repeat customers
* Customer segmentation

### Product Intelligence

Focuses on:

* Product performance
* Category performance
* Revenue contribution
* Product characteristics

### Seller Intelligence

Focuses on:

* Seller revenue
* Seller order volume
* Seller geography
* Seller delivery performance

### Operations Intelligence

Focuses on:

* Delivery duration
* Delivery delays
* Freight costs
* Estimated vs actual delivery

### Customer Experience

Focuses on:

* Review scores
* Review trends
* Delivery performance vs review scores

---

## 8. Orchestration

The final pipeline will be orchestrated using **Databricks Workflows**.

Conceptually:

```text
          START
            │
            ▼
      Raw Ingestion
            │
            ▼
     Bronze Validation
            │
            ▼
    Silver Transformation
            │
            ▼
      Quality Checks
            │
            ▼
     Gold Transformation
            │
            ▼
       BI / Analytics
            │
            ▼
           END
```

---

## 9. Monitoring

The project will eventually include pipeline observability covering:

* Pipeline execution status
* Processing duration
* Records processed
* Records rejected
* Data-quality results
* Transformation failures

This will help demonstrate production-oriented data engineering practices.

---

## 10. Design Principle

The architecture follows the principle:

> **Raw data should be preserved, transformations should be traceable, and business datasets should be separated from engineering layers.**

This separation makes the platform easier to maintain, debug, extend, and co
