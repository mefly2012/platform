# coding=utf-8



import json
import codecs
import os
import sys
import re

if __name__ == '__main__':
    fr1 = codecs.open(sys.argv[1], 'r', encoding='utf-8')  # 我统计的
    fr2 = codecs.open(sys.argv[2], 'r', encoding='utf-8')  # 君哥统计的

    dics1 = []
    dics2 = []
    for i in fr1:
        js = json.loads(i)
        js["bbd_dotime"] = js.get("bbd_dotime").replace(u'年', '-').replace(u'月', '-').replace(u'日', '')

        dics1.append(js)
    for i in fr2:
        js = json.loads(i)
        match = re.compile(u'^(\d+).(\d+).(\d+)$').match(js["bbd_dotime"])

        js["bbd_dotime"] = "%4d-%2d-%2d" % (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        dics2.append(js)

    dics1.sort(key=lambda x: x['company_name'])
    dics2.sort(key=lambda x: x['company_name'])
    # sorted(dics1, key=lambda x: x['company_name'])
    # sorted(dics2, key=lambda x: x['company_name'])

    first = True
    company = ''

    myout = []
    current = []
    dics1.append({})

    for dc in dics1:
        if company != dc.get('company_name', ''):
            # 选出时间最大
            if first:
                first = False
                company = dc.get('company_name', '')
                current.append(dc)
                continue

            company = dc.get('company_name', '')
            max_dc = max(current, key=lambda x: x['bbd_uptime'])
            myout.append(max_dc)
            current = []
            current.append(dc)
            pass
        else:
            current.append(dc)

    print len(myout)
    # for i in myout:
    #     find = False
    #     for j in dics2:
    #         if i == j:
    #             find = True
    #     if find:
    #         print json.dumps(i, ensure_ascii=False)
    for i in myout:
        if i not in dics2:
            print json.dumps(i, ensure_ascii=False)
