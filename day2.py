#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:25:21 2018

@author: admirer
"""

import urllib.request as r
from urllib import parse
import json

#exercise 5

#city = input('Please input the city name:\n')
#
#data = r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
#data = json.loads(data)
#
#cnt = int(len(data['list'])/8)
#
#def Msg(city,cnt,data):
#    print("Information about {} Everyday's 18:00:".format(city))
#    for i in range(0,cnt-1):
#        print('day'+str(i+1)+':')
#        print("Time:"+data['list'][2+i*8]['dt_txt'])
#        print("Temperature:"+str(data['list'][2+i*8]['main']['temp']))
#        print("Max Temperature:"+str(data['list'][2+i*8]['main']['temp_min']))
#        print("Min Temperature:"+str(data['list'][2+i*8]['main']['temp_min']))
#        print("Pressure:"+str(data['list'][2+i*8]['main']['pressure']))
#        print("Description:"+data['list'][2+i*8]['weather'][0]['description'])
#        print("Main:"+data['list'][2+i*8]['weather'][0]['main'])
#        print('=======================================')
#
#Msg(city,cnt,data)
#
#def Var(char,city,cnt,data):
#    print("Varation of the temperature:")
#    for i in range(0,cnt-1):
#        print(data['list'][2+i*8]['dt_txt']+":  "+str(data['list'][2+i*8]['main']['temp'])+'°C',end='')
#        print(char*int(data['list'][2+i*8]['main']['temp']))
#    return True
#
#Var('热',city,cnt,data)


##exercise 6
##https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
#
#query = input('Please what you want to query:\n')
#query = parse.quote(query)
#
#def queryGoods(query):
#    url = 'https://s.taobao.com/search?q='+query+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
#    data = r.urlopen(url).read().decode('utf-8','ignore')
#    data = json.loads(data)
#    
#    print('Here are the information you want')
#    print('----------------------------------------')
#    
#    cnt = len(data['mods']['itemlist']['data']['auctions'])
#    
#    prlist = list()
#    salist = list()
#    zfeelist = list()
#    
#    for i in range(0,cnt):
#        rtitle = data['mods']['itemlist']['data']['auctions'][i]['raw_title']    
#        vprice = data['mods']['itemlist']['data']['auctions'][i]['view_price']
#        prlist.append(float(vprice))
#        loc = data['mods']['itemlist']['data']['auctions'][i]['item_loc']
#        sales = data['mods']['itemlist']['data']['auctions'][i]['view_sales']
#        sales = int(sales.replace('人付款',''))
#        salist.append(sales)
#        nick = data['mods']['itemlist']['data']['auctions'][i]['nick']
#        view_fee = data['mods']['itemlist']['data']['auctions'][i]['view_fee'] #str
#        if int(float(view_fee)) == 0:
#            zfeelist.append(data['mods']['itemlist']['data']['auctions'][i])
#        print('\033[1;31;47m','¥'+str(vprice)+'\t\t\t\t'+str(sales))
#        print('\033[1;35;47m',rtitle) 
#        print('\033[0m')
#        print('店家:'+nick+'\t\t\t\t'+loc)
#        print('------------------------------------------------------')
#        
#        if (i+1)%4==0:
#            print('======================第'+str((i+1)//4)+'行=========================')
#    
#    print('The sorted rank of Price')
#    prlist.sort(reverse = True)
#    print(prlist)
#    print('The sorted rank of Sales')
#    salist.sort(reverse = True)
#    print(salist)
#    #https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=price-desc&ajax=true
#    
#    print('------------------------------------------------------')
#    print('------------------------------------------------------')
#    print('\nThe Free Fee product are:')
#    for i in range(0,len(zfeelist)-1):
#        rtitle = data['mods']['itemlist']['data']['auctions'][i]['raw_title']    
#        vprice = data['mods']['itemlist']['data']['auctions'][i]['view_price']
#        loc = data['mods']['itemlist']['data']['auctions'][i]['item_loc']
#        sales = data['mods']['itemlist']['data']['auctions'][i]['view_sales']
#        nick = data['mods']['itemlist']['data']['auctions'][i]['nick']
#        view_fee = data['mods']['itemlist']['data']['auctions'][i]['view_fee']
#        print('\033[1;31;47m','¥'+str(vprice)+'\t\t\t\t'+str(sales)+'人付款')
#        print('\033[1;35;47m',rtitle)
#        print('\033[0m')
#        print('店家:'+nick+'\t\t\t\t'+loc)
#        print('------------------------------------------------------')
#
#queryGoods(query)

##exercise 7
#def WeatherReminder():
#    city = input('Please input the city name:')
#    data = r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
#    data = json.loads(data)
#    cnt = int(len(data['list'])/8)
#    
#    print("Information about Everyday's 18:00:")
#    for i in range(0,cnt):
#        print('day'+str(i+1)+':')
#        print("Time:"+data['list'][2+i*8]['dt_txt'])
#        temp = data['list'][2+i*8]['main']['temp']
#        print("今天的温度是:"+str(temp))
##        print("Main:"+data['list'][2+i*8]['weather'][0]['main'])
#        if temp >= 40:
#            print('温度极高，防止中暑')
#        elif temp >= 30:
#            print('温度较高，请注意防晒')
#        elif temp >= 20:
#            print('温度较舒适，穿衣适中')
#        elif temp >= 10:
#            print('温度较寒冷，注意穿衣')
#        elif temp >=0:
#            print('温度较低，注意保暖')
#        else:
#            print('温都极低，请待在室内取暖')
#        desc = data['list'][2+i*8]['weather'][0]['description']
#        print("今天的天气情况是:"+desc)
#        if '晴' in desc:
#            print('天晴，阳光高照')
#        elif '大雨' in desc:
#            print('雨势较大，注意躲雨')
#        elif '小雨' in desc:
#            print('出门注意带伞')
#        elif '阴' in desc:
#            print('天气阴天，适合外出')
#        elif '雾' in desc :
#            print('起雾，开车小心追尾')
#        print('=======================================')
#        
#WeatherReminder()

def queryGoods():
    query = input('Please what you want to query:\n')
    query = parse.quote(query)
    url = 'https://s.taobao.com/search?q='+query+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
    data = r.urlopen(url).read().decode('utf-8','ignore')
    data = json.loads(data)
    
    print('Here are the information you want')
    print('----------------------------------------')
    
    cnt = len(data['mods']['itemlist']['data']['auctions'])
    
    
    for i in range(0,cnt):
        rtitle = data['mods']['itemlist']['data']['auctions'][i]['raw_title']    
        vprice = data['mods']['itemlist']['data']['auctions'][i]['view_price']
        if float(vprice)>=800:
            print('下个月又要还花呗了嘛TnT')
        elif float(vprice)>=500:
            print('还是有点小贵，再考虑下嘛')
        else:
            print('价格可以接受~')
        loc = data['mods']['itemlist']['data']['auctions'][i]['item_loc']
        sales = data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        sales = int(sales.replace('人付款',''))
        nick = data['mods']['itemlist']['data']['auctions'][i]['nick']
        view_fee = data['mods']['itemlist']['data']['auctions'][i]['view_fee'] #str
        if int(float(view_fee)) == 0:
            print('此商品包邮哦')
        print('¥'+str(vprice)+'\t\t\t\t'+str(sales))
        print(rtitle) 
        print('店家:'+nick+'\t\t\t\t'+loc)
        print('------------------------------------------------------')
        
        if (i+1)%4==0:
            print('======================第'+str((i+1)//4)+'行=========================')

queryGoods()