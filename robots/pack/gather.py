import json
import time
import requests
import gender

def run(d,cf):
    d(text="发现").click()
    with open('ok','w'):pass
    d(resourceId="com.tencent.karaoke:id/c4n").click() # 点击搜索框
    for z in range(20):
        try:
            seed_kid = requests.get('https://win.60rt.com:6088/getSeed').text #获取爬虫种子
            if seed_kid is '':
                time.sleep(5)
                continue
        except requests.exceptions.ReadTimeout:
            time.sleep(5)
            continue
            

        d(resourceId="com.tencent.karaoke:id/bi5").click()
        d(resourceId="com.tencent.karaoke:id/bi5").set_text(seed_kid) # 搜索种子用户

        try:
            d.send_action('search')
            d(text='用户').wait()
        except:
            d.set_fastinput_ime(False)  # 切换成FastInputIME输入法
            continue
        d(resourceId="com.tencent.karaoke:id/cxs").click() #点击头像
        d(resourceId="com.tencent.karaoke:id/bxw").click() #点击关注列表

        names = []
        num = 0
        while True: # favor them
            cf['gather_data'] = []
            d(text='关注').wait()
            time.sleep(1)
            count_items = d(resourceId="com.tencent.karaoke:id/c9v").count # names
            new_names = []
            for i in range(1,count_items):
                item = d(resourceId="com.tencent.karaoke:id/c9v", instance=i) # a item of name
                name = item.get_text() # get name
                new_names.append(name)
            if new_names == names:
                print('没有新数据')
                break #没有新数据
            names = new_names

            for i in range(len(names)):
                num += 1
                if num > 40:
                    num = 0
                    print('free memory!')
                    d.shell("kill -9 `ps | grep uiautomator | awk '{print $2}'`")

                name = names[i]
                d(text=name).click()
                kid = d(resourceId="com.tencent.karaoke:id/ddb").get_text() # get kid
                d(text='正在加载').wait_gone()
                if not d(text="资料").exists:
                    if not d(resourceId="com.tencent.karaoke:id/bx6").exists: # 点击隐藏信息
                        d.press('back')
                        continue
                    d(resourceId="com.tencent.karaoke:id/bx6").click() # has additional
                if d(resourceId="com.tencent.karaoke:id/bwv").exists:  # judge gender
                    img = d.screenshot()   # headportrait
                    rect = d(resourceId="com.tencent.karaoke:id/bwv").info['bounds']
                    img = img.crop((rect['left'], rect['top'], rect['right'], rect['bottom']))  # 图像裁剪
                    if gender.is_male(img):sex = 1
                    else:sex = 2
                else:sex = 0
                print(kid,name,sex)
                cf['gather_data'].append([kid,name,sex])
                d.press('back') # back
            try:
                if [] == cf.get('gather_data',[]):break
                requests.post('https://win.60rt.com:6088/putGatherData',json = cf['gather_data'])#上传爬虫数据
                print('采集数据：',cf['gather_data'])
            except:pass
            d(text=name).drag_to(text='关注',duration=0.05) # next page
        d.press('back') # back
        d.press('back') # back
    pass
