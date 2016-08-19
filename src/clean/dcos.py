
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class dcos():
    """双软认证"""
    need_check_ziduan = [
        'original_company_name',
        'company_name',
        'original_frname',
        'frname',
        'certificate_num',
        'regdate',
        'issue_date'
    ]
    def check_original_company_name(self, indexstr, ustr):
        """原企业名称"""
        """1、将“、”替换为英文分号“;”
        2、将所有半角括号“()”转换成全角括号“（）”
        3、需要处理的字符：全半角状态下的：空格 . 。 #  *  , ，  ?  / \ ` ； ; ？· $ ￥ @ ！^  … """
        ret = None
        SPECIAL_STR = u"、 　.。#＃＊*×,，?？/\\／＼＇'；~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """1、将“、”替换为英文分号“;”
        2、将所有半角括号“()”转换成全角括号“（）”
        3、需要处理的字符：全半角状态下的：空格 . 。 #  *  , ，  ?  / \ ` ； ; ？· $ ￥ @ ！^  … """
        ret = None
        SPECIAL_STR = u"、 　.。#＃＊*×,，?？/\\／＼＇'；~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_original_frname(self, indexstr, ustr):
        """原法定代表人"""
        """1、将所有半角括号“()”转换成全角括号“（）”
        2、需要处理的字符：全半角状态下的：空格 . 。 #  *  , ，  ?  / \ ` ； ; ？· $ ￥ @ ！^  … """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人"""
        """1、将所有半角括号“()”转换成全角括号“（）”
        2、需要处理的字符：全半角状态下的：空格 . 。 #  *  , ，  ?  / \ ` ； ; ？· $ ￥ @ ！^  … """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_certificate_num(self, indexstr, ustr):
        """证书编号"""
        """将全角的数字和英文转变半角数字和英文 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM+public.QUANJIAO_EN) for c in ustr ):
                ret = u'还有全角字母或者数字'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记日期"""
        """统一日期格式：“yyyy年mm月dd日” """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """认定日期"""
        """统一日期格式：“yyyy年mm月dd日” """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret
