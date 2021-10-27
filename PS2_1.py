#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


Sig_Eqs = pd.read_csv("earthquakes-2021-10-25_20-36-22_+0800.tsv", sep='\t')


# In[4]:


Sig_Eqs.info()


# In[5]:


Sig_Eqs.head()


# In[6]:


Sig_Eqs.groupby("Country")["Total Deaths"].sum().sort_values(ascending = False)[0:10]


# In[7]:


temp = Sig_Eqs[Sig_Eqs["Mag"]>6.0]
temp.head()


# In[10]:


temp.groupby("Year")["Mag"].count()


# In[27]:


#trend：1500年数量以前保持平稳，之后突增。可能是因为近年来观测到的地震都有记录，而以前的可能有记录遗失。


# In[26]:


series_num=Sig_Eqs.groupby("Country")['Year'].count()


# In[112]:


def CountEq_LargestEq(country_name):
    series_num=Sig_Eqs.groupby("Country")['Year'].count()
    mag=Sig_Eqs[Sig_Eqs['Country']==country_name]["Mag"].max()
    y=Sig_Eqs[(Sig_Eqs['Country']==country_name)&(Sig_Eqs["Mag"]==mag)]["Year"].values
    m=Sig_Eqs[(Sig_Eqs['Country']==country_name)&(Sig_Eqs["Mag"]==mag)]["Mo"].values
    d=Sig_Eqs[(Sig_Eqs['Country']==country_name)&(Sig_Eqs["Mag"]==mag)]["Dy"].values
    y=np.concatenate((y,m))
    y=np.concatenate((y,d))
    return series_num[country_name],y

countrys=Sig_Eqs.groupby("Country")['Year'].count().index
for x in countrys:
    print(x,CountEq_LargestEq(x))
    


# In[107]:


Sig_Eqs[Sig_Eqs['Country']=='AFGHANISTAN']["Mag"].max()
y=Sig_Eqs[(Sig_Eqs['Country']=='AFGHANISTAN')&(Sig_Eqs["Mag"]==8.1)]["Year"].values
m=Sig_Eqs[(Sig_Eqs['Country']=='AFGHANISTAN')&(Sig_Eqs["Mag"]==8.1)]["Mo"].values
d=Sig_Eqs[(Sig_Eqs['Country']=='AFGHANISTAN')&(Sig_Eqs["Mag"]==8.1)]["Dy"].values
y=list(y)
m=list(m)
d=list(d)
y=y+m+d
y


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[78]:


countrys=Sig_Eqs.groupby("Country")['Year'].count().index
countrys


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


Sig_Eqs["Country"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




