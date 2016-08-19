# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class zyktgg():
    """开庭公告"""

    need_check_ziduan = ['main',
                         'city',
                         'bbd_dotime',
                         'title'
                         ]

    def check_main(self, indexstr, ustr):
        """main 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'不包含中文'
        else:
            ret = u'为空'
        return ret

    def check_city(self, indexstr, ustr):
        """city 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in public.PROVINCE:
                ret = u'非法的省名'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_title(self, indexstr, ustr):
        """title 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if all(not public.is_chinese(c) for c in ustr):
                ret = u'没有中文'
            elif not len(ustr) >= 5:
                ret = u'不够5个字以上'
        return ret
