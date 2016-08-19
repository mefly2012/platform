# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re




class overseas_investment():
    """境外投资"""
    need_check_ziduan = [u'country_region',
                         u'domestic_invest_subject',
                         u'approval_date',
                         u'foreign_invest_enterprises',
                         u'bbd_dotime'
                         ]
    def check_country_region(self, indexstr, ustr):
        """国家/地区 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', ustr):
                ret = u"包含半角括号"

        return ret

    def check_domestic_invest_subject(self, indexstr, ustr):
        """境内投资主体 校验
            不可为空
        """
        ret = None
        SPECIAL_STR = u"[ 　.。#＃,，?？/、\\`~；;•·$￥@！!^…＇’‘＊*%]"
        SPECIAL_STR2 = u"[^ 　.。#＃,，?？/、\\`~；;•·$￥@！!^…＇’‘＊*%]"
        if ustr and len(ustr):
            if re.compile(u'[()]').search(ustr):
                ret = u'包含半角括号'
            elif re.compile(SPECIAL_STR).search(ustr):
                all_str = re.compile(SPECIAL_STR2).sub('', ustr)
                if public.is_allchinese(all_str):
                    ret = u"全中文包含特殊字符"
        return ret

    def check_approval_date(self, indexstr, ustr):
        """核准日期 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_foreign_invest_enterprises(self, indexstr, ustr):
        """境外投资企业（机构） 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', ustr):
                ret = u"包含半角括号"
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验
            可为空
        """
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
