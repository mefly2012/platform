# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ddb_gzjfw_zhongbiao():
    need_check_ziduan = [u'bbd_dotime',
                         u'main',
                         u'title',
                         u'city',
                         u'industry',
                         u'pubdate',
                         u'data_sources',
                         u'bidwinning_pubdate'
                         ]

    def check_bbd_dotime(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_main(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_title(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个汉字"
        else:
            ret = u'为空'
        return ret

    def check_city(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州':
                ret = u"需要等于贵州"
        else:
            ret = u'为空'
        return ret

    def check_industry(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个汉字"
        return ret

    def check_pubdate(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_data_sources(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州公共资源交易中心':
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_bidwinning_pubdate(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
