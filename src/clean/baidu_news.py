# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class baidu_news():
    """双软认证"""
    need_check_ziduan = [
        'bbd_dotime',
        'pubdate'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u'不满足日期格式'
        return ret

    def check_pubdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret
