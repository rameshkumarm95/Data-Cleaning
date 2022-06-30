#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from scipy import stats
get_ipython().system('pip install mlxtend')
from mlxtend.preprocessing import minmax_scaling
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


kickstarters_2017=pd.read_csv("R:\Technocolabs\ks-projects-201801.csv")
kickstarters_2017


# In[8]:


original_data=pd.DataFrame(kickstarters_2017.usd_goal_real)
scaled_data=minmax_scaling(original_data, columns=['usd_goal_real'])


# In[10]:


print('Original data\nPreview:\n', original_data.head())
print('Minimum value:', float(original_data.min()),
      '\nMaximum value:', float(original_data.max()))
print('_'*30)


# In[11]:


print('\nScaled data\nPreview:\n', scaled_data.head())
print('Minimum value:', float(scaled_data.min()),
      '\nMaximum value:', float(scaled_data.max()))


# In[14]:


# Scaling the goal column
original_goal_data=pd.DataFrame(kickstarters_2017.goal)
scaled_goal_data=minmax_scaling(original_goal_data,columns=['goal'])


# In[22]:


print('original data \nPreview :',original_goal_data.head())
print('Minimum Value: ',float(original_goal_data.min()),'\nMaximum Value : ',float(original_goal_data.max()))


# In[23]:


print('Scaled Data \nPreview : ',scaled_goal_data.head())
print('Maximum Value : ',float(scaled_goal_data.max()),'\nMinimum Value : ',float(scaled_goal_data.max()))


# In[24]:


# Normalization
index_of_positive_pledges=kickstarters_2017.usd_pledged_real > 0


# In[25]:


positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]


# In[26]:


normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='usd_pledged_real', index=positive_pledges.index)


# In[28]:


print('Original data\nPreview:\n', positive_pledges.head())
print('Minimum value:', float(positive_pledges.min()),
      '\nMaximum value:', float(positive_pledges.max()))


# In[29]:


print('\nNormalized data\nPreview:\n', normalized_pledges.head())
print('Minimum value:', float(normalized_pledges.min()),
      '\nMaximum value:', float(normalized_pledges.max()))


# In[30]:


#plotting
ax = sns.histplot(normalized_pledges, kde=True)
ax.set_title("Normalized data")
plt.show()


# In[31]:


index_pledges=kickstarters_2017.pledged > 0
positive=kickstarters_2017.pledged.loc[index_pledges]
normalized=pd.Series(stats.boxcox(positive)[0],
                    name='pledged', index=positive.index)


# In[32]:


print('Original Data\nPreview :',positive.head())
print('Maximum Value : ',float(positive.max()),
     '\nMinimum Value : ',float(positive.min()))


# In[33]:


print('Normalized Data \nPreview :',normalized.head())
print('Maximum Value : ',float(normalized.max()),
     '\nMinimum Value : ',float(normalized.min()))


# In[35]:


NO = sns.histplot(normalized, kde=True)
NO.set_title("Normalized Data")
plt.show()

