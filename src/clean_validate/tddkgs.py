# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class tddkgs():
    """中标"""

    need_check_ziduan = [
        u'key',
        u'_id',
        u'data_source',
        u'main',
        u'bbd_url',
        u'title',
        u'main_source_code',
        u'bbd_version',
        u'url',
        u'rawdata',
        u'bbd_uptime',
        u'district',
        u'uuid',
        u'date',
        u'retain1',
        u'retain2',
        u'bbd_dotime',
        u'bbd_source'
    ]

    def check_key(self, indexstr, ustr):
        """key 清洗验证"""
        ret = None

        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_data_source(self, indexstr, ustr):
        """datasource 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_main(self, indexstr, ustr):
        """main 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """URL 清洗验证"""
        ret = None

        return ret

    def check_title(self, indexstr, ustr):
        """title 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_main_source_code(self, indexstr, ustr):
        """main_source_code 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None

        return ret

    def check_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_rawdata(self, indexstr, ustr):
        """rawdata 清洗验证"""
        ret = None

        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_district(self, indexstr, ustr):
        """district 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有一个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_uuid(self, indexstr, ustr):
        """uuid 清洗验证"""
        ret = None

        return ret

    def check_date(self, indexstr, ustr):
        """date 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_retain1(self, indexstr, ustr):
        """retain1 清洗验证"""
        ret = None

        return ret

    def check_retain2(self, indexstr, ustr):
        """retain2 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
