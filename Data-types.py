#!/usr/bin/env python
# coding: utf-8

# In[27]:


import datetime


# In[3]:


myname = "Harishkumar"
_myname = ""

# Snakecase
my_name="Harish"

#camelCase
myName="Harishkumar"

#TitleCase
MyName = "Harish"


# In[4]:


print(myname)


# In[8]:


# Data Types
# 1. Primithive Datatyps
# 2. Non-Primithive Datatypes / Scallar data types


# In[ ]:


# 1. Primithive Datatyps
#     String
#     Int
#     Float
#     Doubul
#     Bool
#     Date
#     time
#     datetime


# In[9]:


# STring
student_name = "Harishkumar"
student_email = "harish@gmail.com"
stu_contact_address="#301, 401-24-2LA, Hyderabad"

# Int
stu_age = 34

#float
stu_height = 5.9

#Double
stu_score= 162.256478965556

# Bool
is_active = True
is_valentear=False


# In[13]:


print("Name: %s" % student_name)


# In[16]:


print(f"Name: {student_name}")
print(f"Email: {student_email}")


# In[21]:


print(f"Name: {student_name}\nEmail: {student_email}\n\t{student_email}")


# In[22]:


print("Name: {}, and age{}".format(student_name, stu_age))


# In[29]:


tday = datetime.datetime.now()


# In[30]:


tday


# In[31]:


str(tday)


# In[32]:


dob = "1987-9-2"


# In[33]:


type(dob)


# In[34]:


dt_dob = datetime.datetime(1987,9,2)


# In[39]:


dt_dob


# In[36]:


str(dt_dob)


# In[46]:


y_dob = dt_dob.strftime("%y")
print(y_dob)


# In[49]:


m_dob = dt_dob.strftime("%mmm")
print(m_dob)


# In[ ]:

'''
Sr.No.	Directives & Description
1	
get_ipython().run_line_magic('A', '')


Full Weekday name

2	
get_ipython().run_line_magic('B', '')

Full Month Name

3	
get_ipython().run_line_magic('d', '')

Day of the month (1 to 31)

4	
get_ipython().run_line_magic('S', '')

Second

5	
get_ipython().run_line_magic('G', '')

4 digit Year, corresponding to ISO week number

6	
get_ipython().run_line_magic('m', '')

Month (1 to 12)

7	
get_ipython().run_line_magic('M', '')

Minute

8	
get_ipython().run_line_magic('T', '')

Current time, equal to %H:%M:%S

9	
get_ipython().run_line_magic('W', '')

Week number of the current year, starting with the first Monday as the first day of the first week

10	
get_ipython().run_line_magic('w', '')

Day of the week as a decimal, Sunday=0

11	
get_ipython().run_line_magic('Y', '')

Year including the century

12	
get_ipython().run_line_magic('Z', 'or %z')

Time zone or name or abbreviation

'''
# In[50]:


dt_dob.strftime("%B")


# In[51]:


dt_dob.strftime("%B %d, %Y")


# In[54]:


dt_dob.strftime("%M")


# In[56]:


dt_dob.strftime("%z")


# In[ ]:




