import urllib.request as r
#大学主页URL
#http://www.gaokaopai.com/daxue.html
#请求URL
url = 'http://www.gaokaopai.com/university-ajaxGetMajor.html'
#请求头
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}
#请求查询字符串，id:学校id type:1文科 2理科 city:招生地代码 state:1为请求成功
#可以将字符串写在一个json文件中然后再在文件中读取and查询

#f = open('all_school.txt','r',encoding='utf-8')
#data = f.readlines()
#for i in range(0,len(data)):
#    ls = data[i].split(' ')
#    ls[2] = ls[2].replace('http://www.gaokaopai.com/daxue-zhaosheng-','').replace('.html','')
#    #print(ls[2])
#    f1 = open("all_school_id.txt",'a+',encoding='utf-8')
#    f1.write(ls[0]+' '+ls[2])

#id已经存储在all_school_id.txt中
#dis = (11,12,13,14,15,21,22,23,31
#       ,32,33,34,35,36,37,
#       41,42,43,44,45,46,
#       50,51,52,53,54,61,62,63,64,65)
f = open('all_school.txt','r',encoding='utf-8')
idls = f.readlines()

w2 = open('34_2.txt','a+',encoding='utf-8')
cnt2 = 1
f2 = 0
for i in range(0,len(idls)):
    sid = idls[i].split('-jianjie-')[1].replace('.html','')
    for j in [34]:
        for t in [2]:
            try:
                query = 'id='+str(sid)+'&type='+str(t)+'&city='+str(j)+'&state=1'
                #请求命令，data要进行编码
                req = r.Request(url,data=query.encode('utf-8'),headers=header)
                #获取请求数据
                data = r.urlopen(req).read().decode('utf-8','igonre')
                #将获取数据中的Unicode转为中文
#                data = data.encode('utf-8').decode('unicode_escape')
                if data[0]!="{":
                    print("error_1")
                else:
                    w2.write(data+'\n')
                    print(cnt2)
                    cnt2 += 1
            except:
                    print("error_2")

w2.close()
f2 = 1
print("finish2")

f.close()