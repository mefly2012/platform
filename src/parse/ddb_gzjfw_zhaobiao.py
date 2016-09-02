# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ddb_gzjfw_zhaobiao():
    need_check_ziduan = [u'title',
                         u'city',
                         u'pubdate',
                         u'data_sources',
                         u'bidwinning_pubdate'
                         ]

    def check_title(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr and len(ustr):
                if any(c in u')(' for c in ustr):
                    ret = u'有特殊符号'
        return ret

    def check_city(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州':
                ret = u"city不为贵州"
        return ret

    def check_pubdate(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_data_sources(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州公共资源交易中心':
                ret = u"需要等于贵州公共资源交易中心"
        return ret

    def check_bidwinning_pubdate(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
