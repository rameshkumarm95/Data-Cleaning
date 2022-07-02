#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
get_ipython().system('pip install fuzzywuzzy')
import fuzzywuzzy
from fuzzywuzzy import process
import chardet


# In[3]:


professors=pd.read_csv("R:\Technocolabs\pakistan_intellectual_capital.csv")
professors.head()


# In[5]:


professors['Country']=professors['Country'].str.lower()
professors['Country']=professors['Country'].str.strip()


# In[6]:


countries=professors['Country'].unique()
matches = fuzzywuzzy.process.extract("south korea", 
                                     countries, 
                                     limit=10, 
                                     scorer=fuzzywuzzy.fuzz.token_sort_ratio)


# In[9]:


def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):

    strings = df[column].unique()
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    
    rows_with_matches = df[column].isin(close_matches)

    df.loc[rows_with_matches, column] = string_to_match
    
    print("All done!")


# In[10]:


replace_matches_in_column(df=professors, column='Country', 
                          string_to_match="south korea")
countries = professors['Country'].unique()


# In[8]:


countries.sort()
countries

