#!/usr/bin/env python
# coding: utf-8

# # Binary Searching using Python

# ### Define a function that search element using Binary Search

# In[1]:


def binarySearch(item, my_list):
    status = False
    first = 0
    last = len(my_list) - 1
    
    while first <= last and not status:
        midnum = (first + last)// 2
        if my_list[midnum] == item:
            status = True
            return status
        elif my_list[midnum] > item:
            last = midnum -1
        elif my_list[midnum] < item:
            first = midnum +1
    return status


# In[8]:


my_list = [34,2,54,56,2,64,67,89,4,32,67,89,5,34,23]
my_list = set(my_list)
my_list = sorted(my_list)

item = int(input('Enter the key number to search in list. >> '))
print(binarySearch(item, my_list))


# In[ ]:




