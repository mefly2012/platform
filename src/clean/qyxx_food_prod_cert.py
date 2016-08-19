# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_food_prod_cert():
    """食品生产许可证"""

    need_check_ziduan = [
        'company_key',
        'company_name',
        'location',
        'issue_date',
        'validdate',
        'certificate_no'
    ]

    def check_company_key(self, indexstr, ustr):
        """company_key"""
        """（1）需要处理的字符：全半角状态下的：空格 . 。 #  *  , ， 、 ?  / \ ` ； ; ？· $ ￥ @ ！^  …‘                                                                                  
        （2）将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """（1）需要处理的字符：全半角状态下的：空格 . 。 #  *  , ， 、 ?  / \ ` ； ; ？· $ ￥ @ ！^  …‘                                                                                  
        （2）将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_location(self, indexstr, ustr):
        """住所"""
        """（1）需要将所有半角括号“()”转换成全角括号“（）”
        （2）需要将“\\”“/”“—”替换为空值 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有特殊字符'
            elif ustr in (u'\\\\', u'/'):
                ret = u'没有替换为空'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期"""
        """日期统一成“yyyy年mm月dd日”格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_validdate(self, indexstr, ustr):
        """证书有效期"""
        """日期统一成“yyyy年mm月dd日”格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号"""
        """（1）将全角数字转为半角数字
        （2）将全角字母转为半角字母
        （3）删除全半角状态下的空格 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN + u' 　') for c in ustr):
                ret = u'还有全角字母或者数字或空格'
        return ret
