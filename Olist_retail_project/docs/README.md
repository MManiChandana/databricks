# Olist Retail Project

## From Raw E-Commerce Data to Business Intelligence

**Olist Retail Project** is an end-to-end data engineering and analytics project built using the public **Brazilian E-Commerce Public Dataset by Olist**.

The project demonstrates how raw multi-table e-commerce data can be transformed into reliable, analytics-ready datasets through a modern **Bronze → Silver → Gold** data architecture.

The goal is not simply to analyze the dataset, but to build a reusable data platform that supports **revenue intelligence, customer intelligence, product analysis, operational analysis, and data-quality monitoring**.

---

## Project Overview

The Olist dataset contains approximately 100K orders and multiple related datasets covering customers, orders, products, sellers, payments, reviews, and geographic information.

This project takes those raw datasets through a complete data engineering pipeline:

```text
Olist CSV Dataset
       │
       ▼
Raw Data
       │
       ▼
Bronze Layer
Raw data stored as Delta tables
       │
       ▼
Silver Layer
Cleaned + validated + standardized data
       │
       ▼
Gold Layer
Business-ready analytical datasets
       │
       ▼
Business Intelligence
Revenue | Customers | Products | Operations
       │
       ▼
Power BI / Databricks SQL
```

---

## Dataset

Source:

**Olist Brazilian E-Commerce Public Dataset**

The project uses the following datasets:

| Dataset              | Approx. Records |
| -------------------- | --------------: |
| Customers            |          99,441 |
| Geolocation          |       1,000,163 |
| Order Items          |         112,650 |
| Payments             |         103,886 |
| Reviews              |          99,224 |
| Orders               |          99,441 |
| Products             |          32,951 |
| Sellers              |           3,095 |
| Category Translation |              71 |

---

## Technology Stack

* **Python**
* **PySpark**
* **SQL**
* **Databricks**
* **Delta Lake**
* **Databricks Workflows**
* **Git**
* **GitHub**
* **Power BI**

---

## Data Architecture

The project follows a layered data engineering architecture.

### Bronze

The Bronze layer stores the raw Olist datasets as Delta tables with minimal transformation.

Current Bronze tables:

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

### Silver

The Silver layer will focus on:

* Data type standardization
* Timestamp conversion
* Null handling
* Duplicate detection
* Data validation
* Standardized column names
* Category enrichment
* Delivery-time calculations
* Data-quality rules
* Invalid-record identification

### Gold

The Gold layer will provide business-ready datasets for:

* Revenue Intelligence
* Customer Intelligence
* Product Intelligence
* Seller Intelligence
* Delivery & Operations Intelligence
* Customer Experience Analysis
* Data Quality Monitoring

---

## Key Business Questions

The project will answer questions such as:

### Revenue

* How is revenue changing over time?
* What is the average order value?
* Which product categories generate the most revenue?
* What payment methods are most frequently used?

### Customer

* How many customers are repeat customers?
* Which customers generate the highest revenue?
* What is the purchasing frequency of customers?
* Which customer segments require attention?

### Product

* Which products and categories perform best?
* Which products generate high revenue?
* How does product availability relate to sales?

### Seller

* Which sellers generate the most orders and revenue?
* How does seller performance vary geographically?
* Which sellers have delivery-related issues?

### Operations

* How long does delivery take?
* Which orders are delivered late?
* How does actual delivery compare with estimated delivery?
* Is delivery performance associated with customer review scores?

### Customer Experience

* How are review scores distributed?
* Does late delivery correlate with lower review scores?
* Which categories receive stronger customer feedback?

### Data Quality

* Which datasets contain missing values?
* Are there duplicate records?
* Are relationships between datasets valid?
* What percentage of records pass quality checks?

---

## Project Features

The project will progressively implement:

* End-to-end ETL pipeline
* Delta Lake storage
* Bronze/Silver/Gold architecture
* Data-quality framework
* Customer 360 analysis
* Revenue analytics
* Product and category analytics
* Seller performance analysis
* Delivery performance analysis
* Review and customer-experience analysis
* Pipeline monitoring
* Databricks Workflows
* Power BI dashboards
* Git/GitHub version control

---

## Repository Structure

```text
Olist_retail_project/
│
├── notebooks/
│   ├── 01_ingestion
│   ├── 02_raw_data_profiling
│   ├── 03_data_relationships
│   └── 04_bronze_ingestion
│
├── sql/
│
├── data/
│
├── docs/
│   ├── project_requirements.md
│   └── architecture.md
│
└── README.md
```

> Raw Olist CSV files are stored in Databricks storage rather than committed to GitHub.

---

## Current Progress

### Phase 1 — Project Foundation

* [x] Project structure created
* [x] GitHub repository connected to Databricks
* [x] Documentation structure created

### Phase 2 — Dataset Exploration

* [x] Olist dataset obtained
* [x] 9 source datasets uploaded to Databricks Volume
* [x] Dataset row counts verified
* [x] Dataset schemas inspected
* [x] Dataset relationships identified

### Phase 3 — Bronze Layer

* [x] Raw CSV ingestion implemented
* [x] 9 Bronze Delta tables created
* [ ] Bronze validation
* [ ] Data-quality profiling

### Phase 4 — Silver Layer

* [ ] Data cleaning
* [ ] Data type standardization
* [ ] Null handling
* [ ] Duplicate handling
* [ ] Relationship validation
* [ ] Business transformations

### Phase 5 — Gold Layer

* [ ] Revenue analytics
* [ ] Customer 360
* [ ] Product intelligence
* [ ] Seller intelligence
* [ ] Operations intelligence
* [ ] Customer experience analytics

### Phase 6 — Productionization

* [ ] Databricks Workflows
* [ ] Pipeline monitoring
* [ ] Data-quality monitoring
* [ ] GitHub documentation
* [ ] Power BI dashboard

---

## Project Goal

The final objective is to demonstrate practical experience in building a complete data platform—from **raw data ingestion to business-ready analytics**—using modern cloud data engineering technologies.

This project is designed as a portfolio project demonstrating practical skills in:

```text
Data Ingestion
      ↓
Data Engineering
      ↓
Data Quality
      ↓
Data Transformation
      ↓
Data Modeling
      ↓
Business Analytics
      ↓
Visualization
```

---

## Author

**M Mani Chandana**

GitHub: `MManiChandana`

Project: **Olist Retail Project**
