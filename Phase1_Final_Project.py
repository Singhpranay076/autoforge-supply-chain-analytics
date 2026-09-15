#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import duckdb

# 1. MARA (Material Master) - The "What is it?" table
mara_data = {
    'Material_Code': ['MAT-100', 'MAT-101', 'MAT-102', 'MAT-103'],
    'Material_Type': ['Raw', 'Raw', 'Finished', 'Raw'],
    'Description': ['Steel Sheet', 'Rubber Valve', 'Engine Block', 'Copper Wire']
}
mara_df = pd.DataFrame(mara_data)

# 2. MBEW (Valuation/Stock) - The "How much is it worth?" table
mbew_data = {
    'Material_Code': ['MAT-100', 'MAT-101', 'MAT-102', 'MAT-103'],
    'Stock_Qty': [50, 1200, 10, 0],
    'Unit_Cost_USD': [100.0, 2.5, 5000.0, 15.0]
}
mbew_df = pd.DataFrame(mbew_data)

# 3. EKPO (Open Purchase Orders) - The "What is arriving soon?" table
# Notice MAT-101 and MAT-103 have NO open purchase orders!
ekpo_data = {
    'PO_Number': ['PO-901', 'PO-902', 'PO-903'],
    'Material_Code': ['MAT-100', 'MAT-100', 'MAT-102'],
    'Inbound_Qty': [200, 50, 5]
}
ekpo_df = pd.DataFrame(ekpo_data)

print("SAP Database (MARA, MBEW, EKPO) Initialized.")


# In[2]:


final_project_query = """
-- Step 1: The CTE (Mini-table) to sum up inbound orders first
WITH InboundOrders AS (
    SELECT 
        Material_Code, 
        SUM(Inbound_Qty) as Total_Inbound
    FROM ekpo_df
    GROUP BY Material_Code
)

-- Step 2: The Main Dashboard Query
SELECT 
    m.Material_Code,
    m.Description,

    -- Calculating Total Value on the fly
    (v.Stock_Qty * v.Unit_Cost_USD) AS Current_Value_USD,

    -- Protecting our data with COALESCE
    COALESCE(i.Total_Inbound, 0) AS Pipeline_Qty

FROM mara_df AS m

-- INNER JOIN because a material MUST have a valuation record
INNER JOIN mbew_df AS v 
    ON m.Material_Code = v.Material_Code

-- LEFT JOIN because a material might NOT have open purchase orders
LEFT JOIN InboundOrders AS i
    ON m.Material_Code = i.Material_Code

-- Filtering only for the VP's request
WHERE m.Material_Type = 'Raw'
"""

print("--- SUPPLY CHAIN STOCK-OUT RISK REPORT ---")
print(duckdb.query(final_project_query).df())


# In[ ]:




