# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:16:51 2018

@author: ASUS
"""
from pyecharts import Map

f = open("loc_sales.txt",'r',encoding='utf-8')
file = f.readlines()

attr = []
value = []

for i in range(0,len(file)):
    attr.append(file[i].split(',')[0])
    value.append(int(file[i].split(',')[1]))

map = Map("Map 结合 VisualMap 示例", width=1440, height=700)
map.add("", attr, value, maptype='china', is_visualmap=True,
        is_piecewise = True, visual_text_color='#000',
        is_label_show = True,is_label_emphasis = True,
        pieces = [
              {'min': 1000000,},#, 'color': 'red'
              {'min': 100000, 'max': 999999},#, 'color': 'orange'
              {'min': 10000, 'max': 99999},#, 'color': 'yellow'
              {'min': 1000, 'max': 9999},#, 'color': 'blue'
              {'min': 100, 'max': 999,},# 'color': 'green'
              {'max': 99,}# 'color': 'grey'
        ])
map.render()