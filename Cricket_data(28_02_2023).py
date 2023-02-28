#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


cric_data = np.loadtxt("cric.tsv", skiprows=1)
cric_data


# In[7]:


sachin = cric_data[:,1]
sachin


# In[8]:


dravid = cric_data[:,2]
dravid


# In[9]:


india = cric_data[:,3]
india


# In[10]:


def stats(a):
    median = np.median(a)
    mean = np.mean(a)
    return mean,median


# In[12]:


mean1,median1 = stats(sachin)
mean2,median2 = stats(dravid)
mean3,median3 = stats(india)
print("Sachin : Mean runs are {} and median runs are {}.".format(mean1,median1))
print("Dravid : Mean runs are {} and median runs are {}.".format(mean2,median2))
print("India : Mean runs are {} and median runs are {}.".format(mean3,median3))

