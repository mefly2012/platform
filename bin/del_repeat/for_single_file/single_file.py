# -*- coding: utf-8 -*-


import os
import time
import threading
import codecs
import json
import multiprocessing
import logging
import copy


class check_base():
    def __init__(self, thread_num, file_name, total=0, need_to_check_ziduan=[], err_file_path=u''):
        self.thread_num = thread_num
        self.file_name = file_name
        self.need_to_check = need_to_check_ziduan
        self.total = total
        self.lock = multiprocessing.Lock()
        self.err_file_path = err_file_path.decode('GBK')

        self.err_file = None
        if not os.path.exists(self.err_file_path + os.sep + u'err_data'):
            os.mkdir(self.err_file_path + os.sep + u'err_data')
        err_name = multiprocessing.current_process().name
        self.err_file = codecs.open(self.err_file_path + os.sep + u'err_data' + os.sep + file_name + u'__' + err_name + u'_err.txt', 'w',
                                                encoding='utf-8')

    def __del__(self):
        handler = self.err_file
        need_del = 0
        if handler.tell() == 0:
            need_del = 1
        handler.close()
        if need_del and os.path.exists(self.err_file_path + os.sep + u'err_data' + os.sep + self.file_name + u'__' + self.err_file + u'_err.txt'):
            os.remove(self.err_file_path + os.sep + u'err_data' + os.sep + self.file_name + u'__' + self.err_file + u'_err.txt')

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
            ret = getattr(self, 'check_%s' % i_str)(_source, value)
            if ret is not None:
                if value is not None:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  _id:【{0}】 : {1}'.format(_id, value)
                else:
                    ret = u'字段 {0}'.format(i_str) + ret + u'  【_id:{0}】'.format(_id)
            # ret = unicode(i_str) + ret if ret != None else ret
            handle = self.err_file
            if handle is None:
                raise Exception('filehander' + i_str)
            self.syn_write_file(handle, ret)

    def process_get_data(self, frm, size_to):

        fl = open(self.file_name, 'rb')
        fl.seek(frm)
        ok_line = 0
        err_line = 0
        while fl.tell() < size_to:
            line = fl.readline()
            line = line.encode('utf-8')

            try:
                jsobj = json.loads(line)
                ok_line += 1
                _id = jsobj['_id']
                self.deal_all_check(_id, jsobj)
            except:
                err_line += 1
                continue
        fl.close()

        logging.info("ok_line:" + str(ok_line) + ",err_line:" + str(err_line))

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

        print c
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
    obj = check_base(1, file_name='test.txt', total=0, need_to_check_ziduan=['abc'], err_file_path=os.path.split(os.path.realpath(__file__))[0])
    obj.run()
    pass
