import cv2
import numpy as np

def run(source_path,target_path):
    img = cv2.imread(source_path,0)
    template = cv2.imread(target_path,0)
    w,h = template.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    img_size = img.shape[::-1]
    if top_left[0] < (img_size[0] / 2):
        return (0,0,0)
    return (top_left[0] + w / 2,top_left[1] + w / 2, max_val) # 返回中心点