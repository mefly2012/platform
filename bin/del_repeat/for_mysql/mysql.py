# -*- coding: utf-8 -*-


import os
import time
import threading
import codecs
import json
import multiprocessing
import logging
import MySQLdb


class check_base():
    def __init__(self, host="125.65.78.23", port=3306, user="bbd", passwd="bbd-service", db="bbd_higgs", tables={}):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.tables = tables

    def __del__(self):
        pass

    def process_get_data(self, table, repeat_list):
        import logging
        start = time.time()

        strhaving = ' COUNT(%s)>1' % repeat_list[0] + ''.join([' AND COUNT(%s)>1 ' % repeat_list[x] for x in range(1, len(repeat_list))])

        cmd = 'SELECT id,' + ','.join(repeat_list) + ' FROM ' + table + ' GROUP BY ' + ','.join(repeat_list) + ' HAVING ' + strhaving

        print 'cmd:', cmd

        db = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute(cmd)
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        if data:
            print '-----------------%s' % table
            print data

        endtime = time.time()
        print (u'执行表%s耗时 %f 秒' % (table, endtime - start))


    def run(self):
        process_list = []
        start = time.time()
        for k, v in self.tables.items():
            t = multiprocessing.Process(target=self.process_get_data, name='myProcess_' + k, args=(k, v))
            t.start()
            process_list.append(t)

        flag = 1
        while flag:
            flag = 0
            for t in process_list:
                if t.is_alive():
                    flag = 1
                    time.sleep(1)
                    break

        endtime = time.time()
        logging.info(u'总耗时 %f 秒' % (endtime - start))


if __name__ == '__main__':
    a = check_base(tables={'dcos': ['company_name', 'certificate_num']})
    a.process_get_data('dcos', ['company_name', 'certificate_num'])
    pass
