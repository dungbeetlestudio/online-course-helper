from multiprocessing import Process,freeze_support
import subprocess
import requests
import os
import gather_run
import json
import time
from copy import deepcopy
from array import array
import re
import shutil
from config import cf
import sys

if __name__ == '__main__':  #windows下必须加这句
    freeze_support()
    try:
        ps = {}
        while True:
            adb = subprocess.Popen('adb devices',shell=True,stdout=subprocess.PIPE)
            adb.wait()
            output_text = str(adb.stdout.read(), encoding = "utf8")
            devices = re.findall(r'\d+.\d+.\d+.\d+:\d+\tdevice|emulator-\d+\tdevice',output_text)
            for address in devices:
                cf['address'] = address.split('\t')[0]
                port = int(re.findall(r'\d{4}',address)[0])
                cf['port'] = port + 1 if port % 2 is 0 else port
                dir = 'environment/%d/' % cf['port']
                processor = ps.get(cf['address'],None)
                if processor and processor.is_alive():continue
                if processor: pass#print('task %s exit'% cf['address'])
                processor = Process(target=gather_run.main, args=(dir, cf))
                os.makedirs(dir, exist_ok=True)
                if not os.path.exists(dir + 's.ttc'):
                    shutil.copy('s.ttc',dir + 's.ttc')
                if not os.path.exists(dir + 'part/'):
                    shutil.copytree('part/',dir + 'part/')
                if not os.path.exists(dir + 'part2/'):
                    shutil.copytree('part2/',dir + 'part2/')
                ps[cf['address']] = processor
                processor.start()
            time.sleep(10)
    except KeyboardInterrupt:pass