# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:02:21 2018

@author: ASUS
"""

import urllib.request as r;

#ad = open('taobao_admirer.txt','r',encoding='utf-8')
urls = ['https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E8%A5%BF%E8%97%8F',
        'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E6%96%B0%E7%96%86',
        'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E5%86%85%E8%92%99%E5%8F%A4',
        'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E9%BB%91%E9%BE%99%E6%B1%9F']

ex = 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E9%95%BF%E6%98%A5'
city = ['xizang','xinjiang','neimenggu','helongjiang']

cnt = 0
for u in urls:
    f = open('taobao_data_'+city[cnt]+'.txt','a',encoding = 'utf-8')
    for i in range(0,100):
        try:
            url = u+'&s='+str(i*44)+'&ajax=true'
            data = r.urlopen(url).read().decode('utf-8','ignore')
        except:
            print(city[cnt]+':第'+str(i+1)+'页读取数据错误')
        f.write(data+'\n')
        print(city[cnt]+':写文件中...第'+str(i+1)+'页')
    cnt += 1
    
f.close()
print('完成...')