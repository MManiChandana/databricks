# PulseCart Architecture

## High-Level Architecture

```text
                PULSECART DATA SOURCES
                         |
          +--------------+--------------+
          |              |              |
       Customers       Products       Orders
          |              |              |
          +--------------+--------------+
                         |
                         v
                  BRONZE LAYER
                  Raw Delta Tables
                         |
                         v
                  SILVER LAYER
              Clean + Validated Data
                         |
                         v
                   GOLD LAYER
               Business Intelligence
                         |
              +----------+----------+
              |                     |
              v                     v
       Databricks SQL          Power BI
              |
              v
      Business Decisions