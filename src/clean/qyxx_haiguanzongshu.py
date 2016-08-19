# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_haiguanzongshu():
    """海关登记信息"""

    need_check_ziduan = [
        'company_name',
        'validdate',
        'customs_code'
    ]
    def check_company_name(self, indexstr, ustr):
        """company_name"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret

    def check_validdate(self, indexstr, ustr):
        """注册有效期"""
        """将“yyyy-mm-dd"、“yyyy-mm-dd hh:mm:ss”“yyyy年mm月dd日 hh时mm分ss秒”等日期格式全部统一成“yyyy年mm月dd日”格式
         """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_customs_code(self, indexstr, ustr):
        """海关编码"""
        """将所有全角数字和字母转换为半角 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
        return ret
