# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class ktgg():
    """开庭公告"""
    need_check_ziduan = [
        u'action_cause',
        u'litigant',
        u'case_code',
        u'trial_date'

    ]
    def check_action_cause(self, source, ustr):
        """"案由"""
        ret = None
        return ret

    def check_litigant(self, source, ustr):
        """当事人"""
        ret = None
        return ret

    def check_case_code(self, source, ustr):
        """案号"""
        ret = None
        return ret

    def check_trial_date(self, source, ustr):
        """开庭日期"""
        ret = None
        return ret
