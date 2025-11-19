#!/usr/bin/env python
# coding: utf-8

# # Module 2: Control Flow Assignments
# Lesson 2.1: Conditional Statements
# Assignment 1: Simple if Statement
# Write a program that asks the user to input a number and prints whether the
# number is positive.
# Assignment 2: if-else Statement
# Write a program that asks the user to input a number and prints whether the
# number is positive or negative.
# Assignment 3: if-elif-else Statement
# Write a program that asks the user to input a number and prints whether the
# number is positive, negative, or zero.
# Assignment 4: Nested if Statement
# Write a program that asks the user to input a number and prints whether the
# number is positive and even, positive and odd, or negative.
# Lesson 2.2: Loops
# Assignment 5: for Loop
# Write a program that prints all the numbers from 1 to 10 using a for loop.
# Assignment 6: while Loop
# Write a program that prints all the numbers from 1 to 10 using a while loop.
# Assignment 7: Nested Loops
# Write a program that prints a 5x5 grid of asterisks (*) using nested loops.
# Assignment 8: break Statement
# Write a program that asks the user to input numbers until they input 0. The
# program should print the sum of all the input numbers.
# Assignment 9: continue Statement
# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop
# and continue statement.
# Assignment 10: pass Statement
# Write a program that defines an empty function using the pass statement.
# Assignment 11: Combining Loops and Conditionals
# Write a program that asks the user to input a number and prints all the even
# numbers from 1 to that number using a for loop.
# Assignment 12: Factorial Calculation
# Write a program that calculates the factorial of a number input by the user using a
# while loop.
# Assignment 13: Sum of Digits
# Write a program that calculates the sum of the digits of a number input by the user
# using a while loop.
# Assignment 14: Prime Number Check
# Write a program that checks if a number input by the user is a prime number using
# a for loop.
# Assignment 15: Fibonacci Sequence
# Write a program that prints the first n Fibonacci numbers, where n is input by the
# user.

# In[3]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")


# In[5]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")


# In[6]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")


# In[7]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
elif num<0:
    print("number is negative")


# In[8]:


for n in range(1,11):
    print(n)


# In[10]:


n=1
while(n<=10):
    print(n)
    n+=1


# In[11]:


for _ in range(1,6):
    for _ in range(1,6):
        print('*',end='')
    print()


# In[16]:


sum=0
while(True):
    n=eval(input("Enter a number: "))
    sum+=n
    if n==0:
        break
print(sum)


# In[17]:


for n in range(1,11):
    if n==5:
        continue
    print(n)


# In[19]:


def emptyfun():
    pass


# In[27]:


num=int(input("Enter a number: "))
for n in range(1,num+1):
    if n%2==0:
        print(n)


# In[26]:


n=int(input("Enter a number: "))
i=1
prod=1
while(i<=n):
    prod*=i
    i+=1
print("factorial of",n,"is",prod)


# In[28]:


n=int(input("Enter a number: "))
sum=0
while(n>0):
    r=n%10
    sum+=r
    n=n//10
print("sum of digits is",sum)


# In[30]:


n=int(input("Enter a number: "))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count==0:
    print("number is prime")
else:
    print("number is not prime")


# In[31]:


f=0
s=1
n=int(input("Enter a number: "))
count=0
while(count<n):
    print(f)
    sum=f+s
    f=s
    s=sum
    count+=1


# In[ ]:




