# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("UTF-8")
sys.path.append("../")

from kafka import KafkaClient, SimpleConsumer, common
from Queue import Queue
import storageutil


class kafka:
    def __init__(self, ip_port, table_name, frm, **args):
        """
        :param host
        :param port
        :param table_name
        :return: kafka
        """
        self.queue = []
        self.queue_name = table_name.replace(":", "_")
        self.kafka = KafkaClient(ip_port)
        self.consumer = SimpleConsumer(self.kafka, "BASIC_DB_CPD_XGXX_30_1", self.queue_name, auto_commit_every_n=1, max_buffer_size=None)
        self.consumer.seek(frm, 0)
        #self.kafka.send_offset_commit_request()
        self.consumer.commit()

    def __del__(self):
        if self.kafka:
            self.kafka.close()

    def get(self, **args):
        if not self.queue:
            try:
                self.consumer._fetch()
            except Exception as e:
                print e
            kq = self.consumer.queue
            while not kq.empty():
                partition, result = kq.get_nowait()
                self.queue.append(result)
                self.consumer.offsets[partition] += 1
                self.consumer.count_since_commit += 1

            self.consumer.queue = Queue()
            self.consumer.commit()

        if self.queue:
            return self.queue.pop().message.value
        else:
            return None

    def size(self, **args):
        count = 0
        for k, v in self.consumer.offsets.items():
            reqs = [common.OffsetRequest(self.queue_name, k, -1, 1)]
            (resp,) = self.consumer.client.send_offset_request(reqs)
            count += (resp.offsets[0] - v)
        return count + len(self.queue)


if '__main__' == __name__:
    db = storageutil.kafka(table_name='bbd_queue_test_parser_20160705', ip_port='c5node1:9092', frm=0)

    print db.size()

    count = 10
    aa = db.get()
    while count:
        count-=1
        aa = db.get()
        print aa
