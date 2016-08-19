# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class tddy():
    """土地抵押"""

    need_check_ziduan = [
        'landno',
        'land_use_warrant',
        'land_rights_no',
        'mortgage_name',
        'mortgage_right_name',
        'mortgagestartdate',
        'mortgage_enddate',
        'mortgage_usetype'
    ]
    def check_landno(self, indexstr, ustr):
        """宗地编号"""
        """1、将只有符号“-”“//”“/”“\\”“\”“_”“---”都替换为“无”
        2、将“【】”“[]”都替换为全角括号“（）”
        3、将全角的数字和英文变为半角的数字和英文 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[\[\]【】］［]').search(ustr):
                ret = u'还有特殊字符'
        elif any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
            ret = u'还有全角字符'
        elif ustr in (u'-', u'_', u'//', u'\\', u'\\\\', u'---'):
            ret = u'没有替换成无'

        return ret

    def check_land_use_warrant(self, indexstr, ustr):
        """土地使用权证号"""
        """2、将“【】”“[]”都替换为全角括号“（）”
        3、将全角的数字和英文变为半角的数字和英文 """
        ret = None
        SPECIAL_STR = u"【】[]］［"
        if ustr and len(ustr):
            if any(c in (SPECIAL_STR + public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_land_rights_no(self, indexstr, ustr):
        """土地他项权利人证号"""
        """1、将只有符号“-”“\\”“\”“、”都替换为空值
        2、将全角的数字和英文变为半角的数字和英文 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角字符'
            elif ustr in (u'-', u'\\', u'\\\\', u'、'):
                ret = u'没有替换成无'
        return ret

    def check_mortgage_name(self, indexstr, ustr):
        """土地抵押人名称"""
        """1、将“。”“、”“\\"“\”英文逗号“,”中文逗号“，”空格（包含多个空格）都替换为英文分号“;”
        2、将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u"、 　。/\\／＼)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_mortgage_right_name(self, indexstr, ustr):
        """土地抵押权人"""
        """1、将“、”或中文逗号“，”及英文逗号“,”都替换为英文分号“;”
        2、将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u"、，,)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_mortgagestartdate(self, indexstr, ustr):
        """土地抵押登记起始日期"""
        """统一日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_mortgage_enddate(self, indexstr, ustr):
        """土地抵押登记结束日期"""
        """统一日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_mortgage_usetype(self, indexstr, ustr):
        """抵押土地权属性质与使用权类型"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret
