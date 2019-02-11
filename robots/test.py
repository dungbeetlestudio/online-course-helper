import random
import requests
import uiautomator2 as u2
import time
from pymongo import MongoClient

client = MongoClient('dungbeetles.xyz',35778)#建立MongoDB数据库连接
db=client['data_gather']#连接所需数据库,test为数据库名
collection=db['全民k歌']#连接所用集合，也就是我们通常所说的表，test为表名
collection.insert({'kid':'123456','name':12,'gender':'0'})#向集合中插入数据
#collection.update({'Name':'Tom'},{'Name':'Tom','age':18})#更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
#collection.remove()#删除集合collection中的所有数据
#collection.drop()#删除集合collection

with open('gps.txt','a') as f:
    num = 1
    d = u2.connect('emulator-5556')
    d(text="动态").click()
    d(resourceId="com.tencent.karaoke:id/d_t").click(offset=(0.65,0.5))
    while True:
        time.sleep(2)
        rf0 = random.uniform(81.000000,125.999999)
        rf1 = random.uniform(44.000000,112.999999)
        d.shell('setprop call.locate %.6f,%.6f',rf0,rf1)   # changes gps

        if d(resourceId="com.tencent.karaoke:id/u9").exists:
            d(resourceId="com.tencent.karaoke:id/u9").click()

        d(resourceId="com.tencent.karaoke:id/c9v").click()
        kid = d(resourceId="com.tencent.karaoke:id/ddb").get_text()
        d.press('back')
        rs = requests.get('https://win.60rt.com:6088/kidExists',{'kid':kid})
        data ='%d %s (%.6f,%.6f) %s %s'%(num,time.strftime("%H:%M:%S", time.localtime()),rf0,rf1,kid,'存在' if rs.text == '1' else '不存在')
        print(data)
        f.write(data + '\n')
        d(text="动态").click()
        num+=1

client.close()