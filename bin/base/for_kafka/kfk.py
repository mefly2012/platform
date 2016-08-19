# -*- coding: utf-8 -*-


import os
import time
import codecs
import logging
import json
import kafka.client

kafka.client.log.setLevel(logging.ERROR)
import kafka.consumer.base

kafka.consumer.base.log.setLevel(logging.ERROR)
from storageutil import kafka


class check_base():
    def __init__(self, ip_port, topic, frm=0, total=0, err_file_path=u'', instances={}, tables=[]):
        self.ip_port = ip_port
        self.topic = topic
        self.frm = frm
        self.total = total
        self.instances = instances
        self.tables = tables
        self.err_file_path = err_file_path.decode('GBK')

        self.file_list = {}

        if not os.path.exists(self.err_file_path + os.sep + u'err_data'):
            os.mkdir(self.err_file_path + os.sep + u'err_data')

        for table in tables:
            for value in self.instances[table].need_check_ziduan:
                self.file_list[table + value] = codecs.open(self.err_file_path + os.sep + u'err_data' + os.sep + table + u'__' + value + u'_err.txt', 'w',
                                                            encoding='utf-8')

    def __del__(self):
        for table in self.tables:
            for value in self.instances[table].need_check_ziduan:
                handler = self.file_list[table + value]
                need_del = 0
                if handler.tell() == 0:
                    need_del = 1
                handler.close()
                if need_del and os.path.exists(self.err_file_path + os.sep + u'err_data' + os.sep + table + u'__' + value + u'_err.txt'):
                    os.remove(self.err_file_path + os.sep + u'err_data' + os.sep + table + u'__' + value + u'_err.txt')

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
        finally:
            pass

    def deal_all_check(self, _id, _source, bbd_table):
        try:
            instance = self.instances[bbd_table]
        except Exception as e:
            return

        for i_str in instance.need_check_ziduan:
            value = None
            try:
                value = _source[i_str]
                if value is not None:
                    value = unicode(value)
            except:
                pass

            ret = getattr(instance, 'check_%s' % i_str)(_source, value)
            if ret is not None:
                if value is not None:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  _id:【{0}】 : {1}'.format(_id, value)
                else:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  【_id:{0}】'.format(_id)
            handle = self.file_list[bbd_table + i_str]
            if handle is None:
                raise Exception(u'filehander' + bbd_table + i_str)
            self.syn_write_file(handle, ret)

    def run(self):
        db = kafka(ip_port=self.ip_port, table_name=self.topic, frm=self.frm)
        # total = db.size()
        #
        # total_1 = total
        # if total >= self.total != 0:
        #     total = self.total

        # startstr = self.topic.ljust(40) + u'总共 %9d 条, 取 %9d 条' % (total_1, total)
        # 取完
        start = time.time()
        count = 0
        all_count = {}  # 记录每个表的个数
        for table in self.tables:
            all_count[table] = 0
        while True:

            if self.total != 0:
                if count > self.total:
                    break
            data = None
            try:

                data = db.get()
                count += 1

                data = json.loads(data)
                bbd_table = data['bbd_table']
                all_count[bbd_table] = all_count.get(bbd_table, 0) + 1

                if not (count % 10000):
                    logging.info(u'table:%40s/%10d，offset:%10d' % (bbd_table, all_count[bbd_table], count))

                _id = data['_id']
                _source = data

                self.deal_all_check(_id, _source, bbd_table)
            except Exception as e:
                print e
                pass
            if not data:
                break



        js = json.dumps(all_count, ensure_ascii=False)
        logging.info(js)
        endtime = time.time()

        startstr = u''
        endstr = u'取%d条 耗时 %f 秒' % (count, endtime - start)
        logging.info(startstr + endstr)
