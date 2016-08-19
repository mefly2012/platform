# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_industrial_production_permit():
    """工业产品生产许可证"""

    need_check_ziduan = [
        'company_name',
        'issue_date',
        'validdate',
        'certificate_no',
        'specification'
    ]

    def check_company_name(self, indexstr, ustr):
        """company_name"""
        """（1）删除以下内容：全半角状态下的：空格 . 。 #  *  , ， 、 ?  / \ ` ； ; ？· $ ￥ @ ！^  …‘
        （2）将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """许可证编号"""
        """将所有全角数字和字母转换为半角 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
        return ret

    def check_specification(self, indexstr, ustr):
        """品种规格"""
        """（1）删掉全半角状态下的空格。：
        （2）将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u" 　)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret
