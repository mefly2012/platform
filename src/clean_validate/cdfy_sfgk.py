# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re

from common import public




class cdfy_sfgk():
    """开庭公告"""
    need_check_ziduan = ['main',
                         'city',
                         'action_cause',
                         'litigant',
                         'case_code',
                         'trial_date',
                         'bbd_dotime',
                         'title'
                         ]
    def check_main(self, indexstr, ustr):
        """main 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if all(not public.is_chinese(c) for c in ustr):
                ret = u'不包含中文'
        else:
            ret = u'为空'
        return ret

    def check_city(self, indexstr, ustr):
        """city 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'四川':
                ret = u'不是四川'
        else:
            ret = u'为空'
        return ret

    def check_action_cause(self, indexstr, ustr):
        """案由 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有中文'
        return ret

    def check_litigant(self, indexstr, ustr):
        """当事人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_en(ustr, 2) and \
                    not public.has_count_hz(ustr, 2):
                ret = u'既没有2个中文也没有2个英文'
        else:
            ret = u'为空'
        return ret

    def check_case_code(self, indexstr, ustr):
        """案号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not (re.compile(ur'[\u4e00-\u9fa5]').search(ustr) or
                        re.compile(u'[0-9]').search(ustr)):
                ret = u'又没中文又没数字'
        return ret

    def check_trial_date(self, indexstr, ustr):
        """开庭日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_title(self, indexstr, ustr):
        """main 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有中文'
            elif len(ustr) < 5:
                ret = u'不够5个长度'
        return ret
