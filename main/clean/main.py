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

from bin.base.for_es import es
from bin.base.for_hbase import hbase
from bin.base.for_kafka import kfk
from bin.base.for_single_file import single_file
from logs import logconfig

doc_types_clean = [
    # 'ktgg',                                    #开庭公告
    # 'zgcpwsw',                                 #裁判文书

    # 'ktgg',
    # 'cdfy_sfgk',
    # 'newktgg',
    # 'zyktgg',
    # 'zgcpwsw',
    # 'itslaw',
    # 'qyxg_zgcpwsw',
    # 'qyxg_wscpws',
    #
    # 'zhixing',                                 #被执行人
    # 'dishonesty',                              #失信被执行人
    # 'recruit',                                 #招聘
    # 'xgxx_shangbiao',                          #商标
    # 'shgy_zhaobjg',                            #中国国际中标网-招标公告
    # 'shgy_zhongbjg',                           #中国国际中标网-中标公告
    # 'rmfygg',                                  #人民法院公告
    # 'overseas_investment',                     #境外投资
    # 'qyxx_wanfang_zhuanli',                    #万方专利
    # 'tddy',                                    #土地抵押
    # 'tdzr',                                    #土地转让
    # 'dcos',                                    #双软认证
    # 'qyxx_enterpriseQualificationForeign',     #通信建设企业资质
    # 'qyxx_gcjljz',                             #工程监理资质
    # 'qyxx_jzsgxkz',                            #建筑施工许可证
    # 'qyxx_miit_jlzzdwmd',                      #信息系统工程监理资质
    # 'qyxx_food_prod_cert',                     #食品生产许可证
    # 'qyxx_haiguanzongshu',                     #海关登记信息
    # 'qyxx_gmpauth_prod_cert',                  #GMP认证
    # 'qyxx_hzp_pro_prod_cert',                  #化妆品生产许可证
    # 'qyxx_medi_jy_prod_cert',                  #药品经营许可证
    # 'qyxx_medi_pro_prod_cert',                 #药品生产许可证
    # 'qyxx_industrial_production_permit',       #工业产品生产许可证
    # 'qyxx_nyscqyzzcx',                         #农药生产企业资质
    # 'qyxx_tk',                                 #采矿权许可证
    # 'qyxx_ck',  # 探矿权许可证
    # 'xzcf',                                    #行政处罚
    # 'rjzzq',                                   #计算机软件著作权登记公告
    # 'qyxx_finance_xkz',                        #金融许可证
    # 'qylogo',                                  #企业logo
    # 'ssgs_zjzx',                               #上市公司数据-中金在线
    # 'simutong',                                #私募通
    # 'tddkgs',                                  #土地市场-地块公示
    # 'shgy_tdcr',                               #中国土地市场网-土地出让
    # 'qyxx_zhuanli',                            #专利数据抓取——通过官网（时间搜索）
    # 'zhuanli_zhuanyi',                         #专利转移
    # 'zpzzq',                                   #作品著作权登记公告爬虫
    # 'zuzhijigoudm',                             #组织机构代码
    # 'baidu_news',
    #'sfpm_taobao',  # 司法拍卖淘宝网
    # 'gdsw_all_info',  # 企业欠税
    # 'hnsw_all_info',  # 企业欠税
    # 'jyyc',#经营异常
    # 'jijinye_info',#中国基金业协会
    # 'ygcq_gzgg',#阳光产权
    # 'ygcq_zb',#阳光产权招标
    # 'ddb_gzjfw_zhaobiao',
    # 'guizhou_zhaobiao',
    # 'ddb_gzjfw_zhongbiao',#中标
    # 'guizhou_zhongbiao',
    # 'domain_name_website_info',#企业网站信息
    # 'qyxg_baidutiebawt',#百度贴吧
    # 'qyxg_sinablog_data',#新浪博客
    # 'qyxg_wechatofficialid',#微信公众号
    'qyxg_xinwenyuqing_data',#新闻舆情
]


err_file_path = os.path.split(os.path.realpath(__file__))[0]

to_run = 'clean'
run_type = 'single_file'
doc_types = doc_types_clean

if __name__ == '__main__':
    logconfig.init_log(to_run + '.log')

    if run_type == 'es':
        ip_port = ['c4node27:59200', 'c4node28:59200', 'c4node29:59200']
        db_index = 'dp_basic_v1'
        for doc_type in doc_types:
            mod = __import__('src.' + to_run + '.' + doc_type, fromlist=[doc_type])
            if hasattr(mod, doc_type):
                need_check_instance = getattr(mod, doc_type)()
                m = es.check_base(1, ip_port=ip_port, db_index=db_index, doc_type=doc_type, total=100, need_to_check=need_check_instance,
                                  err_file_path=err_file_path)
                m.run()
    elif run_type == 'hbase':
        host = 'c5node6'
        for doc_type in doc_types:
            WANT_TO_GET = 'BASIC_' + doc_type.upper()
            mod = __import__('src.' + to_run + '.' + doc_type, fromlist=[doc_type])
            if hasattr(mod, doc_type):
                need_check_instance = getattr(mod, doc_type)()
                m = hbase.check_base(host=host, table=WANT_TO_GET, total=0, need_to_check=need_check_instance, err_file_path=err_file_path)
                m.run()
    elif run_type == 'single_file':
        doc_path = err_file_path
        for doc_type in doc_types:
            WANT_TO_GET = '' + doc_type
            #WANT_TO_GET = '' + doc_type
            if not os.path.exists(os.path.join(doc_path, doc_type)):
                # 解析层 /user/bbdhadoop/20160705_parser/
                # 入库层 /user/bbdhadoop/20160705/
                # 解析验证层 /user/dataom/20160705_validate_parse
                # + '/part-00000'
                # +'/success/part-00000'

                # add_path='/success/*'
                # if WANT_TO_GET in (U'DISHONESTY', u'ZHIXING'):
                #     add_path = '/spilt/*'
                os.system('hadoop fs -getmerge  /user/dataom/20160801-cleaner/' + WANT_TO_GET + ' ' + doc_path + os.sep + doc_type)#解析层
                #os.system('hadoop fs -getmerge  /user/dataom/20160705_validate_parse/' + WANT_TO_GET + add_path + ' ' + doc_path + os.sep + doc_type)

            mod = __import__('src.' + to_run + '.' + doc_type, fromlist=[doc_type])
            if hasattr(mod, doc_type):
                need_check_instance = getattr(mod, doc_type)()
                m = single_file.check_base(1, db_index=doc_path, doc_type=doc_type, total=0, need_to_check=need_check_instance,
                                           err_file_path=err_file_path)
                m.run()
                if 'nt' not in os.name:  # 如果在windows上就不删除
                    os.system('rm ' + doc_path + os.sep + doc_type)
    elif run_type == 'kafka':
        ip_port = 'c5node1:9092,c5node2:9092,c5node3:9092,c5node4:9092,c5node5:9092,c5node6:9092,c5node7:9092,c5node8:9092'
        topic = 'bbd_queue_test_parser_20160705'
        instances = {}
        for doc_type in doc_types:
            mod = __import__('src.' + to_run + '.' + doc_type, fromlist=[doc_type])
            if hasattr(mod, doc_type):
                instance = getattr(mod, doc_type)()
                instances[doc_type] = instance

        m = kfk.check_base(ip_port=ip_port, topic=topic, frm=0, total=100, err_file_path=err_file_path, instances=instances, tables=doc_types)
        m.run()
