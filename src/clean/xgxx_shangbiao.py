# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re




class xgxx_shangbiao():
    """商标"""

    need_check_ziduan = [u'bbd_dotime',
                         u'company_name',
                         u'applicant_name',
                         u'product_list',
                         u'similar_groups'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 校验
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

    def check_applicant_name(self, indexstr, ustr):
        """申请人名称 校验
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

    def check_product_list(self, indexstr, ustr):
        """商品/服务列表 校验
        """
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"包含半角括号"
        return ret

    def check_similar_groups(self, indexstr, ustr):
        """类似群 校验
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u' 　' for c in unicode(ustr)):
                ret = u"存在空格" + u'{0} ：{1}'.format(indexstr, ustr)
            elif re.compile('\d{5,}').search(ustr):
                ret = u"连续五个以上数字未分组"
        return ret
