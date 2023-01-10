#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Ved"
age = 22
print(name)
print(age)


# In[2]:


name = "ved"
age = 22

name = "aman"
age = 24
print(name)
print(age)


# In[20]:


## Arithmetic Operators
print(5 + 2)
print(5 - 2)
print(1 - 2)
print(5 * 2)
print(5 / 2)
print( 5 // 2)
print(5 % 2)
print(5 ** 2)


# In[4]:


#comparision operater
is_greater = 1 > 5
is_lesser = 1 < 5
# 1 <= 5
# 1 >= 5
is_not_equal = 1 != 5
is_equal = 1 == 5


# In[5]:


1>5


# In[6]:


1<5


# In[7]:


1==5


# In[8]:


1==1


# In[9]:


1!=5


# In[11]:


##.Logical Operators
# or -> (atleast one is true)
# and -> (both are true)
# not -> (reverses any value)
number = 2
print(number > 3)
print(number < 3)
print(not number > 3)
print(not number < 3)
print(number > 3 and number > 1)
print(number > 3 or number > 1)


# In[14]:


##If statements
age = 13
if age >= 18:
 print("you are an adult")
 print("you can vote")
elif age < 3:
 print("you are a child")
else:
 print("you are in school")
 print("thank you")


# In[15]:


##If statements
age = 21
if age >= 18:
 print("you are an adult")
 print("you can vote")
elif age < 3:
 print("you are a child")
else:
 print("you are in school")
 print("thank you")


# In[16]:


##If statements
age = 1
if age >= 18:
 print("you are an adult")
 print("you can vote")
elif age < 3:
 print("you are a child")
else:
 print("you are in school")
 print("thank you")


# In[17]:


##If statements
age = 0
if age >= 18:
 print("you are an adult")
 print("you can vote")
elif age < 3:
 print("you are a child")
else:
 print("you are in school")
 print("thank you")


# In[18]:


##If statements
age = -1
if age >= 18:
 print("you are an adult")
 print("you can vote")
elif age < 3:
 print("you are a child")
else:
 print("you are in school")
 print("thank you")


# In[23]:


##Let’s build a Calculator
#Our Calculator
first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("press keys for operator (+,-,*,/,%)")
operator = input("Enter operator : ")
if operator == "+":
 print(first + second)
elif operator == "-":
 print(first - second)
elif operator == "*":
 print(first * second)
elif operator == "/":
 print(first / second)
elif operator == "%":
 print(first % second)
else:
 print("Invalid Operation")


# In[27]:


# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()


# In[28]:


def calculator(num1, operator, num2):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    return "Invalid operator"

print(calculator(2, "+", 3))
print(calculator(5, "-", 1))
print(calculator(4, "*", 5))
print(calculator(9, "/", 3))
print(calculator(2, "$", 3))


# In[ ]:




