#!/usr/bin/env python
# coding: utf-8

# # Statistics
# 

# ## Mean,Median,Mode
# 

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    ##MEAN
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    mean = (sum/(len(arr)))
    print(round(mean,1))
    
    ##MEDIAN
    l = []
    for i in range(len(arr)):
        l.append(arr[i])
    
    l.sort()
    if len(l)%2 == 0:
        median = (l[int(len(l)/2)] + l[int(len(l)/2)-1])/2
    else:
        median = l[(int((len(l)+1)/2))]
    print(round(median,1))
    
    ##MODE
    mod = {}
    mod1 = {}
    for p in l:
        mod[p] = mod.get(p,0) + 1
    mode = 0
    if (max(mod.values()) != 1):
        for key,value in mod.items():
            if mod[key] == max(mod.values()):
                mod1[key] = mod1.get(key,0) + 1
                mode = min(mod1.keys())
                
    else:
        mode = min(mod.keys())
    print(mode)


# In[ ]:




