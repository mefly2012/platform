# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_nyscqyzzcx():
    """农药生产企业资质"""
    need_check_ziduan = [
        'company_name'
    ]

    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret
