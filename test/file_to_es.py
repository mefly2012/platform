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


class check_base():
    def __init__(self, thread_num, file_name, total=0, ip_port='', db_index='', doc_type=''):
        self.thread_num = thread_num
        self.file_name = file_name
        self.total = total
        self.ip_port = ip_port
        self.db_index = db_index
        self.doc_type = doc_type
        self.lock = multiprocessing.Lock()

    def __del__(self):
        pass

    def deal_all_check(self, _id, _source):
        pass

    def process_get_data(self, frm, size_to):

        es = Elasticsearch(self.ip_port, timeout=30, max_retry=5, retry_on_timeout=True)

        fl = codecs.open(self.file_name, 'r', encoding='utf-8')
        fl.seek(frm)
        all_line = 0
        ok_line = 0
        err_line = 0
        send_ok_line = 0
        err_flag = 0
        err_example = ''
        while fl.tell() < size_to:
            line = fl.readline()
            line = line.strip()
            all_line += 1

            try:
                jsobj = json.loads(line)
                ok_line += 1
                # basic = jsobj['basic'][0]

                es.index(self.db_index, self.doc_type, jsobj, id=uuid.uuid1())
                send_ok_line += 1

            except Exception as e:
                if err_flag == 0:
                    print str(e)
                    err_example = line

                err_flag = 1

                err_line += 1
                continue
        fl.close()

        print 'all:%d\n,ok:%d\n,err_line:%d\n,send_ok_line:%d\nerr_example:%s' % (all_line, ok_line, err_line, send_ok_line, err_example)

    def run(self):
        process_num = self.thread_num

        fl = open(self.file_name, 'r')
        fl.seek(0, os.SEEK_END)
        total = fl.tell()

        total_1 = total
        if total >= self.total != 0:
            total = self.total

        print self.file_name.ljust(40) + u'总共 %9d 字节, 取 %9d 字节' % (total_1, total),

        a = range(process_num)
        c = [x * (total / process_num) for x in a]
        fl.seek(0, 0)
        for offset in range(process_num):  ####只能处理json 的，这个不处理也没多大关系，就丢弃几条。
            if c[offset] == 0:
                continue
            else:
                fl.seek(c[offset])
                tmp = fl.readline()
                if tmp == "":
                    break
                try:
                    json.loads(tmp)
                    tmpindex = fl.tell() - len(tmp + os.linesep)
                    c[offset] = tmpindex
                except:
                    c[offset] = fl.tell()

        c.append(total)
        fl.close()
        process_list = []
        start = time.time()
        for i in range(len(c) - 1):  # 注意这里
            t = multiprocessing.Process(target=self.process_get_data, name='myProcess_' + str(i), args=(c[i], c[i + 1]))
            t.start()
            process_list.append(t)

        flag = 1
        while flag:
            flag = 0
            for i in process_list:
                if i.is_alive():
                    flag = 1
                    time.sleep(1)
                    break

        endtime = time.time()
        print u'耗时 %f 秒' % (endtime - start)


if __name__ == '__main__':
    logconfig.init_log('file_to_es.log')
    db_index = 'qyxx_basic_db'
    doc_type = 'guozibeijing'
    ip_host = '118.123.9.111:9292'
    file_name = 'out.txt1'

    a = check_base(thread_num=4, db_index=db_index, doc_type=doc_type, ip_port=ip_host, file_name=file_name)
    a.run()

    pass
