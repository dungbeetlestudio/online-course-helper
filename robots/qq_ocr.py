from aip import AipOcr
import word_to_image
import image_to_point
import part_to_image
import requests
import json
import os
from cy_four import cy

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 读取成语 """
def get_cy_content(filePath):
    with open(filePath, 'r',encoding='utf-8') as fp:
        return fp.read()

def get_cf_images(file_path):
    with open(file_path, 'r') as fp:
        return fp.read()

def set_cf_images(file_path):
    with open(file_path, 'w') as fp:
        return fp.write()

def baidu_ocr(image):
    baidu_api = {'num':0,'appId':'','key':'','secret':''}
    
    try:
        with open('api.txt','r') as f:
            baidu_api = json.loads(f.read())
    except:
        baidu_api['num'] = 10

    if baidu_api['num'] < 10:
        baidu_api['num'] += 1
    else:
        while True:
            try:
                rs = requests.post('https://win.60rt.com:6088/getApiKey')
                baidu_api = json.loads(rs.text)['data']
                baidu_api['num'] = 0       
                break
            except:pass

    with open('api.txt','w') as f:
        f.write(json.dumps(baidu_api))

    """ 你的 APPID AK SK """
    APP_ID = baidu_api['appId']
    API_KEY = baidu_api['key']
    SECRET_KEY = baidu_api['secret']

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
    rs = client.basicAccurate(image, options)
    text = {}

    print(rs)
    try:
        i = 1
        for w in rs['words_result'][0]['words']:
            text[w] = i
            i += 1
        print(text)
    except:
        text = None
    return text

# 检测匹配
def check(text_rs,image_path):
    cy_images = {}
    maxSumRs = 0
    maxPoints = []
    cacheRs = {}
    for i in range(4,0,-1):
        for a in text_rs[i]:
            sumRs = 0
            points = []
            for c in a:
                f = str(ord(c))
                (x,y,rs) = cacheRs.get(c, (False, False, False))
                if not rs:
                    if not cy_images.get(c,None):
                        cy_images[c] = word_to_image.run(c,'cy_images/'+ f)
                    (x,y,rs) = image_to_point.run(image_path,'./cy_images/' + f + '.png')
                    cacheRs[c] = (x,y,rs)
                points.append((x,y,c))
                sumRs += rs
            if sumRs > maxSumRs :
                maxSumRs = sumRs
                maxPoints = points
                maxSumWords = a
            #print("matched item:",a, sumRs, points)
    #print("max matched item:",maxSumWords, maxSumRs, maxPoints)
    return maxPoints

def run(little,big):
    os.makedirs('cy_images',exist_ok=True)
    print(little,big)
    little_image = get_file_content(little)
    text = baidu_ocr(little_image)
    if text is None:
        return None

    text_rs = {1:[],2:[],3:[],4:[]}

    #查找成语
    for o in cy:
        max_i = n = 0
        is_continue = False
        for c in o: 
            i = text.get(c,None)
            if i is None:
                continue
            if i > max_i:
                n+=1
                max_i = i
            else:
                is_continue = True
                break
        if is_continue:continue

        if n != 0: text_rs[n].append(o)

    if len(text_rs[4]) > 0 :
        text_rs[3] = []
        text_rs[2] = []
        text_rs[1] = []
    elif len(text_rs[3]) > 0:
        text_rs[2] = []
        text_rs[1] = []
    elif len(text_rs[1]) > 200:
        text_rs[1] = []
    return check(text_rs,big)
    
def run2(part,big):
    point = None
    max_rs = 0
    for dirpath,dirnames,filenames in os.walk(part):
        for file in filenames:
            fullpath=os.path.join(dirpath,file)
            (x,y,rs) = part_to_image.run(big,fullpath)
            print(x,y,rs,fullpath)
            if rs > max_rs and x > (288 / 2):
                max_rs = rs
                point = (x,y)
    if point[0] == 0:return None
    return point