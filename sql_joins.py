#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import duckdb

# 1. Table 1: EKPO (The Line Items)
ekpo_data = {
    'PO_Number': ['PO-100', 'PO-100', 'PO-101', 'PO-102'],
    'Item_Pos': [10, 20, 10, 10],
    'Material': ['MAT-01', 'MAT-02', 'MAT-01', 'MAT-03'],
    'Order_Qty': [500, 150, 1000, 200]
}
ekpo_df = pd.DataFrame(ekpo_data)

# 2. Table 2: EKKO (The Header)
# *Notice that PO-102 is missing from this table!*
ekko_data = {
    'PO_Number': ['PO-100', 'PO-101'], 
    'Vendor_Name': ['Acme Corp', 'Global Steel'],
    'Doc_Date': ['2026-09-01', '2026-09-05']
}
ekko_df = pd.DataFrame(ekko_data)

print("SAP PO Tables Ready.")


# In[2]:


# The INNER JOIN: Only keeps rows that have a perfect match in BOTH tables
query_inner = """
SELECT 
    items.PO_Number,
    items.Material,
    items.Order_Qty,
    header.Vendor_Name
FROM ekpo_df AS items
INNER JOIN ekko_df AS header
    ON items.PO_Number = header.PO_Number
"""

print("--- SQL INNER JOIN ---")
print(duckdb.query(query_inner).df())


# In[3]:


# The LEFT JOIN: Keeps EVERYTHING from the 'FROM' table (items), regardless of a match
query_left = """
SELECT 
    items.PO_Number,
    items.Material,
    items.Order_Qty,
    header.Vendor_Name
FROM ekpo_df AS items
LEFT JOIN ekko_df AS header
    ON items.PO_Number = header.PO_Number
"""

print("\n--- SQL LEFT JOIN ---")
print(duckdb.query(query_left).df())


# In[4]:


# The COALESCE Function: Replacing NULLs with clean business logic
query_clean = """
SELECT 
    items.PO_Number,
    items.Material,
    items.Order_Qty,
    COALESCE(header.Vendor_Name, 'UNASSIGNED VENDOR') AS Vendor_Name
FROM ekpo_df AS items
LEFT JOIN ekko_df AS header
    ON items.PO_Number = header.PO_Number
"""

print("\n--- SQL LEFT JOIN (CLEANED WITH COALESCE) ---")
print(duckdb.query(query_clean).df())


# In[ ]:




