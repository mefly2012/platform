# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public



class qyxg_zgcpwsw():
    """开庭公告"""

    need_check_ziduan = [
        'company_name',
        'action_cause',
        'caseout_come',
        'court_litigant',
        'pro_litigant',
        'def_litigant',
        'pro_other_related',
        'def_other_related',
        'court_acceptance_fee',
        'historycase'
    ]
    def check_company_name(self, indexstr, ustr):
        """company_name"""
        """不可为空，至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_action_cause(self, indexstr, ustr):
        """案由"""
        """可为空，若非空至少包含2个中文汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有5个以上汉字'
        return ret

    def check_caseout_come(self, indexstr, ustr):
        """案件结果"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None

        return ret

    def check_court_litigant(self, indexstr, ustr):
        """法院当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_pro_litigant(self, indexstr, ustr):
        """起诉方当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_def_litigant(self, indexstr, ustr):
        """被诉方当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_pro_other_related(self, indexstr, ustr):
        """起诉方其他相关人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_def_other_related(self, indexstr, ustr):
        """被诉方其他相关人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字页没有2个英文字母'
        return ret

    def check_court_acceptance_fee(self, indexstr, ustr):
        """受理费"""
        """可为空，若非空为数字+单位的格式"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{1,}(元|\$)$').match(ustr):
                ret = u'不符合格式数字+单位'
        return ret

    def check_historycase(self, indexstr, ustr):
        """历审案例"""
        """可为空，必须全为汉字，且包含“法院”两字"""
        ret = None
        if ustr and len(ustr):
            if public.is_allchinese(ustr):
                if u'法院' not in ustr:
                    ret = u'不包含法院二字'
            else:
                ret = u'不全为汉字'
        return ret
