from lianzhong_api import main as ocr
import gender
import subprocess
import json
import requests
import random
import traceback
import requests
import time
import os 
import logging

# the following is defined function
def run(cf, d):
    d(text="发现").click()
    d(resourceId="com.tencent.karaoke:id/c4n").click() # 点击搜索框
    d(resourceId="com.tencent.karaoke:id/bi5").click()
    for z in range(cf['numConf'][3]): #关注人数限制
        while True:
            try:
                kid = requests.get('https://win.60rt.com:6088/getOne').text #获取一个用户
                print('%s:kid:%s'%(cf['account'],kid))
                break
            except:time.sleep(5)
        d(resourceId="com.tencent.karaoke:id/bi5").set_text(kid) # 搜索种子用户
        d.send_action('search')
        d(resourceId="com.tencent.karaoke:id/cxs").click() #点击头像\

        if d(resourceId="com.tencent.karaoke:id/b99").get_text() == '已关注': 
            d.press('back')
            continue
        d(resourceId="com.tencent.karaoke:id/b99").click() #关注
        name = d(resourceId="com.tencent.karaoke:id/c9v").get_text() # 获取名字
        if '已关注' != d(resourceId="com.tencent.karaoke:id/b99").get_text():
            logging.info('关注失败，功能受限')
            cf['status_of_sent'] = "关注失败，功能受限" # 设置私信状态 
            cf['status_of_account'] = -4
            return
        d.press('back')
        print('%s:关注:%d-%d'%(cf['account'],z + 1,cf['numConf'][3]))
        cf['attentions'][kid] = {'name':name,'time_of_attention':int(time.time()) * 1000}   
    # female = 0
    # while True: # favor them
    #     dv(text='关注').wait()
    #     time.sleep(2)
    #     count_items = dv(resourceId="com.tencent.karaoke:id/c9v").count # fans and name
    #     # img = dv.screenshot()   # headportrait
    #     cur_attention = cf['numConf'][2]
    #     name=''
    #     for i in range(1,count_items):
    #         o = dv(resourceId="com.tencent.karaoke:id/c9v", instance=i)
    #         name = o.get_text()
    #         logging.info(name.encode('gbk','replace').decode('gbk'))
    #         if names_of_fans.get(name,None):continue
    #         names_of_fans[name] = 1
    #         o.click()
    #         dv(text='正在加载').wait_gone()
    #         if not dv(text="资料").exists:
    #             logging.info('查看附加信息')
    #             if not dv(resourceId="com.tencent.karaoke:id/bx6").exists:
    #                 dv.press('back')
    #                 continue
    #             dv(resourceId="com.tencent.karaoke:id/bx6").click() # has additional
    #         dv(resourceId="com.tencent.karaoke:id/bwv").wait()  # judge gender
    #         time.sleep(2)
    #         img = dv.screenshot()   # headportrait
    #         rect = dv(resourceId="com.tencent.karaoke:id/bwv").info['bounds']
    #         img = img.crop((rect['left'], rect['top'], rect['right'], rect['bottom']))  # 图像裁剪
    #         logging.info('关注限制：%d %d'%(cur_attention,cf['numConf'][3]))  #关注多少个人之后切换账号
    #         print('关注%d,限制:%d'%(cur_attention,cf['numConf'][3]))
    #         if gender.is_male(img):
    #             if not dv(text=u"已关注").exists:
    #                 # tick = time.time()
    #                 # print('ten times:%d' % len(ten_times))
    #                 # if len(ten_times) is 9:
    #                 #     sleep = tick - ten_times[0]
    #                 #     print('sleep:%d' % sleep)
    #                 #     if sleep < (5 * 60):
    #                 #         sleep = 5 * 60 - sleep
    #                 #         print("超过频率，等待%d秒"%sleep)
    #                 #         time.sleep(sleep)
    #                 #     del ten_times[0]
    #                 # ten_times.append(tick)
    #                 kid = dv(resourceId="com.tencent.karaoke:id/ddb").get_text() # 获取id
    #                 while True:
    #                     try:
    #                         kid_is_exists = int(requests.get('https://win.60rt.com:6088/kidExists?kid=%s'%kid).text)
    #                         print('kid is %s'%kid_is_exists)
    #                         break
    #                     except: 
    #                         traceback.print_exc()
    #                 if kid_is_exists > 0:
    #                     dv.press('back')
    #                     continue
    #                 dv(resourceId="com.tencent.karaoke:id/b99").click() # 关注
    #                 time.sleep(3)
    #                 if '已关注' != dv(resourceId="com.tencent.karaoke:id/b99").get_text():
    #                     logging.info('关注失败，功能受限')
    #                     cf['status_of_sent'] = "关注失败，功能受限" # 设置私信状态 
    #                     cf['status_of_account'] = -4
    #                     return
    #                 cf['attentions'][kid] = {'name':name,'time_of_attention':int(time.time()) * 1000}   
    #                 cf['numConf'][3] -= 1   # condition of 
    #                 cur_attention -= 1
    #             female = 0
    #         else:
    #             dv.toast.show("非目标性别")
    #         dv.press('back') # back
    #         if cf['numConf'][3] == 0 or cur_attention == 0: break
    #     if cf['numConf'][3] == 0 or cur_attention == 0: break
    #     if dv(text=u'已加载全部').exists: break
    #     dv(text=name).drag_to(text=u'粉丝')# next page
    # dv.press('back')