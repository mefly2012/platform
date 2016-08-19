# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public





class qyxx_gcjljz():
    """工程监理资质"""

    need_check_ziduan = [
        'company_name',
        'location',
        'certificate_no',
        'business_scope',
        'issue_date',
        'validdate'
    ]
    def check_company_name(self, indexstr, ustr):
        """单位名称"""
        """（1）需要处理的字符：全半角状态下的：空格 . 。 #  *  , ， 、 ?  / \ ` ； ; ？· $ ￥ @ ！^  …‘                                                                                  
        （2）将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_location(self, indexstr, ustr):
        """所在省"""
        """将所有包含以下关键字的value：“安徽”、“北京”、“福建”、“甘肃”、“广东”、“广西”、“贵州”、“海南”、“河北”、“河南”、“黑龙江”、“湖北”、“湖南”、“吉林”、“江苏”、“江西”、“辽宁”、“内蒙”、“宁夏”、“青海”、“山东”、“山西”、“陕西”、“上海”、“四川”、“天津”、“西藏”、“新疆”、“云南”、“浙江”、“重庆”对应替换为“安徽”、“北京”、“福建”、“甘肃”、“广东”、“广西”、“贵州”、“海南”、“河北”、“河南”、“黑龙江”、“湖北”、“湖南”、“吉林”、“江苏”、“江西”、“辽宁”、“内蒙古”、“宁夏”、“青海”、“山东”、“山西”、“陕西”、“上海”、“四川”、“天津”、“西藏”、“新疆”、“云南”、“浙江”、“重庆” """
        ret = None
        if ustr and len(ustr):
            if u'内蒙' in ustr:
                if u'内蒙古' not in ustr:
                    ret = u'没有替换完呢'
                elif u'内蒙古古' in ustr:
                    ret = u'替换过头了吧'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """资质证书编号"""
        """（1）将全角数字转为半角数字
        （2）将全角字母转为半角字母 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
        return ret

    def check_business_scope(self, indexstr, ustr):
        """业务范围"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
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
        """有效期至"""
        """日期统一成“yyyy年mm月dd日”格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret
