import random
import requests
import uiautomator2 as u2
import time

d = u2.connect('emulator-5554')

desktop_page = d(resourceId="com.android.launcher3:id/workspace")
login_page = d(resourceId="com.tencent.edu:id/ub")
guide_page = d(text=u"选择你的学院")
index_page = d(text=u"人人都会微信小程序")
sign_page = d(text=u"立即报名", className="android.widget.Button")
bind_page = d(text=u"绑定手机", className="android.widget.TextView")
enter_page = d(text=u"立即学习", className="android.widget.Button")

while True:
    if login_page.exists():
        d(resourceId="com.tencent.edu:id/ub").click()  # qq登陆
    if guide_page.exists():
        d(text=u'跳过').click()  # 跳过
    if index_page.exists():
        d(text=u"人人都会微信小程序").click()
        d(resourceId="com.tencent.edu:id/d5").send_keys('直播测试课')  # 课程名
        d.press("enter")  # 搜索课程
        d(resourceId="com.tencent.edu:id/ul").click()  # 选择第一个课程
    if sign_page.exists():
        d(text=u"立即报名").click()
    if bind_page.exists():
        d(text=u'跳过').click()
    if enter_page.exists():
        d(text=u"立即学习").click()
    if desktop_page.exists():
        d.app_start('com.tencent.edu')