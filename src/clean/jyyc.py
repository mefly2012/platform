# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class jyyc():
    """经营异常"""
    need_check_ziduan = [u'regno_or_creditcode',
                         u'rank_date',
                         u'remove_date',
                         u'company_name',
                         u'rank_busexcep_date',
                         u'title'
                         ]

    def check_regno_or_creditcode(self, source, ustr):
        """注册号/统一社会信用代码"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5\-]').search(ustr):
                ret = u'还有数字字母汉字-之外的符号'
        return ret

    def check_rank_date(self, source, ustr):
        """列入日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_remove_date(self, source, ustr):
        """移出日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_company_name(self, source, ustr):
        """企业名称"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_rank_busexcep_date(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_title(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if any(x in ustr for x in u')('):
                ret = u'还有半角括号'
        return ret


if __name__ == '__main__':
    a = jyyc()
    print a.check_regno_or_creditcode(1, u'eee我的')