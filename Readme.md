# AutoForge Supply Chain Analytics

**Real-world Automotive Supply Chain Analysis Project**  
Messy ERP data → Cleaning → Analysis → Actionable Insights (Google Sheets + SQL + Python + Looker Studio)

## Project Overview
You are the new Supply Chain Analyst at **AutoForge Motors** — a manufacturer of SUVs and Sedans.  
This repo demonstrates how to handle messy multi-system data (ERP, MES, WMS) and turn it into business decisions that prevent production line stoppages and optimize cash flow.

## Day 1: Google Sheets Basics – Taming Messy Master Data
**What we built today:**
- Generated realistic messy automotive data (suppliers, BOM, inventory, logistics, demand)
- Proper raw vs clean sheet workflow
- Data cleaning (Trim whitespace, Remove duplicates, fix data types)
- Linked tables using **XLOOKUP**
- Built **Master Combined View** with first KPIs:
  - Lead time risk
  - Critical components
  - Defect impact

**Key skills demonstrated:**
- Google Sheets data cleaning best practices
- XLOOKUP for linking tables
- Creating a Master Combined View for supply chain analysis

## Day 2: Inventory Valuation, Production Variance & Mini Dashboard
**What we built today:**
- Calculated core automotive KPIs:
  - Total inventory value
  - Days of cover
  - ABC classification (A/B/C analysis)
  - Lead time risk & critical components
- Used powerful Google Sheets functions:
  - **QUERY** (SQL-like dynamic filtering and sorting)
  - **FILTER** (dynamic views of critical items)
- Created first mini interactive dashboard

**Key skills demonstrated:**
- Advanced Google Sheets formulas (QUERY, FILTER)
- Core automotive supply chain KPIs
- Building interactive mini dashboards

## Day 3: SQL – Connecting ERP/MES/WMS/TMS Data in PostgreSQL
**What we built today:**
- Created `autoforge` schema inside the `supply_chain` PostgreSQL database
- 4 normalized tables with proper primary keys, foreign keys & CHECK constraints
- Imported cleaned CSVs using `COPY` commands
- Wrote 4 production-ready JIT supply-chain queries

**Key skills demonstrated:**
- Relational database design for automotive supply chain
- JOINs across ERP + WMS + TMS systems
- COALESCE + CASE statements for risk scoring and OTIF logic
- ABC classification value analysis

**New files added:**
- `sql/queries/` → 4 reusable `.sql` files

## Day 4: Advanced SQL – Reusable Views, CTEs, Window Functions + Python Connection
**What we built today:**
- 3 powerful **reusable VIEWS** (`vw_critical_jit_stock`, `vw_supplier_risk`, `vw_open_po_risk`)
- Advanced queries using **CTEs** and **Window Functions**
- Live connection from Jupyter Notebook to PostgreSQL using `sqlalchemy`

**Key skills demonstrated:**
- `CREATE OR REPLACE VIEW`
- CTEs for readable complex logic
- Window Functions (`RANK() OVER PARTITION BY`)
- Python + SQLAlchemy integration

**New files added:**
- `sql/queries/` → advanced view and query files
- `notebooks/01_data_generation.ipynb`

## Day 5: Looker Studio – Professional JIT Supply Chain Dashboard
**What we built today:**
- Complete **4-page interactive dashboard** in Google Looker Studio
- Connected three advanced PostgreSQL views via CSV export
- Designed with real automotive/JIT principles (risk alerts, A-class focus)

**Dashboard Pages:**
1. Executive Overview
2. Critical JIT Stock Alerts
3. Supplier Risk
4. Open PO Risk

**Key skills demonstrated:**
- Professional Looker Studio dashboard design
- Conditional formatting and cross-page filters
- Visual risk alerts for JIT supply chain

**Key Features:**
- Automotive-themed design with clear risk alerts
- Easy refresh via CSV upload

## Day 6: Python Pandas – Full ETL Pipeline + Prophet Forecasting
**What we built today:**
- Complete end-to-end **ETL pipeline** in `notebooks/02_python_etl_pipeline.ipynb`
- Automated cleaning, KPI calculation, and CSV export for Looker Studio
- Added Prophet demand forecasting with delay-risk flags

**Key skills demonstrated:**
- Professional Pandas ETL pipeline
- ABC classification using Pareto logic
- Prophet time-series forecasting
- Full automation replacing manual steps

**Key Outputs:**
- Fresh CSVs for the Looker Studio dashboard
- 60-day demand forecast with risk alerts

**How to run:**
1. Open `notebooks/02_python_etl_pipeline.ipynb`
2. Run all cells
3. Refresh Looker Studio with new CSVs

## Automotive Supply Chain Domain Concepts
- **JIT (Just-In-Time)**, **BOM**, **MRP**, **OTIF**, **ABC Analysis**, **Lead Time Variability** (see original for full details)

## Technologies Used
- Google Sheets • SQL (PostgreSQL) • Python (Pandas + Prophet) • Looker Studio • Git + GitHub

---

**Feel free to clone this repo and follow along!**

Made with ❤️ for anyone learning supply chain analytics.
