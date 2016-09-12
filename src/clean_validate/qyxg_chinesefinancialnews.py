# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_chinesefinancialnews():
    need_check_ziduan = [
        'bbd_table',
        'search_key'
    ]

    def check_bbd_table(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'不为空'
        return ret

    def check_search_key(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'不为空'
        return ret
