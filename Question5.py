#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[5]:


df = pd.read_csv("vaccinations_imputed.csv")


# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.info


# In[9]:


#Claculate the median daily vaccination number for each country 
vaccinations_median = df.groupby("country")["daily_vaccinations"].median()


# In[10]:


vaccinations_median


# In[13]:


top3_countries = vaccinations_median.sort_values(ascending=False).head(3)


# In[15]:


# Print the top 3 countries and their median daily vaccination numbers
print("Top 3 countries by median daily vaccinations:")
for country, vaccinations in top3_countries.iteritems():
    print(f"{country}: {vaccinations}")


# In[ ]:




