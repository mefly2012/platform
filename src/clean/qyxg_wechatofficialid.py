# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_wechatofficialid():
    """微信公众号"""
    need_check_ziduan = [
        'pubdate'
    ]


    def check_pubdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret
