# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:10:32 2018

@author: ASUS
"""

import urllib.request as r

data = r.urlopen("http://www.fengup.com/daxue/60593.html").read().decode("utf-8","ignore")

print(data)


