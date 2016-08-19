# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class qyxg_wscpws():
    need_check_ziduan = [u'caseOutcome',
                         u'litigantType',
                         u'courtAcceptance_fee',
                         u'doc_Type',
                         u'historyCase'
                         ]

    def check_caseOutcome(self, source, ustr):
        """案件结果"""
        ret = None

        return ret

    def check_litigantType(self, source, ustr):
        """当事人类型"""
        ret = None

        return ret

    def check_courtAcceptance_fee(self, source, ustr):
        """受理费"""
        ret = None
        return ret

    def check_doc_Type(self, source, ustr):
        """文书类型"""
        ret = None
        return ret

    def check_historyCase(self, source, ustr):
        """历审案例"""
        ret = None
        return ret
