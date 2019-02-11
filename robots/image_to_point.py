import cv2
import numpy as np

def run(source_path,target_path):
    img = cv2.imread(source_path,0)
    template = cv2.imread(target_path,0)
    w,h = template.shape[::-1]
    # 6 中匹配效果对比算法
    method = cv2.TM_CCOEFF#, 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return (top_left[0] + w / 2,top_left[1] + w / 2, max_val) # 返回中心点