# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class tddkgs():
    """土地市场-地块公示"""
    need_check_ziduan = [u'key',
                         u'title',
                         u'url',
                         u'rawdata',
                         u'date',
                         u'retain1',
                         u'retain2',
                         u'bbd_dotime'

                         ]
    def check_key(self, indexstr, ustr):
        """key 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_title(self, indexstr, ustr):
        """title 校验"""
        ret = None
        if any(c in u')(' for c in ustr):
            ret = u'半角括号'
        return ret

    def check_url(self, indexstr, ustr):
        """url 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_rawdata(self, indexstr, ustr):
        """rawdata 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_date(self, indexstr, ustr):
        """date 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_retain1(self, indexstr, ustr):
        """retain1 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_retain2(self, indexstr, ustr):
        """retain2 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
