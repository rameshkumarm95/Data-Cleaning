#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import seaborn as sns
import datetime


# In[24]:


earthquakes=pd.read_csv("R:\Technocolabs\database.csv")
earthquakes


# In[25]:


earthquakes.head()


# In[26]:


print(earthquakes['Date'].head())


# In[27]:


earthquakes['Date'].dtype


# In[28]:


earthquakes[3378:3383]


# In[30]:


date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()


# In[31]:


indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]


# In[51]:


earthquakes['Date_Parsed']=pd.to_datetime(earthquakes['Date'],
                                         infer_datetime_format=True)
print(earthquakes['Date_Parsed'].head())


# In[60]:


day_of_month_earthquakes=earthquakes['Date_Parsed'].dt.strftime("%d/%m/%Y %H:%M")
day_of_month_earthquakes


# In[62]:


day_of_month_earthquakes=day_of_month_earthquakes.dropna()


# In[63]:


sns.distplot(day_of_month_earthquakes, kde=False, bins=31)

