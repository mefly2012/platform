# -*- coding: utf-8 -*-

import os
import sys

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

all_tables = [
    # 'ktgg',
    # 'zgcpwsw',
    # #
    # # # 'ktgg',
    # # # 'cdfy_sfgk',
    # # # 'newktgg',
    # # # 'zyktgg',
    # # # 'zgcpwsw',
    # # # 'itslaw',
    # # # 'qyxg_zgcpwsw',
    # # # 'qyxg_wscpws',
    # #
    # 'zhixing',
    # 'dishonesty',
    # 'recruit',
    # 'xgxx_shangbiao',
    # 'shgy_zhaobjg',
    # 'shgy_zhongbjg',


    # 'rmfygg',
    'overseas_investment',
    # 'qyxx_wanfang_zhuanli',
    'tddy',
    'tdzr',
    'dcos',
    'qyxx_enterpriseQualificationForeign',
    'qyxx_gcjljz',
    'qyxx_jzsgxkz',
    'qyxx_miit_jlzzdwmd',
    'qyxx_food_prod_cert',
    'qyxx_haiguanzongshu',
    'qyxx_gmpauth_prod_cert',
    'qyxx_hzp_pro_prod_cert',
    'qyxx_medi_jy_prod_cert',
    'qyxx_medi_pro_prod_cert',
    'qyxx_industrial_production_permit',
    'qyxx_nyscqyzzcx',
    'qyxx_tk',
    'qyxx_ck',
    'xzcf',
    # 'rjzzq',
    'qyxx_finance_xkz',
    'qylogo',
    'ssgs_zjzx',
    'simutong',
    'tddkgs',
    # 'shgy_tdcr',
    # 'qyxx_zhuanli',
    # 'zhuanli_zhuanyi',
    'zpzzq',
    # 'zuzhijigoudm',

    # 'sfpm_taobao':['title','auctioneer','disposal_unit'],
    # 'domain_name_website_info':['organizer_name','site_certificate_no','domain_name']
]

host = "125.65.78.23"
port = 3306
user = "bbd"
passwd = "bbd-service"
db = "bbd_higgs"
doc_path = os.path.split(os.path.realpath(__file__))[0]
if __name__ == '__main__':
    logconfig.init_log('del_repeat' + '.log')
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #
    #     # 使用execute方法执行SQL语句
    #     cmd = """
    #     SELECT
    # 	table_name,
    # 	DATA_TYPE,
    # 	CHARACTER_MAXIMUM_LENGTH,
    # 	CHARACTER_OCTET_LENGTH
    # FROM
    # 	information_schema. COLUMNS
    # WHERE
    # 	TABLE_SCHEMA = 'bbd_higgs'
    # AND table_name = 'shgy_tdcr'
    # AND COLUMN_NAME = 'bbd_dotime'
    #     """
    #
    #     cursor.execute(cmd)
    #
    #     # 使用 fetchone() 方法获取一条数据库。
    #     data = cursor.fetchone()

    # print data
    all_not_into_mysql = ["bbd_html", "bbd_seed", "bbd_source", "bbd_version",
                          "bbd_qyxx_branch", "bbd_qyxx_branch_id", "bbd_url", "bbd_params", "bbd_customer_name", "bbd_xgxx_date",
                          "bbd_table", "bbd_qyxx_company", "bbd_qyxx_company_id", "_id", "hbase_rowkey", "bbd_error_process",
                          "bbd_html_src", "bbd_error_log", "raw_data"]
    for table_name in all_tables:

        if not os.path.exists(os.path.join(doc_path, table_name)):
            WANT_TO_GET = table_name.upper()
            os.system('hadoop fs -getmerge  /user/dataom/xgxx_dup/' + WANT_TO_GET + ' ' + doc_path + os.sep + table_name)  # 解析层
            # os.system('hadoop fs -getmerge  /user/dataom/xgxx_mysql/' + WANT_TO_GET + ' ' + doc_path + os.sep + table_name+'_mysql')  # 解析层

        all_len = {}
        # 获取到了每个字段的最大值
        err_flag = 0
        err_count = 0
        err_example = ''
        all_count = 0
        fhandle = codecs.open(doc_path + os.sep + table_name, 'r', encoding='utf-8')
        for i in fhandle:
            all_count += 1
            i = i.strip()
            try:
                js = json.loads(i)
            except:
                err_count += 1
                if err_flag == 0:
                    err_example = i

                err_flag = 1
                continue
                pass
            for k, v in js.items():
                if isinstance(v, basestring):
                    all_len[k] = [len(v) if all_len.get(k, [0, ''])[0] < len(v) else all_len.get(k, [0, ''])[0],
                                  v if all_len.get(k, [0, ''])[0] < len(v) else all_len.get(k, [0, ''])[1]]
        all_len_new = {}
        all_len_err = {}
        for k, v in all_len.items():
            if k in all_not_into_mysql:
                # 就不要该字段了
                continue

            cmd = """SELECT table_name,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,CHARACTER_OCTET_LENGTH
        FROM
        	information_schema.COLUMNS
        WHERE
        	TABLE_SCHEMA = 'bbd_higgs'
        AND table_name = '{0}'
        AND COLUMN_NAME = '{1}'
            """.format(table_name, k)

            cursor.execute(cmd)
            # 使用 fetchone() 方法获取一条数据库。
            data = cursor.fetchone()

            data_len = 'type:%-20s,max:%-10d' % ('not_into_mysql', v[0])
            mysql_max_len = None
            if data:
                if data[1] == 'varchar':
                    mysql_max_len = data[2]
                    data_len = 'type:%-20s,max:%-10d,mysql:%-10d,value:%s' % (data[1], v[0], data[2], v[1])
                    if v[0] > mysql_max_len:
                        all_len_err['%-20s' % k] = 'type:%-20s,max:%-10d,mysql:%-10d,value:%s' % ('varchar', v[0], mysql_max_len, v[1])
                else:
                    data_len = 'type:%-20s,max:%-10d,value:%s' % (data[1], v[0], v[1])
            else:
                1 == 1
                pass

            all_len_new['%20s' % k] = data_len

        logging.info(os.linesep)
        logging.info('+' * 40)
        logging.info('all_count：%d' % all_count)
        js = json.dumps(all_len_new, indent=2, ensure_ascii=False)
        jserr = json.dumps(all_len_err, indent=2, ensure_ascii=False)
        logging.info(table_name + '=====' + js)
        logging.info(table_name + '-----' + jserr)
        logging.info('err_count:%d' % err_count)
        logging.info('err_example' + err_example)

        fhandle.close()

        if 'nt' not in os.name:  # 如果在windows上就不删除
            os.system('rm ' + doc_path + os.sep + table_name)
