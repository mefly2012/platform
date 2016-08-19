# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public



class newktgg():
    """开庭公告"""
    need_check_ziduan = ['action_cause',
                         'litigant',
                         'case_code',
                         'trial_date'
                         ]

    def check_action_cause(self, indexstr, ustr):
        """案由"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上2个汉字'
        return ret

    def check_litigant(self, indexstr, ustr):
        """当事人"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_en(ustr, 2) \
                    and not public.has_count_hz(ustr, 2):
                ret = u'没有两个中文或2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_case_code(self, indexstr, ustr):
        """案号"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'[\u4e00-\u9fa5]').search(ustr) \
                    or not re.compile(u'[0-9]').search(ustr):
                ret = u'没有中文或者没有数字'
        return ret

    def check_trial_date(self, indexstr, ustr):
        """开庭日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
