# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:16:44 2019

@author: Administrator
"""

import random 
import string
a = list(string.ascii_letters)
for i in range(200):
    c = []
    random.shuffle(a)
    b = ''.join(a)
    c.append(b[:8])
    print(c)
    
