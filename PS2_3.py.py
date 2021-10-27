#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


data = pd.read_csv("beijing_all_20190130.csv")


# In[16]:


data.head()


# In[20]:


new = data.dropna()
new.head()


# In[ ]:




