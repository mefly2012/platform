# -*- coding: utf-8 -*-


import os
import time
from elasticsearch import *
import codecs
from datetime import datetime
import json
import logging


class check_base():
    def __init__(self, thread_num=1, ip_port='', db_index='', doc_type='', total=0, need_to_check=None, err_file_path=u''):

        self.db_index = db_index
        self.doc_type = doc_type
        self.need_to_check = need_to_check.need_check_ziduan
        self.need_to_check_instance = need_to_check
        self.total = total
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
        try:
            if file_handler.tell() > 10 * 1024 * 1024:
                # 太多了没意义
                return
            file_handler.write(str_in + os.linesep)
        except:
            logging.error(u'写入文件错误：' + str_in)
            pass

    def deal_all_check(self, _id, _source):
        for i_str in self.need_to_check:
            value = None
            value = _source[i_str]

            try:
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

    def run(self):
        starttime = time.time()
        try:
            fl = open(self.db_index + os.sep + self.doc_type, 'r')
        except Exception as e:
            logging.error(sys.exc_info())
            return
        ok_line = 0
        err_line = 0
        count = 0
        for i in fl.xreadlines():
            count += 1
            if self.total != 0:
                if count > self.total:
                    break
            try:
                line = i.strip().decode(u'utf-8')

                # jsobj = eval(line)
                # jsobj2 = json.dumps(jsobj)
                jsobj = json.loads(line)
                jsobj = jsobj.get('raw_data')  ###解析验证层的
                ok_line += 1
                _id = jsobj['_id']
                self.deal_all_check(_id, jsobj)
            except Exception as e:
                err_line += 1
                print count, e
                break  # 出错就终止
        fl.close()
        endtime = time.time()
        timestap = (endtime - starttime)
        hour = timestap // 3600
        minute = (timestap % 3600) // 60
        second = ((timestap % 3600) % 60) % 60
        logging.info(self.doc_type + u" ok_line:" + str(ok_line) + u",err_line:" + str(err_line) + u'耗时 %f时%f分%f秒' % (hour, minute, second))
