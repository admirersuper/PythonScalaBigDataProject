# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:09:56 2018

@author: ASUS
"""
import jieba
from collections import Counter
#from pyecharts import WordCloud

f = open("title_sales.txt",'r',encoding = 'utf-8')
data = f.readlines()

cmts=[]

for d in data:
#    cmt.append(d.split(",")[0])
    c = d.split(",")[0]
    cmts.append(c)

title_after_cut = jieba.cut(str(cmts).replace(' ','')
        .replace('\'','').replace(',','').replace('-',''))
#print(cmts_after_cut)

wcs = " ".join(title_after_cut)
print(wcs)
#words_cnts = Counter(cmts_after_cut).most_common(100)
#print(words_cnts)
#
w = open("words_cut.txt",'w',encoding = 'utf-8')
w.write(wcs)
w.close()
f.close()
#words = []
#cnts = []
#
#for item in words_cnts:
#    words.append(item[0])
#    cnts.append(item[1])
#wordcloud = WordCloud(width=1320, height=620)
#wordcloud.add("", words, cnts, word_size_range=[20, 100],
#              shape='cardioid')
#wordcloud.render()
