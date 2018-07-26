# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:19:57 2018

@author: ASUS
"""

f = open("category",'r')

data = f.readlines()

for i in range(0,123):
    data[i] = data[i].replace("\n",'')
    print("\""+data[i]+"\",",end='')