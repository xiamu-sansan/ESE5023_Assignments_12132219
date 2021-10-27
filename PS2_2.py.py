#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


wind = pd.read_csv("2281305.csv")


# In[4]:


wind.head()


# In[11]:


df=wind["WND"].str.split(pat=",",expand=True)
df.head()


# In[12]:


df["date"]=wind[1]
df.head()

