# -*- coding: utf-8 -*-
import json
from elasticsearch import Elasticsearch
import os
import MySQLdb
import re

host = "125.65.78.28"
port = 3306
user = "bbd"
passwd = "bbd-service"
db = "bbd_higgs"
doc_path = os.path.split(os.path.realpath(__file__))[0]

if __name__ == '__main__':

    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8', use_unicode=True)
    cursor = db.cursor()

    all_err = 0
    wanttotal = 0
    all_need_insert_mysql = 0
    db_index = 'qyxx_history_v1'
    doc_type = 'qyxx'
    order_key = 'bbd_qyxx_id'
    asc_or_desc = 'desc'
    es_dp_test_hosts = [{"host": "c4node27", "port": 59200}]
    es = Elasticsearch(es_dp_test_hosts, timeout=20000)
    c = es.search(index=db_index, doc_type=doc_type,
                  body={"query": {"match_all": {}},
                        'size': 0})

    total = c['hits']['total']

    total_1 = total
    if total > wanttotal != 0:
        total = wanttotal

    startstr = u'总共 %9d 条, 取 %9d 条' % (total_1, total)

    frm = 0
    count_per_time = 20
    times = total // count_per_time
    yushu = total % count_per_time
    jia = 1 if yushu > 0 else 0

    currentList = []
    cunrent_company_qyxx_id = ''
    count = 0
    company_enterprise_statusList1 = (u'存续', u'迁出')
    company_enterprise_statusList2 = (u'存续', u'注销')
    for i in xrange(times + jia):
        if i == times:
            count_per_time = yushu
        c = es.search(index=db_index, doc_type=doc_type,
                      body={"query": {"match_all": {}},
                            "sort": {
                                order_key: {
                                    "order": asc_or_desc
                                }
                            },
                            'from': frm + i * count_per_time,
                            'size': count_per_time},
                      request_timeout=2000)

        for hit in c['hits']['hits']:
            try:
                if wanttotal != 0 and count > wanttotal:
                    exit(0)
                # count += 1
                print count
                if (count % 10000) == 0:
                    print u'deal:%d' % count

                onedata = hit['_source']
                qyxx_id = onedata.get('bbd_qyxx_id')
                newest = None
                if cunrent_company_qyxx_id == qyxx_id:  # 有重复
                    currentList.append(onedata)
                    continue
                else:  # 去重，判断
                    cunrent_company_qyxx_id = qyxx_id

                    lens = len(currentList)
                    if lens > 1:
                        status_list = set()
                        approval_date_list = {}
                        bbd_uptime_list = {}
                        two_compare = {}
                        #####get('qyxx_basic', '')[0].
                        for n, i in enumerate(currentList):
                            status = i.get('company_enterprise_status', '')
                            status_list.add(status)

                            approval_date = i.get('approval_date', '')
                            # approval_date_list[approval_date] = n

                            bbd_uptime = i.get('bbd_uptime', '')
                            # bbd_uptime_list[bbd_uptime] = n

                            two_compare[approval_date + str(bbd_uptime)] = n

                            sort_key = two_compare.keys()
                            sort_key.sort(reverse=True)

                        if status_list == company_enterprise_statusList1:  # (u'存续', u'迁出')
                            for i in sort_key:
                                newest = currentList[two_compare.get(i)]
                                if newest.get('company_enterprise_status', '') == u'存续':
                                    break
                        elif status_list == company_enterprise_statusList2:  # (u'存续', u'注销')
                            newest = None
                            for i in sort_key:
                                newest = currentList[two_compare.get(i)]
                                if newest.get('company_enterprise_status', '') == u'存续':
                                    break
                            pass
                        else:
                            # 核准日期最新
                            newest = currentList[two_compare.get(sort_key[0])]
                            pass
                        pass
                    elif lens == 1:
                        newest = currentList[0]
                        pass
                    else:
                        # 第一次里面没数据，就不考虑

                        pass
                    currentList = []
                    currentList.append(onedata)
                if newest:
                    all_need_insert_mysql += 1
                    qyxx_id = newest.get('bbd_qyxx_id')
                    # print newest['bbd_qyxx_id']
                    cmd = """SELECT * from qyxx_basic where bbd_qyxx_id='{0}'""".format(qyxx_id)

                    cursor.execute(cmd)
                    # 使用 fetchone() 方法获取一条数据库。

                    resultList = cursor.fetchall()
                    if len(resultList) > 1:
                        print u"mysql multi record id：%s" % qyxx_id
                    elif len(resultList) == 0:
                        print u"mysql no record,id：%s" % qyxx_id

                    for row in resultList:
                        f1 = row[13] == newest['company_name']
                        f2 = row[11] == newest['company_enterprise_status']
                        datemysql = re.compile('[^0-9]').sub('', str(row[3]))
                        datees = re.compile('[^0-9]').sub('', newest['approval_date'])
                        f3 = datemysql == datees
                        location = newest['type']
                        if u'北京' in location:
                            location = u'北京'
                        f4 = row[14] == location
                        if any(not c for c in (f1, f2, f3, f4)):
                            if all_err > 10000:
                                exit(0)
                            all_err += 1
                            print u'insert wrong to mysql，id:【%s】' % qyxx_id
            except Exception as e:
                print 'err:' + str(e)
                try:
                    print json.dump(hit, ensure_ascii=False)
                except:
                    pass

    print 'total!:%d into mysql' % all_need_insert_mysql
