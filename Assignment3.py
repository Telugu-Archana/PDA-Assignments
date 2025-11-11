#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.2: Python Basics
# ## Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)
# 

# ## 1. Syntax and Semantics
# 
# **Question 1:** Write a Python program to print "Hello, World!".

# In[1]:


# Your code here
print("Hello, World!")


# **Question 2:** Write a Python program that takes a user input and prints it.

# In[3]:


# Your code here
s=input("Enter: ")
print(s)


# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

# In[4]:


# Your code here
n=int(input("Enter a number: "))
if n>0:
    print("The number is positive")
elif n<0:
    print("The numner is negative")
else:
    print("The number is Zero")


# **Question 4:** Write a Python program to find the largest of three numbers.

# In[16]:


# Your code here
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print("greater value is a=",a)
elif b>c:
    print("greater value is b=",b)
else:
    print("greater value is c=",c)


# **Question 5:** Write a Python program to calculate the factorial of a number.

# In[17]:


# Your code here
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("The factorial of",n,"is",fact)


# ## 2. Variables and Data Types
# 
# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.

# In[7]:


# Your code here
a=10
b=12.34
c="Python"
d=False
print("Integer value",a,type(a))
print("Float value",b,type(b))
print("String value",c,type(c))
print("Boolean value",d,type(d))


# **Question 7:** Write a Python program to swap the values of two variables.

# In[8]:


# Your code here
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("a and b values before swapping are",a,"and",b)
a,b=b,a
print("a and b values after swapping are",a,"and",b)


# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.

# In[28]:


# Your code here
c=int(input("Enter the temperature in celsius: "))
f=(c*(9/5))+32
print("The temperature in fahrenheit is",f)


# **Question 9:** Write a Python program to concatenate two strings.

# In[9]:


# Your code here
a=input("Enter first String: ")
b=input("Enter second string: ")
print("The concatenation of two strings is",a+b)


# **Question 10:** Write a Python program to check if a variable is of a specific data type.

# In[10]:


# Your code here
n=3+9j
print(n,type(n))


# ## 3. Basic Operators (Arithmetic, Comparison, Logical)
# 
# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.

# In[11]:


# Your code here
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The addition of two numbers is",a+b)
print("The subtraction of two numbers is",a-b)
print("The multiplication of two numbers is",a*b)
print("The floor division of two numbers is",a/b)
print("The integer division of two numbers is",a//b)


# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

# In[13]:


# Your code here
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("a equal to b?",a==b)
print("a not equal to b?",a!=b)
print("a greater than b?",a>b)
print("a less than b?",a<b)


# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

# In[12]:


# Your code here
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The logical AND of two numbers is",a and b)
print("The logical OR of two numbers is",a or b)
print("The logical NOT of a is",not a)
print("The logical NOT of b is",not b)


# **Question 14:** Write a Python program to calculate the square of a number.

# In[6]:


# Your code here
num=int(input("Enter a number: "))
print(num**2)


# **Question 15:** Write a Python program to check if a number is even or odd.

# In[5]:


# Your code here
n=int(input("Enter a number: "))
if n%2==0:
    print("The number is Even")
else:
    print("The number is odd")


# **Question 16:** Write a Python program to find the sum of the first n natural numbers.

# In[15]:


# Your code here
n=int(input("Enter a number: "))
sum=(n*(n+1))//2
print(sum)


# **Question 17:** Write a Python program to check if a year is a leap year.

# In[25]:


# Your code here
year=int(input("Enter a year: "))
if year%100!=0 and year%4==0 or year%100==0 and year%400==0:
    print("The year",year,"is a leap year")
else:
    print("The year",year,"is not a leap year")


# **Question 18:** Write a Python program to reverse a string.

# In[17]:


# Your code here
s=input("Enter a string: ")
rev=''
for ind,val in enumerate(s):
    rev=val+rev
print("The reverse of",s,"is",rev)


# **Question 19:** Write a Python program to check if a string is a palindrome.

# In[16]:


# Your code here
s=input("Enter a string: ")
rev=''
for ind,val in enumerate(s):
    rev=val+rev
if s==rev:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")


# **Question 20:** Write a Python program to sort a list of numbers in ascending order.

# In[15]:


# Your code here
l1=[10,20,5,50,30,90,2,100]
print(l1)
l1.sort()
print(l1)


# In[ ]:




