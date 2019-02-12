import random
import requests
import uiautomator2 as u2
import time

d = u2.connect('emulator-5554')

desktop_page = d(resourceId="com.android.launcher3:id/workspace")
login_page = d(resourceId="com.tencent.edu:id/ub")
index_page = d(text=u"人人都会微信小程序")
skip_page = d(text=u'跳过')
course_page = d(resourceId="com.tencent.edu:id/sm", text=u"咨询")
courselist_page = d(resourceId="com.tencent.edu:id/to")
room_page = d(resourceId="com.tencent.edu:id/q5")
button_msg = d(resourceId="com.tencent.edu:id/q5")
input_send = d(resourceId="com.tencent.edu:id/pr")
button_send = d(resourceId="com.tencent.edu:id/hp", text=u"发送")
button_flower = d(resourceId="com.tencent.edu:id/q6")
button_sign = d(text=u"立即报名")
button_enter = d(resourceId="com.tencent.edu:id/ss")
text_living = d(text=u'正在直播')

msg = 'hahahah'

while True:
    if desktop_page.exists():
        d.app_start('com.tencent.edu')
    elif login_page.exists():
        d(resourceId="com.tencent.edu:id/ub").click()  # qq登陆
    elif index_page.exists():
        d(text=u"人人都会微信小程序").click()
        d(resourceId="com.tencent.edu:id/d5").send_keys('直播测试课')  # 课程名
        d.press("enter")  # 搜索课程
        d(resourceId="com.tencent.edu:id/ul", text=u"C语言/C++语言/数据结构算法/MFC/QT【杰越教育】", className="android.widget.TextView").click()         # 选择第一个课程
    elif skip_page.exists():
        d(text=u'跳过').click()
    elif course_page.exists():
        if text_living.exists():#正在直播中
            button_enter.click() # 进入房间
        else:
            button_sign.click() #报名
            d.press('back')
    elif room_page.exists():
        if True:        #发送文本
            button_msg.click()
            input_send.send_keys(msg)
            button_send.click()
            d.press('back')
            d.press('back')
        else:           #鲜花
            button_flower.click()
    else:
        pass