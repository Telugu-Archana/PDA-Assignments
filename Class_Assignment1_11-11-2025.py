#!/usr/bin/env python
# coding: utf-8

# In[1]:


l1=[10,11,12,13]
l2=[]
for ind,val in enumerate(l1):
    value=val+10
    l2.append(value)
print(l2)


# In[2]:


l1=[10,11,23,45,78,90,42,41]
l2=[]
for ind,val in enumerate(l1):
    if val>=40:
        l2.append(val)
print(l2)


# In[16]:


l1=[10,11,12,13]
l2=[5,6,7,8,9]
l3=[]
for ind,val in enumerate(l1):
    s=l1[ind]+l2[ind]
    l3.append(s)
print(l3)


# In[18]:


l1=[10,20,15,45,89,90,11,34]
l2=[]
l2.append(l1[0])
l2.append(l1[1])
l2.append(l1[5])
l2.append(l1[7])
print(l2)


# In[ ]:




