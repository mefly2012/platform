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
import os

if __name__ == '__main__':

    # if (len(sys.argv) <= 2):
    #     print 'python xxx.py infile outfile'
    #     exit(0)
    # file_in = codecs.open(sys.argv[1], u'r', encoding='utf-8')
    # file_out = codecs.open(sys.argv[2], 'w', encoding='utf-8')
    if not os.path.exists('file_in'):
        os.system('hadoop fs -getmerge /user/dataom/BUSINESS_REAL_TIME_BBD_HIGGS_QYXX_20160816/ file_in')

    file_in = codecs.open('file_in', u'r', encoding='utf-8')
    file_out = codecs.open('myout3', 'w', encoding='utf-8')
    guoziwei = u'(国资委|国有资产委员会|国有资产监督管理局|国务院|国资办|国有资产管理局|国有资产管理中心|国资局|国有资产经营管理中心|国有资产管理运营中心|国有资产监督管理委员会|国有资产管理办公室|国有资产管理委员会|国有资产管理委|国有资产管理股|国有资产监督委员会|国有资产经营中心|国有资产管理委员会办公室|国有资产运营中心|国有资产经营评估中心|国有资产监督管理办公室|国有资产办公室|国有资产营运中心|国有资产监督管理中心|国有资产经营管理办公室|人民政府|财政局)'

    url_path = u"http://125.65.43.222:81/dataspec/apitadcompdesc/?debug=true"
    resp = requests.get(url_path, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36'})
    duiying = {}
    if resp.status_code == 200:
        data = resp.json().get('rdata', [])
        for d in data:
            try:
                duiying[d.get('companytype', 'nodate')] = int(d.get('type_code', '0'))
            except:
                print json.dumps(d, ensure_ascii=False)
    else:
        print 1223344555

    all_count = 0
    err_count = 0
    guoziwei_cout = 0
    no_type_num = 0
    for line in file_in:
        all_count += 1
        if (all_count % 100000) == 0:
            print all_count
        try:
            obj = json.loads(line.strip())
            # check
            flag = False
            qyxx_basic0 = json.loads(obj.get('qyxx_basic', "[{}]"))[0]
            company_type = qyxx_basic0.get('company_type', '')
            if company_type:
                if int(duiying.get(company_type, 0)) in (1110, 1140, 1213, 1223, 3100, 9920):
                    flag = True
            else:
                no_type_num += 1

            if not flag:
                gdxxs = json.loads(obj.get('qyxx_gdxx', '[{}]'))
                for gdxx in gdxxs:
                    company_name = gdxx.get('shareholder_name', '')
                    if re.compile(guoziwei).search(company_name):
                        flag = True
                        break
            if flag:
                guoziwei_cout += 1
                out = {}
                out['bbd_qyxx_id'] = obj.get('bbd_qyxx_id', '')
                out['company_name'] = qyxx_basic0.get('company_name', '')
                out['company_type'] = qyxx_basic0.get('company_type', '')
                out['bbd_uptime'] = qyxx_basic0.get('bbd_uptime', '')
                out['bbd_dotime'] = obj.get('bbd_dotime', '')
                file_out.write(json.dumps(out, ensure_ascii=False))
                file_out.write(os.linesep)


        except Exception as e:
            err_count += 1
            print all_count,
            print str(e)

    print "all_count:%d, err_count:%d,no_type_num:%d, guoziwei_cout:%d" % (all_count, err_count, no_type_num, guoziwei_cout)
