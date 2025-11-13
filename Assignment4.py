#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.2: Tuples
# ### Assignment 1: Creating and Accessing Tuples
# 
# Create a tuple with the first 10 positive integers. Print the tuple.
# 
# ### Assignment 2: Accessing Tuple Elements
# 
# Print the first, middle, and last elements of the tuple created in Assignment 1.
# 
# ### Assignment 3: Tuple Slicing
# 
# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
# 
# ### Assignment 4: Nested Tuples
# 
# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
# 
# ### Assignment 5: Tuple Concatenation
# 
# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
# 
# ### Assignment 6: Tuple Methods
# 
# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
# 
# ### Assignment 7: Unpacking Tuples
# 
# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
# 
# ### Assignment 8: Tuple Conversion
# 
# Convert a list of the first 5 positive integers to a tuple. Print the tuple.
# 
# ### Assignment 9: Tuple of Tuples
# 
# Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
# 
# ### Assignment 10: Tuple and List
# 
# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
# 
# ### Assignment 11: Tuple and String
# 
# Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
# 
# ### Assignment 12: Tuple and Dictionary
# 
# Create a dictionary with tuple keys and integer values. Print the dictionary.
# 
# ### Assignment 13: Nested Tuple Iteration
# 
# Create a nested tuple and iterate over the elements, printing each element.
# 
# ### Assignment 14: Tuple and Set
# 
# Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
# 
# ### Assignment 15: Tuple Functions
# 
# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

# In[1]:


t=(1,2,3,4,5,6,7,8,9,10)
print(t,type(t))


# In[9]:


print("First element of tuple is",t[0])
print("Last element of tuple is",t[-1])
mid=(0+9)//2
print("Middle element of tuple is",t[mid])


# In[10]:


print("The first three elements of tuple are",t[0:3])
print("The last three elements of tuple are",t[7:10])
print("The tuple elements from index 2 to 5 are",t[2:6])


# In[12]:


mat=((1,2,3),(4,5,6),(7,8,9))
print("The tuple matrix is")
for val in mat:
    print(val)
print("The element in second row third column is",mat[1][2])


# In[13]:


t1=(1,2,3)
t2=(4,5,6)
print("First tuple is",t1)
print("Second tuple is",t2)
t3=t1+t2
print("The concatenation tuple is",t3)


# In[15]:


tup=10,20,40,10,30,20,10,40,60,50,60
print("The number of occurence of 10 is",tup.count(10))
print("The number of occurence of 20 is",tup.count(20))
print("The number of occurence of 30 is",tup.count(30))
print("The index of first occurence of 40 is",tup.count(40))
print("The index of first occurence of 50 is",tup.count(50))
print("The index of first occurence of 60 is",tup.count(60))


# In[16]:


t=1,2,3,4,5
print("tuple is",t,type(t))
a,b,c,d,e=t
print("The variables are",a,b,c,d,e)


# In[17]:


l=[1,2,3,4,5]
print("List is",l,type(l))
t=tuple(l)
print("Tuple is",t,type(t))


# In[21]:


t=((10,20,30),(40,50,60),(70,80,90))
print("The tuple is",t)
print("The tuple of tuples is")
for val in t:
    print(val)


# In[23]:


t1=1,2,3,4,5
print("The tuple is",t1,type(t1))
l1=list(t1)
print("tuple to list is",l1,type(l))
l1.append(6)
print("list after append of 6 is",l1,type(l))
t2=tuple(l1)
print("The resultant tuple is",t2,type(t2))


# In[26]:


t="P","Y","T","H","O","N"
print("The tuple is",t,type(t))
s=""
for char in t:
    s=s+char
print("Tuple elemnets into a string is",s,type(s))


# In[27]:


d={1:"a",2:"b",3:"c",4:"d"}
print(d,type(d))


# In[29]:


t=(1,2,3),(4,5,6),(7,8,9)
print(t,type(t))
for val in t:
    for element in val:
        print(element)


# In[33]:


t1=1,4,5,4,9,5,7,1,5,6,7,2,5
print(t1,type(t))
s=set(t1)
print("The resultant set is",s,type(s))


# In[36]:


t1=1,4,5,4,9,5,7,1,5,6,0,7,2,5
t2=(min(t1),max(t1),sum(t1))
print(t2)
for val in t2:
    print(val)


# In[ ]:




