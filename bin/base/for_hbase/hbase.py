# -*- coding: utf-8 -*-


import os
import time
import codecs
from datetime import datetime
import logging
import happybase
import json


class check_base():
    def __init__(self, host, table, total=0, need_to_check=None, err_file_path=u''):
        self.host = host
        self.table = table
        self.need_to_check = need_to_check.need_check_ziduan
        self.need_to_check_instance = need_to_check
        self.total = total
        self.err_file_path = err_file_path.decode('GBK')
        datetime.strptime('2016/03/12 10:59:07', '%Y/%m/%d %X')  # for thread safe

        self.file_list = {}
        if not os.path.exists(self.err_file_path + os.sep + u'err_data'):
            os.mkdir(self.err_file_path + os.sep + u'err_data')
        for value in self.need_to_check:
            self.file_list[value] = codecs.open(self.err_file_path + os.sep + u'err_data' + os.sep + table + u'__' + value + u'_err.txt', 'w',
                                                encoding='utf-8')

    def __del__(self):
        for value in self.need_to_check:
            handler = self.file_list[value]
            need_del = 0
            if handler.tell() == 0:
                need_del = 1
            handler.close()
            if need_del and os.path.exists(self.err_file_path + os.sep + u'err_data' + os.sep + self.table + u'__' + value + u'_err.txt'):
                os.remove(self.err_file_path + os.sep + u'err_data' + os.sep + self.table + u'__' + value + u'_err.txt')

    def syn_write_file(self, file_handler, str_in):
        if str_in is None:
            return
        try:
            if file_handler.tell() > 10 * 1024 * 1024:
                # 太多了没意义
                return
            file_handler.write(str_in + os.linesep)
        except:
            pass

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
                    ret = u'字段 {0}'.format(i_str) + ret + u'  rk:【{0}】 : {1}'.format(_id, value)
                else:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  rk:【{0}】'.format(_id)
            handle = self.file_list[i_str]
            if handle is None:
                raise Exception('filehander' + i_str)
            self.syn_write_file(handle, ret)

    def run(self):

        start = time.time()

        conn = happybase.Connection(self.host)
        table = conn.table(self.table)
        count = 0

        for rk, data in table.scan():
            count += 1
            if self.total != 0:
                if count > self.total:
                    break
            # new_data={}
            # for k, v in data.items():
            #     new_data[k[5:]] = v.decode('utf-8')
            new_data = dict([(k[5:], v.decode('utf-8')) for k, v in data.items()])
            _id = rk
            _source = new_data
            # print 123
            self.deal_all_check(_id, _source)
            # data = map(lambda x,y:{x:y.decode('utf-8')},map(lambda key : key[5:],data.keys()), data.values())
            # print rk, json.dumps(data, ensure_ascii=False)
        pass

        startstr = ''
        endtime = time.time()
        total = min(self.total, count)
        endstr = u'获取了%d条，耗时 %f 秒' % (total, endtime - start)
        logging.info(startstr + endstr)


if __name__ == '__main__':
    conn = happybase.Connection('c5node6')
    table = conn.table('BASIC_KTGG')
    count = 0

    for rk, data in table.scan():
        count += 1
        if count > 10:
            break
        # new_data={}
        # for k, v in data.items():
        #     new_data[k[5:]] = v.decode('utf-8')
        # new_data = dict([(k[5:],v.decode('utf-8')) for k,v in data.items()])
        # data = map(lambda x,y:{x:y.decode('utf-8')},map(lambda key : key[5:],data.keys()), data.values())
        print rk, json.dumps(data, ensure_ascii=False)
    pass
