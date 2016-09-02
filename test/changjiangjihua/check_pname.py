# -*- coding: utf-8 -*-


import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
cunrrent_path = os.path.dirname(os.path.abspath(__file__))
father_path = os.path.dirname(cunrrent_path)
father_father_path = os.path.dirname(father_path)
father_father_father_path = os.path.dirname(father_father_path)
sys.path.append(father_path)
sys.path.append(father_father_path)
sys.path.append(father_father_father_path)

import time
from elasticsearch import *
import codecs
import json
import multiprocessing
import logging
import uuid
from logs import logconfig

if __name__ == '__main__':

    file_in = codecs.open(u'zhixing.txt', 'r', encoding='utf-8')

    count = 0
    for line in file_in:
        if len(line.strip()) == 0:
            break
        obj = json.loads(line.strip())

        name_list = obj.get('BBD_QYXX_ID_NAME_LIST', {})
        obj_name_list = json.loads(name_list)
        for name in obj_name_list:
            keys = name.keys()
            name = keys[0]
            if name not in obj.get('pname'):
                print u"%d行错误" % count

    file_in = codecs.open(u'zhixing.txt', 'r', encoding='utf-8')

    count = 0
    for line in file_in:
        if len(line.strip()) == 0:
            break
        obj = json.loads(line.strip())

        name_list = obj.get('BBD_QYXX_ID_NAME_LIST', {})
        obj_name_list = json.loads(name_list)
        for name in obj_name_list:
            keys = name.keys()
            name = keys[0]
            if name not in obj.get('pname'):
                print u"%d行错误" % count
