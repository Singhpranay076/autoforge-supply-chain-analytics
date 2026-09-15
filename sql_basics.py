#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import duckdb

# 1. Mocking SAP's MBEW (Material Valuation) Table
mbew_data = {
    'Material_Code': ['MAT-01', 'MAT-02', 'MAT-03', 'MAT-04'],
    'Material_Type': ['Raw', 'Finished', 'Raw', 'Packaging'],
    'Total_Stock': [1500, 50, 8500, 200],
    'Total_Value_USD': [15000, 25000, 85000, 400]
}

# Create the DataFrame
mbew_df = pd.DataFrame(mbew_data)
print("Pandas Engine Ready.")


# In[2]:


# The SQL Query: "Select everything from the mbew_df table"
# We add .df() at the end to turn the SQL result back into a beautiful Pandas table
query_1 = """
SELECT * 
FROM mbew_df
"""

result_1 = duckdb.query(query_1).df()
print("--- SQL: SELECT ALL ---")
print(result_1)


# In[3]:


# The SQL Query: "Select everything, but ONLY where the value is greater than 10,000"
query_2 = """
SELECT * 
FROM mbew_df
WHERE Total_Value_USD > 10000
"""

result_2 = duckdb.query(query_2).df()
print("--- SQL: FILTERED FOR HIGH VALUE ---")
print(result_2)


# In[4]:


# 1. Specific Columns (Protecting the Server)
query_4 = """
SELECT 
    Material_Code, 
    Total_Value_USD 
FROM mbew_df
WHERE Material_Type = 'Raw'
"""
print("--- RAW MATERIALS (SPECIFIC COLUMNS) ---")
print(duckdb.query(query_4).df())

# 2. Aggregation (The SQL Pivot Table)
# We use SUM() and GROUP BY to instantly calculate total cash tied up per category
query_5 = """
SELECT 
    Material_Type, 
    SUM(Total_Value_USD) AS Total_Category_Value
FROM mbew_df
GROUP BY Material_Type
"""
print("\n--- INVENTORY VALUE BY CATEGORY ---")
print(duckdb.query(query_5).df())


# In[ ]:




