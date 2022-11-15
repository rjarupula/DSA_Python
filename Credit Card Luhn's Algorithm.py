#!/usr/bin/env python
# coding: utf-8

# # Luhn's Algorithm

# In[8]:


def credit_card(number):
    n = len(number)
    sum = 0
    i = 1
    while i <= n:
        if i % 2 ==0:
            sum += number[-i]*2
        else:
            sum += number[-i]
        i = i + 1
    if sum % 10 == 0:
        return True
    else:
        return False


# In[11]:


n = [3,5,4,2,9,7,4,6,9,3,0,4,7,9,5,3,2,5,8,6,5,3,2,1,0]
print(credit_card(n))


# In[ ]:




