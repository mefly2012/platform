# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_xinwenyuqing_data():
    """双软认证"""
    need_check_ziduan = [
        'time'
    ]

    def check_time(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret
