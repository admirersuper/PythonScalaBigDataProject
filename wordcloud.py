#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 07:50:31 2018

@author: admirer
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

f = open('words_space_cut.txt','r',encoding = 'utf-8')
word_space_split = f.read()

backgroud_Image = plt.imread("package_1.jpg")
stopwords = STOPWORDS.copy()
stopwords.add("包")
stopwords.add("包包")

wc = WordCloud(width=1024,height=768,background_color='white',
    mask=backgroud_Image,
    font_path="Deng.ttf",
    stopwords=stopwords,
    max_font_size=400,
    random_state=60,
    collocations=False)
wc.generate_from_text(word_space_split)
img_colors= ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴  
plt.show()
#保存结果到本地
wc.to_file("word_cloud_1.png")