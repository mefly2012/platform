# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class sfpm_taobao():
    """司法拍卖淘宝网"""
    need_check_ziduan = [u'bbd_dotime'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
