#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.4: Dictionaries
# Qno 1: Creating and Accessing Dictionaries
# 
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

# Qno 2: Accessing Dictionary Elements
# 
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

# Qno 3: Dictionary Methods
# 
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

# Qno 4: Iterating Over Dictionaries
# 
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.

# Qno 5: Dictionary Comprehensions
# 
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

# Qno 6: Merging Dictionaries
# 
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

# Qno 7: Nested Dictionaries
# 
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

# Qno 8: Dictionary of Lists
# 
# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.

# Qno 9: Dictionary of Tuples
# 
# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.

# Qno 10: Dictionary and List Conversion
# 
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.

# Qno 11: Dictionary Filtering
# 
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

# Qno 12: Dictionary Key and Value Transformation
# 
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.

# Qno 13: Default Dictionary
# 
# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.

# Qno 14: Counting with Dictionaries
# 
# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

# Qno 15: Dictionary and JSON
# 
# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.

# In[14]:


d={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
print(d,type(d))


# In[15]:


print(d[5])
print(d.get(5))
for key in d.keys():
    print(key)


# In[16]:


d[11]=121
del d[1]
print("The modified dictionary is",d,type(d))


# In[17]:


print("The key-value pairs in dictionary is")
for k,v in d.items():
    print(k,"=>",v)


# In[22]:


d={x:x**3 for x in range(1,11)}
print(d,type(d))


# In[23]:


d1={1:1,2:4,3:9,4:16,5:25}
print("first dictionary is",d1,type(d1))
d2={6:36,7:49,8:64,9:81,10:100}
print("second dictionary is",d2,type(d2))
d1.update(d2)
print("merged dictionary is",d1,type(d1))


# In[27]:


student={'name':'Ram','age':21,'grades':{'math':70,'science':80,'english':90}}
print(student,type(student))
print("nested list is",student['grades'])


# In[28]:


d={y:[y*x for x in range(1,6)] for y in range(1,6)}
print(d,type(d))


# In[29]:


d={x:(x,x**2) for x in range(1,6)}
print(d,type(d))


# In[33]:


d={x:x**2 for x in range(1,11)}
print(d,type(d))
l=[]
for item in d.items():
    l.append(item)
print("list of tuples is",l,type(l))


# In[38]:


d1={x:x**2 for x in range(1,11)}
print(d1,type(d1))
d2={}
for k,v in d1.items():
    if k%2==0:
        d2[k]=v
print("new dictionary is",d2,type(d2))


# In[40]:


d1={x:x**2 for x in range(1,6)}
print(d1,type(d1))
d2={}
for k,v in d1.items():
    d2[v]=k
print("new dictionary is",d2,type(d2))


# In[1]:


key=['a','b','c']
val=[]
d=dict.fromkeys(key,val)
print("default dictionary is",d,type(d))
val.append(1)
val.append(2)
print("resultant dictionary is",d,type(d))


# In[9]:


def countchar(s):
    d={}
    for char in s:
        d[char]=s.count(char)
    return d
s='mississippi'
print(countchar(s),type(countchar(s)))


# In[10]:


book={'title':'Ram chandra series','author':'Manish','year':2021,'genre':11}
print(book,type(book))


# In[ ]:




