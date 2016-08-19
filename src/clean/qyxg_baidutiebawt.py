# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_baidutiebawt():
    """百度贴吧"""
    need_check_ziduan = [
        'company_name'
    ]

    def check_company_name(self, indexstr, ustr):
        ret = None
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

