import requests
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14989385'
API_KEY = 'IKG1oBrfpGQFdZ3X6505f7MD'
SECRET_KEY = 'xb7VAEs2nvZYpXiz5QUzOlTcastX3Y10'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 如果有可选参数 """
options = {}
options["recognize_granularity"] = "big"
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "false"
options["detect_language"] = "false"
options["vertexes_location"] = "false"
options["probability"] = "true"

""" 带参数调用通用文字识别（含位置信息版）, 图片参数为本地图片 """
with open('s.png', 'rb') as fp:
    image = fp.read()
rs = client.basicAccurate(image, options)
text = {}
print(rs)