# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class tdzr():
    """土地转让"""

    need_check_ziduan = [
        'landno',
        'original_usename',
        'land_use_period',
        'land_usetype',
        'transaction_time',
        'current_usename'
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

    def check_original_usename(self, indexstr, ustr):
        """原土地使用权人"""
        """按以下顺序清洗数据：
        1、将空格（包含多个空格）且空格两边的任意一边有单个汉字的内容，去掉其空格（可参考案例1）
        2、将空格两边都是汉字的空格替换为英文分号“;”（可参考案例2）
        3、将“、”“\\””\”都替换为英文分号“;”
        4、将所有半角括号“()”“[]”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u"、 　\\)([]］［"
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_land_use_period(self, indexstr, ustr):
        """土地使用年限"""
        """统一日期格式：yyyy年mm月dd日 """
        ret = None
        # if ustr and len(ustr):邮件06-06 12:01
        #     if not public.date_format(ustr):
        #         ret = u'不合法日期'
        return ret

    def check_land_usetype(self, indexstr, ustr):
        """土地使用权类型"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret

    def check_transaction_time(self, indexstr, ustr):
        """成交时间"""
        """统一日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_current_usename(self, indexstr, ustr):
        """现土地使用权人"""
        """按以下顺序清洗数据：
        1、将“、”或中文逗号“，”或英文括号“,”或“，”或“\\”或“\”或“/”或“//”替换为英文分号“;”
        2、将所有半角括号“()”及“[]”都转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u"、，/\\)([]］［"
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret
