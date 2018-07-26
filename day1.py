## -*- coding: utf-8 -*-
#'''
#Spyder Editor
#
#This is a temporary script file.
#'''
#
## exercise 1
#print("exercise 1:")
#week = [30,39,34,35,37,30,40]
#
#for i in range(0,6):
#    if i == 2:
#        print('周三：',end='')
#    print(week[i])
#
##exercise 2
#print("exercise 2:")
#dic = {'Mon':['30','Cloudy'],'Tue':['39','Sunny'],'Thu':['34','Cloudy'],'Wen':['35','Sunny'],'Fri':['37','Rain']}
#
#print(dic['Mon'][0],dic['Mon'][1])
#print(dic['Tue'][0],dic['Tue'][1])
#print(dic['Thu'][0],dic['Tue'][1])
#print(dic['Wen'][0],dic['Wen'][1])
#print(dic['Fri'][0],dic['Fri'][1])

#exercise 3
print('exercise4')

import urllib.request as r
import json

#def query(q):
#    #q = 'ji%27an'
#    data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+q+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
#    data = json.loads(data)   
#    print('description:'+data['weather'][0]['description'])
#    print('temp:'+str(data['main']['temp']))
#    print('pressure:'+str(data['main']['pressure']))
#
#q = input('请输入查询的城市名:')
#query(q)

#json:JavaScript Object Notation
#exercise 4

city = input('Please input the city name:')

data = r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
data = json.loads(data)

cnt = int(len(data['list'])/8)

templist = list()

print("Information about Everyday's 18:00:")
for i in range(0,cnt):
    print('day'+str(i+1)+':')
    print("Time:"+data['list'][2+i*8]['dt_txt'])
    print("Temperature:"+str(data['list'][2+i*8]['main']['temp']))
    templist.append(data['list'][2+i*8]['main']['temp'])
    print("Max Temperature:"+str(data['list'][2+i*8]['main']['temp_min']))
    print("Min Temperature:"+str(data['list'][2+i*8]['main']['temp_min']))
    print("Pressure:"+str(data['list'][2+i*8]['main']['pressure']))
    print("Description:"+data['list'][2+i*8]['weather'][0]['description'])
    print("Main:"+data['list'][2+i*8]['weather'][0]['main'])
    print('=======================================')

print("Varation of the temperature:")
for i in range(0,cnt-1):
    print(data['list'][2+i*8]['dt_txt']+":  "+str(data['list'][2+i*8]['main']['temp'])+'°C',end='')
    print('-'*int(data['list'][2+i*8]['main']['temp']))

print('=======================================')
print("The Sorted of the temperature:")
sorted(templist)
print(templist)



