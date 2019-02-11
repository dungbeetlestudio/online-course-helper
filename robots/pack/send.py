import gender
import json
import requests
import random
import requests
import sys
import time
import os
import logging

# the following is defined function
def run(cf, dv):
    dv.watcher('messages').when(text=u"您每日私信可用条数已超限制，请明天再试").click(text=u"确定")
    dv(text=u"我的").click()  # personal info
    fans = int(dv(resourceId="com.tencent.karaoke:id/bxq").get_text())
    last_fans = cf.get('fans',0)
    cur_fans = fans - last_fans
    if  cur_fans <= 0:
        cf['time_of_done'] = int(time.time()) * 1000
        return True
    cf['fans'] = last_fans
    logging.info('new fans:%d' % cur_fans)
    dv(text=u"粉丝").click() # click attention 存在无法点击到的问题
    dv(text=u'粉丝列表').wait()
    names_of_fans = {}
    for id,o in cf['attentions'].items(): 
        name = o.get('name',None)
        if name is None: continue
        names_of_fans[name] = id

    while cur_fans and cf['numConf'][1]:
        count_items = dv(resourceId="com.tencent.karaoke:id/c9v").count
        name = ''
        for i in range(1,count_items):
            if os.path.exists('../../stop'): break
            o = dv(resourceId="com.tencent.karaoke:id/c9v",instance=i)
            name = o.get_text()
            if cf['numConf'][1] is 0: break # [1]最大私信数
            logging.info(name.encode('gbk','replace').decode('gbk'))           
            if names_of_fans.get(name,None): continue       # 是否重复发送
            o.click()
            time.sleep(1)
            if not dv(text=u'K歌号').exists: dv(resourceId="com.tencent.karaoke:id/dlw").click()
            id = dv(resourceId="com.tencent.karaoke:id/ddb").get_text() # 获取id
            if cf['attentions'].get(id,None):
                print('id相同，重复私信，忽略')
                dv.press('back')
                time.sleep(1)
                continue
            print(name)
            cur_fans -= 1
            cf['fans'] += 1
            wechat = cf['wechat'][random.randint(0,len(cf['wechat']) - 1)]
            wechat_confuse = cf['wechat_confuse'][random.randint(0,len(cf['wechat_confuse']) - 1)]
            message = cf['message'][random.randint(0,len(cf['message']) - 1)]
            message = message.replace('{wechat_confuse}',wechat_confuse).replace('{wechat}',wechat)
            time.sleep(1)
            dv(resourceId="com.tencent.karaoke:id/b9b").click() # send message

            for m in message.split('@'):
                if m is '': continue
                dv(resourceId="com.tencent.karaoke:id/iy").wait()
                dv(resourceId="com.tencent.karaoke:id/iy").set_text(m)  # say something
                dv(description=u"发表").click()  # send

            dv(resourceId="com.tencent.karaoke:id/ayy").wait()
            if dv(description=u"发送失败").exists:
                logging.info('关注失败，功能受限')
                cf['status_of_sent'] = u"私信失败，功能受限" # 设置私信状态 
                cf['status_of_account'] = -4
                return# 切换账号
            names_of_fans[name] = id
            cf['attentions'][id] = {'name':name,'wechat':wechat,'time_of_sent':int(time.time())*1000}
            cf['numConf'][1] -= 1 # 最大私信记录
            dv(resourceId="com.tencent.karaoke:id/aa3").wait() # back
            dv.press('back')
            dv(resourceId="com.tencent.karaoke:id/b9g").wait() # back to list
            dv.press('back')
            if cf['numConf'][1] is 0: break
            if cur_fans is 0: break
        if dv(text=u'已加载全部').exists: break
        dv(text=name).drag_to(text=u'粉丝')# next page
    cf['time_of_done'] = int(time.time()) * 1000
    dv(resourceId="com.tencent.karaoke:id/aa3").wait() # back
    dv.press('back')
    dv.toast.show("任务结束")