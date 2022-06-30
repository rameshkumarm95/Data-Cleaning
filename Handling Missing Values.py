#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Handling Missing Values
import pandas as pd
import numpy as np


# In[2]:


sf_permits=pd.read_csv("R:\Technocolabs\Building_Permits.csv")
sf_permits


# In[4]:


sf_permits.head()


# In[5]:


missing_values_count=sf_permits.isnull().sum()


# In[6]:


missing_values_count[0:10]


# In[10]:


total_cells=np.product(sf_permits.shape)
total_missing=missing_values_count.sum()


# In[11]:


percent_missing=(total_missing/total_cells)*100
percent_missing


# In[12]:


missing_values_count[0:10]


# In[13]:


sf_permits.dropna()


# In[15]:


columns_without_missing=sf_permits.dropna(axis=1)
columns_without_missing.head()


# In[16]:


sf_permits.shape[1]


# In[17]:


columns_without_missing.shape[1]


# In[18]:


print("Columns in original dataset : %d\n"%sf_permits.shape[1])
print("Columns with na's dropped: %d"%columns_without_missing.shape[1])


# In[24]:


sf_permits_subset=sf_permits.loc[:,'Street Number':'Record ID'].head()
sf_permits_subset


# In[25]:


sf_permits_with_na_imputed=sf_permits_subset.fillna(0)


# In[26]:


sf_permits_with_na_imputed

