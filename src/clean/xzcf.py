# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class xzcf():
    """万方专利"""

    need_check_ziduan = [u'punish_code',
                         u'public_date',
                         u'name'
                         ]
    def check_punish_code(self, indexstr, ustr):
        """文书号 校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'[]\＼［〔〕］【】()',ustr):
                ret = u'还有特殊字符'
        return ret

    def check_public_date(self, indexstr, ustr):
        """发布日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_name(self, indexstr, ustr):
        """处罚对象 校验"""
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret
