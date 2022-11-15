#!/usr/bin/env python
# coding: utf-8

# ## Linear Search using Python Code

# In[4]:


def linearSearch(item, my_list):
    status = False
    point = 0
    
    while point < len(my_list)-1 and not status:
        if my_list[point] == item:
            status = True
            return status
        point += 1
    return status


# In[5]:


my_list = [2,12,45,3,67,90,56,34,6,87,8]
item = int(input('Enter the target Number >> '))

print(linearSearch(item, my_list))


# In[ ]:




