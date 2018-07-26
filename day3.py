#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:06:50 2018

@author: admirer
"""

#exercise 8
#import urllib.request as r;
#
#f = open('data3.txt','w',encoding = 'utf-8')
#
#for i in range(0,100):
#    url = 'https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E5%B9%BF%E4%B8%9C&s='+str(i*44)+'&ajax=true'
#    try:
#        data = r.urlopen(url).read().decode('utf-8','ignore')
#    except:
#        print('第'+str(i+1)+'页读取数据错误')    
#    f.write(data+'\n')
#    print('写文件中...第'+str(i+1)+'页')
#
#f.close()
#print('完成...')

#mergeFile
#f1 = open('data4.txt','r',encoding = 'utf-8')
#f2 = open('data5.txt','a',encoding = 'utf-8')
#data = str(f1.read())
#f2.write(data)
#print('合并完成')

#convertToCSV
f1 = open('dataMerge4.txt','r',encoding = 'utf-8')
data = f1.readlines() #列表
cF = open('dataMerge4.csv','w',encoding = 'utf-8')
for i in range(0,len(data)):
    cF.write(data[i])