#!/usr/bin/env python
# coding: utf-8

# In[27]:


# 1. Bring the Pandas 'tool' out of the toolbox
import pandas as pd

# 2. Create a dictionary (a list of your columns and rows)
my_warehouse_data = {
    'Material_Code': ['MAT-1001', 'MAT-1002', 'MAT-1003'],
    'Stock_Qty': [550, 20, 300],
    'Unit_Cost': [5.50, 12.00, 2.25],
    'Column_name' : ['R1','R2','']
}

# 3. Convert that raw data into a beautiful Pandas Excel-like table
df = pd.DataFrame(my_warehouse_data)

# Create the new column using your exact logic
df['Total_Value'] = df['Stock_Qty'] * df['Unit_Cost']

# Sort the table by Total_Value from highest to lowest
df = df.sort_values(by='Total_Value', ascending=False)

# Show the sorted table
df


# In[28]:


# --- 1. FILTERING ---
# We wrap the rule inside df[] to tell Python: "Filter df where this rule is true"
reorder_table = df[df['Stock_Qty'] < 500]

print("--- ITEMS TO REORDER ---")
print(reorder_table)
print("\n") # This just prints a blank line for spacing


# --- 2. LABELING (The IF/ELSE column) ---
# To do an IF/ELSE in Python, we bring in Pandas' calculator tool called NumPy
import numpy as np

# np.where works EXACTLY like Excel's =IF(condition, value_if_true, value_if_false)
df['Status'] = np.where(df['Stock_Qty'] < 500, 'Reorder', 'OK')

print("--- FULL TABLE WITH STATUS ---")
print(df)


# In[29]:


# 1. Create the second table (Procurement Data)
procurement_data = {
    'Material_Code': ['MAT-1001', 'MAT-1002', 'MAT-1003'],
    'Vendor_Name': ['Acme Steel', 'Global Rubber', 'ElecWire Co'],
    'Lead_Time_Days': [14, 30, 45]
}

# 2. Turn it into a Pandas DataFrame
vendor_df = pd.DataFrame(procurement_data)

print("--- VENDOR DATA ---")
print(vendor_df)


# In[30]:


# The syntax: pd.merge(Left_Table, Right_Table, on='Common_Column', how='join_type')
master_table = pd.merge(df, vendor_df, on='Material_Code', how='left')

print("--- MASTER TABLE ---")
print(master_table)


# In[31]:


master_table = pd.merge(df, vendor_df, on='Material_Code', how='inner')

print("--- MASTER TABLE ---")
print(master_table)


# In[ ]:




