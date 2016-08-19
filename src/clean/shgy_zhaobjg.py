# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class shgy_zhaobjg():
    """招标"""
    need_check_ziduan = [u'bbd_dotime',
                         u'title',
                         u'pubdate'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_title(self, indexstr, ustr):
        """tile 校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"title包含半角括号"
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
