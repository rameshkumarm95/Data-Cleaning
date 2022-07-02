#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import chardet


# In[2]:


sample_entry=b'\xa7A\xa6n'
print(sample_entry)


# In[3]:


type(sample_entry)


# In[6]:


new_entry = "big5-tw"


# In[7]:


type(new_entry)


# In[8]:


Coverted_entry = new_entry.encode("utf-8",errors="replace")


# In[9]:


type(Coverted_entry)


# In[10]:


Coverted_entry


# In[11]:


print(Coverted_entry.decode("utf-8"))


# In[12]:


print(Coverted_entry.decode("ascii"))


# In[13]:


dataset = pd.read_csv("R:\Technocolabs\PoliceKillingsUS.csv")
dataset.head()


# In[14]:


with open("R:\Technocolabs\PoliceKillingsUS.csv",'rb') as rawdata:
    result=chardet.detect(rawdata.read(10000))


# In[15]:


result


# In[16]:


dataset = pd.read_csv("R:\Technocolabs\PoliceKillingsUS.csv",
                      encoding='Windows-1252')
dataset.head()


# In[17]:


dataset.to_csv("PoliceKillingsUS-utf8.csv")

