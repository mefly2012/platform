# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class shgy_zhaobjg():
    """招标"""

    need_check_ziduan = [u'bbd_dotime',
                         u'main',
                         u'title',
                         u'city',
                         u'industry',
                         u'source_funds',
                         u'pubdate',
                         u'data_sources'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_main(self, indexstr, ustr):
        """main 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        return ret

    def check_title(self, indexstr, ustr):
        """title 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"没有包括至少两个汉字"
        else:
            ret = u"为空"
        return ret

    def check_city(self, indexstr, ustr):
        """地区 清洗验证"""
        ret = None

        return ret

    def check_industry(self, indexstr, ustr):
        """行业 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u'没有包括至少两个汉字'
        return ret

    def check_source_funds(self, indexstr, ustr):
        """资金来源 清洗验证"""
        ret = None

        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u"为空了"
        return ret

    def check_data_sources(self, indexstr, ustr):
        """数据来源 清洗验证"""
        ret = None

        return ret
