# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:55:17 2018

@author: ASUS
"""

f = open('all_school_id.txt','r',encoding='utf-8')
idls = f.readlines()
for i in range(0,len(idls)):
    sid = idls[i].split(' ')[1].rstrip()
    if sid.isnumeric()==False:
        print(i)
        break
    else:
        print(idls[i])