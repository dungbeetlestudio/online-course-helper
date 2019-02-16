import uiautomator2 as u2
import json
import requests
import sys
import traceback
import os
import multiprocessing
import time
import shutil
import random
import subprocess
from multiprocessing import Process
import logging
import datetime
import qq_ocr
import task
from api_def import API


def main(cfdir, cf):
    os.chdir(cfdir)
    rs = json.loads(requests.get(API.Online, {'id': cf['address']}).text)

    print(rs)
    if rs['err']:
        print('accounts is empty')
        time.sleep(10)
        return

    robot = rs['ret']
    status = {'hasEntered': False}
    order = {'i': 0, 'f': 'enter', 'v': '直播测试课'}

    while True:
        time.sleep(5)
        try:
            order = json.loads(requests.get(
                API.DoWhat, {'account': robot['account']}).text)
        except:
            continue

        print(order)
        task.main(cf, order, status)

        while True:
            try:
                order = json.loads(requests.get(
                    API.TellStatus, {'status': status}).text)
                break
            except:
                pass
