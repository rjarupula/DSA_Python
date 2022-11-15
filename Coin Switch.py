#!/usr/bin/env python
# coding: utf-8

# In[31]:


from collections import Counter
def coin_switch(n):
    coinline = []
    count = 0
    head = True
    tail = False
    for i in range(n):
        coinline.append(head)
    print(coinline)
    for i in range(1,n+1):
        k = i
        while k < n:
            coinline[k] = (not coinline[k])
            k = k + (i+1)
        #print(coinline)
    print(coinline)
    print()
    count = dict(Counter(coinline))
    return count



n = int(input('Enter list size >> '))
print(coin_switch(n))
            
        
        


# In[ ]:




