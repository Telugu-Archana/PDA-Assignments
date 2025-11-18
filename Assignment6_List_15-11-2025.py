#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists
# 
# Create a list of the first 20 positive integers. Print the list.
# 
# ### Assignment 2: Accessing List Elements
# 
# Print the first, middle, and last elements of the list created in Assignment 1.
# 
# ### Assignment 3: List Slicing
# 
# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
# 
# ### Assignment 4: List Comprehensions
# 
# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
# 
# ### Assignment 5: Filtering Lists
# 
# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
# 
# ### Assignment 6: List Methods
# 
# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
# 
# ### Assignment 7: Nested Lists
# 
# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
# 
# ### Assignment 8: List of Dictionaries
# 
# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
# 
# ### Assignment 9: Matrix Transposition
# 
# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
# 
# ### Assignment 10: Flattening a Nested List
# 
# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.
# 
# ### Assignment 11: List Manipulation
# 
# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
# 
# ### Assignment 12: List Zipping
# 
# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
# 
# ### Assignment 13: List Reversal
# 
# Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
# 
# ### Assignment 14: List Rotation
# 
# Write a function that rotates a list by n positions. Print the original and rotated lists.
# 
# ### Assignment 15: List Intersection
# 
# Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.

# In[1]:


l=list(range(1,21))
print(l,type(l))


# In[2]:


print("first element",l[0])
print("middle element",l[(0+len(l)-1)//2])
print("last element",l[-1])


# In[8]:


print("first five element",l[0:6])
print("last element",l[15:20])
print("elements from index 5 to 15",l[5:16])


# In[10]:


l1=[x**2 for x in range(1,11)]
print(l1,type(l1))


# In[12]:


l2=[x for x in l if x%2==0]
print(l2,type(l2))


# In[20]:


l1=[10,2,3,12,15,20,3,9,18,22,10,25,23,10]
l1.sort()
print("ascending order",l1)
l1.sort(reverse=True)
print("descending order",l1)
print("after removing duplicates",list(set(l1)))


# In[21]:


mat=[[1,2,3],[4,5,6],[7,8,9]]
print("The list matrix is")
for val in mat:
    print(val)
print("The element in second row third column is",mat[1][2])


# In[53]:


l=[{'name':'Ram','score':65},{'name':'Sita','score':80},{'name':'Raavan','score':75}]
print(l,type(l))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]['score']<l[j]['score']:
            l[i],l[j]=l[j],l[i]
print(l,type(l))


# In[26]:


mat1=[[1,2,3],[4,5,6],[7,8,9]]
print(mat1,type(mat1))
print("The list matrix is")
for val in mat1:
    print(val)
mat2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(mat1)):
    for j in range(0,len(mat1)):
        mat2[j][i]=mat1[i][j]
print(mat2,type(mat2))
print("The transposed list matrix is")
for val in mat2:
    print(val)


# In[27]:


l1=[[1,2,3],[4,5,6],[7,8,9]]
print("original list is",l1,type(l1))
l2=[]
for val in l1:
    for v in val:
        l2.append(v)
print("flattened list is",l2,type(l2))


# In[28]:


l=list(range(1,11))
print("original list is",l,type(l))
l.remove(2)
l.remove(4)
l.remove(6)
l.insert(5,99)
print("modified list is",l,type(l))


# In[33]:


l1=[1,2,3,4]
print("first list is",l1,type(l1))
l2=[5,6,7,8]
print("second list is",l2,type(l2))
t=list(zip(l1,l2))
print("list of tuples is",t,type(t))


# In[38]:


l1=[10,30,14,25,36,17,28,49,56,24,12]
print("original list is",l1,type(l1))
l1.reverse()
print("reversed list is",l1,type(l1))


# In[54]:


l=[10,20,30,40,50,60,70,80,90]
print(l,type(l))
n=int(input("Enter number of positions n:"))
l1=l[n:]
l2=l[:n]
l3=l1+l2
print(l3,type(l3))


# In[39]:


l1=[1,2,3,4,5,6]
print("first list is",l1,type(l1))
l2=[4,5,6,7,8,9]
print("second list is",l2,type(l2))
l3=[]
for val in l1:
    if val in l1 and val in l2:
        l3.append(val)
print("resultant list is",l3,type(l3))


# In[ ]:




