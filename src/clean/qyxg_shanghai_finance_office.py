# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_shanghai_finance_office():
    need_check_ziduan = [
        'pubdate'
    ]

    def check_pubdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format_with_s(ustr):
                ret = u'不满足yyyy-mm-dd hh:mm:ss'
        return ret
