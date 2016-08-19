# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_gmpauth_prod_cert():
    """GMP认证"""
    need_check_ziduan = [
        'company_name',
        'issue_date',
        'valid_period',
        'certificate_no',
        'continue_legalize_scope',
        'continue_date',
        'validdate'
    ]
    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_valid_period(self, indexstr, ustr):
        """有效期/有效期截止日"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号/许可证编号"""
        """将所有的全角数字和字母转换为半角，且将数字、字母、汉字以外的字符去掉 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
            else:
                sub = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5]').sub('', ustr)
                if len(sub) > 0:
                    ret = u'还有其他字符'
        return ret

    def check_continue_legalize_scope(self, indexstr, ustr):
        """批准延续的认证范围"""
        """①将所有半角括号“()”“【】”“[]”转换成全角括号“（）”
        ②删掉全半角状态下的空格。： """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[\[\])(【】 　 ］［]').search(ustr):
                ret = u'还有特殊字符'
        return ret

    def check_continue_date(self, indexstr, ustr):
        """批准延续日期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期延续至"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret
