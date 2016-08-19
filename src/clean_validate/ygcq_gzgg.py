# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ygcq_gzgg():
    need_check_ziduan = [u'bbd_dotime',
                         u'main',
                         u'title',
                         u'city',
                         u'pubdate',
                         u'data_sources'
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
            if ustr != U'更正公告':
                ret = u"没有更正公告"
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
            if ustr != u'贵州阳光产权':
                ret = u"不为贵州阳光产权"
        else:
            ret = u'为空'
        return ret
