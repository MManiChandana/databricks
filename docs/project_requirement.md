# PulseCart — Project Requirements

## 1. Project Overview

PulseCart is an end-to-end e-commerce data engineering and analytics platform built using Databricks.

The platform ingests raw e-commerce data, cleans and validates it, transforms it into analytical datasets, and produces business intelligence for customers, products, orders, revenue, and operations.

---

## 2. Business Problem

An e-commerce company receives large amounts of customer, product, order, and payment data.

The raw data may contain:

- Duplicate records
- Missing values
- Invalid prices
- Incorrect dates
- Inconsistent values
- Invalid customer or product references

Business teams need reliable data to understand:

- Revenue
- Orders
- Customers
- Products
- Customer segments
- Business trends

PulseCart provides a reliable data pipeline that transforms raw data into trusted business intelligence.

---

## 3. Project Goals

The project will:

1. Ingest raw e-commerce data.
2. Store raw data using Delta Lake.
3. Clean and validate incoming data.
4. Handle duplicate and invalid records.
5. Build Silver-level trusted datasets.
6. Create Gold-level business intelligence tables.
7. Calculate business KPIs.
8. Generate customer intelligence.
9. Monitor data quality.
10. Automate the pipeline using Databricks Workflows.
11. Maintain the project using GitHub.
12. Provide analytical outputs for visualization.

---

## 4. Technology Stack

- Python
- PySpark
- SQL
- Databricks
- Delta Lake
- Databricks Workflows
- Git
- GitHub
- Power BI

---

## 5. Architecture

The project will follow the Medallion Architecture:

Raw Data
    ↓
Bronze Layer
    ↓
Silver Layer
    ↓
Gold Layer
    ↓
Business Intelligence

---

## 6. Core Business Areas

### Revenue Intelligence

- Total revenue
- Monthly revenue
- Average order value
- Revenue trends

### Customer Intelligence

- Customer lifetime spending
- Purchase frequency
- Customer segments
- High-value customers
- At-risk customers

### Product Intelligence

- Best-selling products
- Revenue by product
- Revenue by category
- Product performance

### Operational Intelligence

- Order volume
- Payment methods
- Invalid records
- Data quality metrics

---

## 7. Data Quality

The pipeline will detect:

- Duplicate records
- Missing values
- Invalid prices
- Invalid dates
- Invalid customer IDs
- Invalid product IDs
- Invalid order quantities

Invalid records will be identified and handled separately from trusted data.

---

## 8. Expected Output

The final platform should provide:

- Trusted Silver datasets
- Gold analytical datasets
- Business KPI tables
- Customer intelligence
- Product intelligence
- Data quality reports
- Pipeline execution monitoring
- Power BI-ready datasets

---

## 9. Version Control

GitHub will be used to:

- Track code changes
- Maintain project history
- Version notebooks and SQL
- Document project development