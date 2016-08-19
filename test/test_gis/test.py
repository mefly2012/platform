# -*- coding: utf-8 -*-

import os
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
cunrrent_path = os.path.dirname(os.path.abspath(__file__))
father_path = os.path.dirname(cunrrent_path)
father_father_path = os.path.dirname(father_path)
father_father_father_path = os.path.dirname(father_father_path)
sys.path.append(father_path)
sys.path.append(father_father_path)
sys.path.append(father_father_father_path)

import codecs
import json
import MySQLdb
from logs import logconfig
import logging
import requests

from elasticsearch import *

es = Elasticsearch('dataomes.bbdservice.net:80', timeout=30, max_retry=5, retry_on_timeout=True)


def get_gis_from_es(company_name):
    c = es.search(index='addrs', doc_type='addr',
                  body={
                      "query": {
                          "bool": {
                              "must": [
                                  {
                                      "query_string": {
                                          "query": "name:\"{0}\"".format(company_name)
                                      }
                                  }
                              ]
                          }
                      }
                  },
                  request_timeout=2000)
    for hit in c['hits']['hits']:
        _source = hit['_source']
        return (_source['lon'], _source['lat'])
    pass


def get_gis_data_list():

    p = 1
    gis_data = []

    while True:
        url = 'http://test.api.bbdservice.com/api/bbd_geo_qyxx/?lon={0}&lat={1}&page={2}&ak=8058b811e243b58a4b68aa736b7fc39d&r={3}'.format(x, y, p, r)

        data = requests.get(url=url)
        if data.status_code == 200:
            js = data.json()
            total = js.get('total')
            if not total:
                break

            results = js.get('results')
            if not len(results):
                break
            p += 1
            for i in results:
                company = i.get('company_name')
                try:
                    gis = get_gis_from_es(company)
                except:
                    print company
                    continue
                gis_data.append(gis)
                print gis
    print "gis_get_ok,total:%d" % len(gis_data)
    return gis_data


def show_fig(gis_array):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Ellipse,Circle
    import numpy as np

    def millions(x):
        return '$%1.1fM' % (x * 1e-6)

    x1 = map(lambda x: x[0], gis_array)
    y1 = map(lambda x: x[1], gis_array)



    fig, ax = plt.subplots()
    ax.fmt_ydata = millions
    plt.plot(x1, y1, 'o')

    plt.show()


import math

if __name__ == '__main__':
    x = 114.08008
    y = 22.57310
    r = 1000

    gis = get_gis_data_list()
    show_fig(gis)
    pass
