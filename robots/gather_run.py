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
    dv.watcher("u2exit").when(text=u"很抱歉，“uiautomator”已停止运行。").click(text="确定")

    rs = {'account':'517013400','password':'xfskyl6422'}
    cf.update(rs)
    qq_run(dv,cf)