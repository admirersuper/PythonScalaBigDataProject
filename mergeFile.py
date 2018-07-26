# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:41:34 2018
merge file
@author: ASUS
"""

w = open('taobao_data.txt','a',encoding = 'utf-8')
for i in range(1,63):
    f = open('taobao_data ('+str(i)+').txt','r',encoding = 'utf-8')
    data = str(f.read())
    w.write(data)
    print("merging file {}".format(i))
    f.close
w.close()

