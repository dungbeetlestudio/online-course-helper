import uiautomator2 as u2
import json
import requests
import sys
import traceback
import os
import multiprocessing
import gather
import time
import shutil
import random
import subprocess
from multiprocessing import Process
import logging
import datetime
import qq_ocr

def input_account(cf,dv,account,password):
    dv.set_fastinput_ime(True)  # 切换成FastInputIME输入法
    dv(className="android.widget.EditText").wait()
    if account:
        dv(className="android.widget.EditText").click()
        time.sleep(1)
        logging.info(cf['account'])
        for z in range(15):dv.press('delete')
        dv.send_keys(cf['account'])  # adb广播输入
    if password:
        dv(className="android.widget.EditText", instance=1).click()
        time.sleep(1)
        logging.info(cf['password'])
        dv.send_keys(cf['password'])  # adb广播输入
    dv.set_fastinput_ime(False)  # 切换成正常的输入法
    dv(description=u"登 录").click()
def wait_for(dv):
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=False
    for z in range(10):
        if bool(dv(description=u"亿万用户已选择QQ帐号登录应用").exists):
            d = bool(dv(description=u"你的帐号暂时无法登录，请").exists)
            b = bool(dv(description=u"网络异常").exists)
            a = bool(dv(description=u"你还没有输入密码！").exists)
            m = bool(dv(description=u"您还没有输入账号").exists)
            c = bool(dv(description=u"你输入的帐号或密码不正确，请重新输入。").exists)
            print('a:%s,b:%s,c:%s,d:%s,m:%s'%(a,b,c,d,m))
            if a or b or c or d or m:return (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        elif bool(dv(text=u'QQ登录').exists):# 永久封号
            e = True
            print('e:%s'%e)
            if e:return (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        elif bool(dv(text=u"我的").exists):
            f=True
            print('f:%s'%f)
            if f:return (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        elif bool(dv(description=u"返回").exists) or bool(dv(description=u"验证").exists):
            g = bool(dv(description=u"请顺序点击大图中的文字").exists)
            h = bool(dv(description=u"验证错误，请重新验证").exists)
            o = bool(dv(description=u"请选择图中文字进行验证").exists)
            i = bool(dv(description=u"请控制拼图块对齐缺口").exists)
            j = bool(dv(description=u"这题有点难呢，已为您更换题目").exists)
            k = bool(dv(description=u"拖动下方滑块完成拼图").exists)
            l = bool(dv(description=u"请点击重新加载").exists)
            #x = bool(dv(description=u"图片加载失败，请点击刷新").exists)
            n = bool(dv(description=u"登 录").exists)
            #print('滑块图片加载%s'%x)
            print('g:%s,h:%s,i:%s,j:%s,k:%s,l:%s,n:%s,o:%s'%(g,h,i,j,k,l,n,o))
            if g or h or i or j or k or l or n or o:return (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
    return None

def run(dv,cf):
    #dv.app_start('com.sollyu.xposed.hook.model')  # modify info
    dv.app_clear('com.tencent.karaoke') 
    dv.app_start('com.tencent.karaoke')  # 启动全名k歌
    
    # if dv(text='打开 XPOSED').exists:
    #     dv(text='打开 XPOSED').click()
    #     dv(text='小心！').wait()
    #     dv(text='确定').click()
    #     dv(description="打开导航抽屉").wait()
    #     dv(description="打开导航抽屉").click()
    #     dv(text='模块').wait()
    #     dv(text='模块').click()
    #     dv(resourceId="de.robv.android.xposed.installer:id/checkbox").wait()
    #     dv(resourceId="de.robv.android.xposed.installer:id/checkbox").click()
    #     dv.shell('reboot')
    #     return True
    try:
        # dv(text=u'全民K歌').click()
        # dv(className="android.widget.ImageView", instance=1).click() # click menu 无法点击
        # dv(text=u"运行程序").click()
        dv.watcher("advertisement").when(resourceId="com.tencent.karaoke:id/cr5", text=u"跳过").click()
        dv.watcher("toolong").when(resourceId="android:id/message").click(text=u"等待")
        dv.watcher("update").when(text=u"安装").click(text=u"取消")
        
        dv(text='QQ登录').wait()
        if dv(text='QQ登录').exists:# 永久封号
            dv(text='QQ登录').click()

            sequence = {}
            screenshot_num = 3
            retry = 1
            swipe_retry = 3
            #input_account(cf,dv,True,True)

            for z in range(20):
                if dv(text="登录").exists:
                    dv(text="登录").click()
                    break
                if dv(text="授权并登录").exists:
                    dv(text="授权并登录").click()
                    break
                time.sleep(1)
            
            while True:
                flags = wait_for(dv)
                if flags is None:
                    cf['status_of_account'] = -99
                    cf['status_of_description'] = u'未知原因，等待标志超时'
                    return True
                (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o) = flags
                if a: return True
                if b: 
                    dv(description=u"登 录").click()
                    continue
                elif m:
                    input_account(cf,dv,True,False)
                    continue
                elif c:
                    if retry:
                        dv(description=u"关闭").click()
                        dv(className="android.widget.Button", instance=1).click()
                        input_account(cf,dv,False,True)
                        retry -= 1
                        continue
                    cf['status_of_account'] = -3
                    cf['status_of_description'] = u'密码错误'
                    return False
                elif d:
                    cf['status_of_account'] = -2
                    cf['status_of_description'] = u'平台封号'
                    return False
                elif e: 
                    cf['status_of_account'] = -1
                    cf['status_of_description'] = u'APP封号'
                    return False
                elif f:break
                elif o:pass # refush
                elif g or h or j or k:pass
                elif i:pass       # refresh
                elif l:
                    dv(description=u"").click()
                    continue # reload
                else:continue
                
                time.sleep(1) # just wait for verification code to show
                if g or h or o:
                    try:
                        print('验证')
                        if g: box1 = dv(description=u"请顺序点击大图中的文字").info['bounds']
                        elif o: box1 = dv(description=u"请选择图中文字进行验证").info['bounds']
                        elif h: box1 = dv(description=u"验证错误，请重新验证").info['bounds']
                        print('screenshot')
                        img = dv.screenshot()
                        img.save('screenshot.png')
                        print('crop')                    
                        little_box = (box1['right'], box1['bottom'] - 23, box1['right'] + 110, box1['bottom'] - 23 + 33)
                        big_box = (box1['left'], box1['top'] + 35, box1['left'] + 238, box1['top'] + 35 + 134)
                        little = img.crop(little_box)  # 大图
                        little.save('little.png')
                        big = img.crop(big_box)  # 小图
                        big.save('big.png')
                        sequence = qq_ocr.run('little.png', 'big.png')
                    except Exception as e:
                        traceback.print_exc()
                        print(e)
                        sequence = None
                    if not sequence:# failed to get position
                        print('无法识别！')
                        screenshot_num -= 1
                        if screenshot_num is 0:
                            print('虚拟机太卡，重启！')
                            dv.shell('reboot')
                            return True
                        dv(description=u"").click()
                        continue
                    for x, y,c in sequence:
                        print(x + big_box[0], y + big_box[1],c)
                        dv.click(x + big_box[0], y + big_box[1])
                    dv(description=u"验证").click()                # verify
                    if dv(description=u"请选择图中文字进行验证").exists:
                        dv(description=u"").click()
                    #time.sleep(2)
                elif i or j or k:
                    if swipe_retry is 0: return True
                    try:
                        print('screenshot')
                        img = dv.screenshot()
                        img.save('xcode.png')  # 存储当前区域
                        sequence = qq_ocr.run2('part/','xcode.png')
                    except Exception as e:
                        traceback.print_exc()
                        print(e)
                        sequence = None
                    if not sequence:
                        print('无法识别！')
                        screenshot_num -= 1
                        if screenshot_num is 0:
                            print('虚拟机太卡，重启！')
                            dv.shell('reboot')
                            return True
                        dv.click(0.934, 0.643)    # refresh
                        continue
                    b = dv(description=u"tag-bar").info['bounds']
                    sx = b['left'] + (b['right'] - b['left']) / 2
                    sy = b['top'] + (b['bottom'] - b['top']) / 2
                    ex = sequence[0]
                    ey = sequence[1]
                    ps = [(sx, sy),(ex - 20, ey - 5),(ex + 10, ey + 5), (ex, ey)]
                    dv.swipe_points(ps,0.05)
                    if dv(description=u"请控制拼图块对齐缺口").exists:
                        dv.click(0.934, 0.643)
                    swipe_retry -= 1
                    time.sleep(2)
        with open('ok','w'):pass # 设置标记
        gather.run(dv,cf)
    except u2.UiObjectNotFoundError as e:
        traceback.print_exc()
        return True
    finally:
        print('free memory!')
        dv.shell("kill -9 `ps | grep uiautomator | awk '{print $2}'`")
        print('post data')
        while True:
            try:
                if [] == cf.get('gather_data',[]):break
                requests.post('https://win.60rt.com:6088/putGatherData',json = cf['gather_data'])#上传爬虫数据
                print('采集数据：',cf['gather_data'])
                break
            except requests.exceptions.ReadTimeout:
                time.sleep(5)
    return True

def qq_run(d,cf):
    retry = 0

    d.app_clear('com.tencent.tim') # 启动tim
    d.app_start('com.tencent.tim')
    d(resourceId="com.tencent.tim:id/title").wait()
    for z in range(5):d.swipe(0.9,0.5,0.01,0.5,0.05)

    d(text="登 录").click()
    d(description="请输入QQ号码或手机或邮箱").set_text(cf['account'])
    d(description="密码 安全").set_text(cf['password'])

    while True:
        d(description='登录').click()
        d(text='验证码').wait()
        if not d(text='验证码').exists:break
        if d(text='输入验证码').exists:
            raise Exception()
        d(description="tag-bar").wait()
        while True:
            try:
                time.sleep(2)
                img = d.screenshot()
                img.save('qcode.png')  # 存储当前区域
                sequence = qq_ocr.run2('part2/','qcode.png')
            except Exception as e:
                traceback.print_exc()
                print(e)
                sequence = None
            if not sequence:
                d.click(0.928, 0.639)    # refresh
                continue
            b = d(description="tag-bar").info['bounds']
            sx = b['left'] + (b['right'] - b['left']) / 2
            sy = b['top'] + (b['bottom'] - b['top']) / 2
            ex = sequence[0]
            ey = sequence[1]
            ps = [(sx, sy),(ex - 20, ey - 5),(ex + 10, ey + 5), (ex, ey)]
            d.swipe_points(ps,0.05)
            time.sleep(1)
            if d(description="请控制拼图块对齐缺口").exists:d.click(0.928, 0.639)    # refresh
            else:break
        time.sleep(2)
        
        #if dv(text='帐号或密码错误，请重新输入。').exists:pass
        if d(description='登录').exists:
            retry += 1
            if retry == 2:
                cf['status_of_account'] = -3
                cf['status_of_description'] = '密码错误'
                raise Exception()
            continue

        if d(text='登录失败').exists:
            d(text='确定').click()
            retry += 1
            if retry == 2:
                cf['status_of_account'] = -3
                cf['status_of_description'] = '密码错误'
                raise Exception()
            continue

        if d(text='去安全中心').exists:
            cf['status_of_account'] = -2
            cf['status_of_description'] = '平台封号'
            raise Exception()
        
        return True

def main(cfdir, cf):
    os.chdir(cfdir)

    dv = u2.connect(cf['address'])
    dv.app_stop_all()
    dv.watcher("exit2").when(text=u"很抱歉，“TIM”已停止运行。").click(text="确定")
    dv.watcher("exit").when(text=u"很抱歉，“全民K歌”已停止运行。").click(text="确定")
    dv.watcher("u2exit").when(text=u"很抱歉，“uiautomator”已停止运行。").click(text="确定")
    with open('../../ClientSrv.share','rb') as f:css = json.loads(f.read())
    url = '%s&port=%d' % (css['url'],cf['port'])

    try:
        if not os.path.exists('ok'):
            rs = json.loads(requests.get(url % 'getGatherTask').text) #获取爬虫任务
            print(rs)
            #rs = {'account':'517013400','password':'xfskyl6422'}
            cf.update(rs)
            qq_run(dv,cf)

        if not run(dv,cf):
            os.remove('ok')
    except KeyboardInterrupt:pass
    except:
        traceback.print_exc()
    finally:
        data = {'account':cf['account'],'status_of_account':cf.get('status_of_account',0),'status_of_description':cf.get('status_of_description',None)}
        requests.post(url % 'putHistoryOfAttention',json = data,verify=False)