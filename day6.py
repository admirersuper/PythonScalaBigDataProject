# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:51:29 2018

@author: ASUS
"""
##exercise 10.1
#
#f = open('all_school.txt','r',encoding='utf-8')
#idls = f.readlines()
#
#print("school id are as follows:")
#for i in range(0,len(idls)):
#    sid = idls[i].split('-jianjie-')[1].split('.')[0]
#    f1 = open("all_id.txt",'a+',encoding='utf-8')
#    print(sid)
#    f1.write(sid+'\n')
#
#f1.close()
#f.close()

#exercise 10.2

f = open('city_info_xml.txt','r',encoding = 'utf-8')
cities = f.readlines()

w = open('city_id.txt','a',encoding = 'utf-8')
print("city id are as follows:")
for i in range(0,len(cities)):
    cid = cities[i].split(')\\">')[0][-2:]
    city = cities[i].split(')\\">')[1][0:2]
    print(cid+" "+city)
    w.write(cid+" "+city+'\n')
    
f.close()
w.close()