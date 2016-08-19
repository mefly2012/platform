# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class zgcpwsw():
    """开庭公告"""

    need_check_ziduan = [u'company_name',
                         u'title',
                         u'main',
                         u'casecode',
                         u'sentence_date',
                         u'trial_court'

                         ]

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_en(ustr, 2) \
                    and not public.has_count_hz(ustr, 2):
                ret = u'不包含2中文或者英文字母'
        else:
            ret = u'为空'
        return ret

    def check_title(self, indexstr, ustr):
        """案件标题 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有中文'
            elif any(c in ustr for c in u')('):
                ret = u'有半角括号'
        else:
            ret = u'为空'
        return ret

    def check_main(self, indexstr, ustr):
        """文书内容 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有中文'
        else:
            ret = u'为空'
        return ret

    def check_casecode(self, indexstr, ustr):
        """案号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有中文'
            elif any(c in ustr for c in u')('):
                ret = u'有半角括号'
        else:
            ret = u'为空'
        return ret

    def check_sentence_date(self, indexstr, ustr):
        """裁判日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        else:
            ret = u'为空'
        return ret

    def check_trial_court(self, indexstr, ustr):
        """审理法院 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if u'法院' not in ustr:
                ret = u'没有法院二字'
            elif not public.is_allchinese(ustr):
                ret = u'不全为中文'
        else:
            ret = u'为空'
        return ret
