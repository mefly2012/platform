# -*- coding: utf-8 -*-


import os
import time
from elasticsearch import *
import threading
import codecs
from datetime import datetime
import logging


class check_base():
    def __init__(self, thread_num, ip_port, db_index, doc_type, total=0, need_to_check=None, err_file_path=u''):
        self.thread_num = thread_num
        self.ip_port = ip_port
        self.db_index = db_index
        self.doc_type = doc_type
        self.need_to_check = need_to_check.need_check_ziduan
        self.need_to_check_instance = need_to_check
        self.total = total
        self.lock = threading.RLock()
        self.err_file_path = err_file_path.decode('GBK')
        datetime.strptime('2016/03/12 10:59:07', '%Y/%m/%d %X')  # for thread safe

        self.file_list = {}
        if not os.path.exists(self.err_file_path + os.sep + u'err_data'):
            os.mkdir(self.err_file_path + os.sep + u'err_data')
        for value in self.need_to_check:
            self.file_list[value] = codecs.open(self.err_file_path + os.sep + u'err_data' + os.sep + doc_type + u'__' + value + u'_err.txt', 'w',
                                                encoding='utf-8')

    def __del__(self):
        for value in self.need_to_check:
            handler = self.file_list[value]
            need_del = 0
            if handler.tell() == 0:
                need_del = 1
            handler.close()
            if need_del and os.path.exists(self.err_file_path + os.sep + u'err_data' + os.sep + self.doc_type + u'__' + value + u'_err.txt'):
                os.remove(self.err_file_path + os.sep + u'err_data' + os.sep + self.doc_type + u'__' + value + u'_err.txt')

    def syn_write_file(self, file_handler, str_in):
        if str_in is None:
            return

        self.lock.acquire()
        try:
            if file_handler.tell() > 10 * 1024 * 1024:
                # 太多了没意义
                return
            file_handler.write(str_in + os.linesep)
        except:
            pass
        finally:
            self.lock.release()

    def deal_all_check(self, _id, _source):
        for i_str in self.need_to_check:
            value = None
            try:
                value = _source[i_str]
                if value is not None:
                    value = unicode(value)
            except:
                pass
            ret = getattr(self.need_to_check_instance, 'check_%s' % i_str)(_source, value)
            if ret is not None:
                if value is not None:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  _id:【{0}】 : {1}'.format(_id, value)
                else:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  【_id:{0}】'.format(_id)
            # ret = unicode(i_str) + ret if ret != None else ret
            handle = self.file_list[i_str]
            if handle is None:
                raise Exception('filehander' + i_str)
            self.syn_write_file(handle, ret)

    def thread_get_data(self, frm, total):
        es = Elasticsearch(self.ip_port, timeout=30, max_retry=5, retry_on_timeout=True)
        # print threading.current_thread().getName(),' ',frm,' ',total
        count_per_time = 20
        times = total // count_per_time
        yushu = total % count_per_time
        jia = 1 if yushu > 0 else 0
        for i in xrange(times + jia):
            # print '%d/%d' % (i, times)
            if i == times:
                count_per_time = yushu
            # print u'from %d size %d'%(frm + i * count_per_time,count_per_time)
            c = es.search(index=self.db_index, doc_type=self.doc_type,
                          body={"query": {"match_all": {}},
                                'from': frm + i * count_per_time,
                                'size': count_per_time},
                          request_timeout=2000)

            for hit in c['hits']['hits']:
                _id = hit['_id']
                _source = hit['_source']
                # print 123
                self.deal_all_check(_id, _source)

    def run(self):
        thread_num = self.thread_num
        es = Elasticsearch(self.ip_port)
        c = es.search(index=self.db_index, doc_type=self.doc_type,
                      body={"query": {"match_all": {}},
                            'size': 0})

        total = c['hits']['total']

        total_1 = total
        if total >= self.total != 0:
            total = self.total

        startstr = self.doc_type.ljust(40) + u'总共 %9d 条, 取 %9d 条' % (total_1, total)
        threadList = []
        yushu = total % thread_num
        every_thread_num = (total + yushu) // thread_num

        start = time.time()
        for i in range(thread_num):
            t = threading.Thread(target=self.thread_get_data, name='thread_' + str(i), args=(i * every_thread_num, every_thread_num))
            t.start()
            threadList.append(t)

        flag = 1
        while flag:
            flag = 0
            for i in threadList:
                if i.isAlive():
                    flag = 1
                    time.sleep(1)
                    break

        endtime = time.time()
        endstr = u'耗时 %f 秒' % (endtime - start)
        logging.info(startstr + endstr)
