
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class gdsw_all_info():
    """企业欠税"""
    need_check_ziduan = [
        'defaulteroftax_name'
    ]
    def check_defaulteroftax_name(self, indexstr, ustr):
        """欠税人名称"""
        """（1）需要处理的字符：全半角状态下的：空格 . 。 #  *  , ， 、 ?  / \ ` ； ; ？· $ ￥ @ ！^  …‘
            （2）将所有半角括号“()”转换成全角括号“（）”"
        """
        ret = None
        SPECIAL_STR = u"、 　.。#＃＊*×,，?？/\\／＼＇'；~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret
