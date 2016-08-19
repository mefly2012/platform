# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qylogo():
    """万方专利"""

    need_check_ziduan = [u'key',
                         u'bbd_url',
                         u'rawdata',
                         u'company_full_name',
                         u'company_short',
                         u'retain1',
                         u'retain2',
                         u'company_logo',
                         u'bbd_dotime'
                         ]

    def check_key(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_rawdata(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_company_full_name(self, indexstr, ustr):
        """ 校验"""
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，、?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_company_short(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_retain1(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_retain2(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_company_logo(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """ 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
