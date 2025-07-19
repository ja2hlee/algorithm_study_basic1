#!/usr/bin/env python
# coding: utf-8

# In[25]:


# 분해합

N = int(input())
x = 0

while x < N:
    str_x = str(x)
    add= 0
    for i in range(len(str_x)):
        add += int(str_x[i])
    if x+add == N:
        break
    else:
        x+=1
        
if x != N:    
    print(x)    
else: #생성자가 존재하지 않는 경우
    print(0)    

