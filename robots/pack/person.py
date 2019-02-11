import logging
import time
import random

def run(cf,dv):
    dv(text="我的").click()  # personal info
    time.sleep(3)
    dv(resourceId="com.tencent.karaoke:id/dbf").wait()
    bounds = dv(resourceId="com.tencent.karaoke:id/dbf").info['bounds']
    dv.click(bounds['left'] + 10,bounds['bottom'] + 5)  # change background 
    dv(text="从手机相册选择").click()
    dv(text="bg").click()
    time.sleep(1)
    i = random.randint(0, dv(className="android.widget.ImageView").count - 1)
    dv(className="android.widget.ImageView", instance=i).click()
    dv(description=u"完成").click()
    time.sleep(1)
    dv(resourceId="com.tencent.karaoke:id/bwr").wait()
    dv(resourceId="com.tencent.karaoke:id/bwr").click() # 编辑个人资料
    time.sleep(1)
    dv.swipe(0.5,0.2,0.5,0.6)
    dv(text="更换头像").click()  # click change headportrait
    dv(text="从相册选取").click()
    dv(text="hd").click()
    time.sleep(1)
    of_random_headportrait = random.randint(0, dv(className="android.widget.ImageView").count - 1)
    dv(className="android.widget.ImageView", instance=of_random_headportrait).click()
    dv(description=u"完成").click()
    
    if len(cf.get('nicknames',[])):
        nickname = cf['nicknames'][random.randint(0,len(cf['nicknames']) - 1)]
        dv(resourceId="com.tencent.karaoke:id/a0i").set_text(nickname)  # nickname

    if dv(text=u"男").exists:
        dv(text=u"男").click()
        dv(text=u"女").click()  # gender

    wechat = ''
    wechat_confuse = ''
    if len(cf.get('wechat',[])):
        wechat = cf['wechat'][random.randint(0,len(cf['wechat']) - 1)]
        wechat_confuse = cf['wechat_confuse'][random.randint(0,len(cf['wechat_confuse']) - 1)]

    signature = cf['signatures'][random.randint(0,len(cf['signatures']) - 1)]
    signature = signature.replace('{wechat_confuse}',wechat_confuse).replace('{wechat}',wechat)
    dv(resourceId="com.tencent.karaoke:id/bvo").clear_text()
    dv(resourceId="com.tencent.karaoke:id/bvo").set_text(signature)  # signature
    dv(text=u"完成").click()