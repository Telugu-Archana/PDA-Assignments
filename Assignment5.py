#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.3: Sets
# ### Assignment 1: Creating and Accessing Sets
# 
# Create a set with the first 10 positive integers. Print the set.
# 
# ### Assignment 2: Adding and Removing Elements
# 
# Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
# 
# ### Assignment 3: Set Operations
# 
# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
# 
# ### Assignment 4: Set Comprehensions
# 
# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.
# 
# ### Assignment 5: Filtering Sets
# 
# Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
# 
# ### Assignment 6: Set Methods
# 
# Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.
# 
# ### Assignment 7: Subsets and Supersets
# 
# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
# 
# ### Assignment 8: Frozenset
# 
# Create a frozenset with the first 5 positive integers. Print the frozenset.
# 
# ### Assignment 9: Set and List Conversion
# 
# Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
# 
# ### Assignment 10: Set and Dictionary
# 
# Create a dictionary with set keys and integer values. Print the dictionary.
# 
# ### Assignment 11: Iterating Over Sets
# 
# Create a set and iterate over the elements, printing each element.
# 
# ### Assignment 12: Removing Elements from Sets
# 
# Create a set and remove elements from it until it is empty. Print the set after each removal.
# 
# ### Assignment 13: Set Symmetric Difference Update
# 
# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
# 
# ### Assignment 14: Set Membership Testing
# 
# Create a set and test if certain elements are present in the set. Print the results.
# 
# ### Assignment 15: Set of Tuples
# 
# Create a set containing tuples, where each tuple contains two elements. Print the set.

# In[4]:


s={1,2,3,4,5,6,7,8,9,10}
print(s,type(s))


# In[5]:


s.add(11)
s.remove(1)
print(s,type(s))


# In[6]:


s1={1,2,3,4,5}
s2={2,4,6,8,10}
print(s1,type(s1))
print(s2,type(s2))
s3=s1.union(s2)
print("The union operation of two sets is",s3)
s4=s1.intersection(s2)
print("The intersection operation of two sets is",s4)
s5=s1.difference(s2)
print("The difference operation of two sets is",s5)
s6=s1.symmetric_difference(s2)
print("The symmetric difference operation of two sets is",s6)


# In[7]:


s1={1,2,3,4,5,6,7,8,9,10}
print(s1,type(s1))
s2={val**2 for val in s1}
print(s2,type(s2))


# In[8]:


s1={val for val in s if val%2==0 }
print(s1,type(s1))


# In[9]:


s1={40,10,20,30,60,40,10,30,50,10,70}
print(s1,type(s1))
s1.remove(10)
s1.remove(30)
s1.remove(40)
print(s1,type(s1))


# In[10]:


s1={1,2,3,4,5}
s2={1,2,3}
print(s1,type(s1))
print(s2,type(s2))
print("Is second set is subset of first set?",s2.issubset(s1))
print("Is first set is superset of second set?",s1.issuperset(s2))


# In[3]:


fs=frozenset({1,2,3,4,5})
print("The frozen set is",fs,type(fs))


# In[11]:


s1={1,2,3,4,5}
print(s1,type(s1))
l1=list(s1)
l1.append(6)
s2=set(l1)
print(s2,type(s2))


# In[18]:


d={frozenset({1,4}):'a',frozenset({2,3,5}):'b'}
print(d,type(d))


# In[12]:


s={15,"python",True,3-2j,23.46}
for val in s:
    print(val,type(val))


# In[13]:


s={15,"python",True,3-2j,23.46}
print(s,type(s))
s.pop()
print(s,type(s))
s.pop()
print(s,type(s))
s.pop()
print(s,type(s))
s.pop()
print(s,type(s))
s.pop()
print(s,type(s))


# In[14]:


s1={1,2,3,4,5}
print(s1,type(s1))
s2={4,5,6,7,8}
print(s2,type(s2))
s1=s1.symmetric_difference(s2)
print("Symmetric difference of two sets is",s1,type(s1))


# In[15]:


s={15,"python",True,3-2j,23.46}
print(15 in s)
print(20 in s)
print(True in s)
print(False in s)


# In[16]:


s={(1,2),(3,4),(5,6),(7,8)}
print(s,type(s))


# In[ ]:




