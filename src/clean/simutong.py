# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class simutong():
    """私募通"""
    need_check_ziduan = [u'invest_side',
                         u'bbd_dotime',
                         u'invest_time'
                         ]

    def check_invest_side(self, indexstr, ustr):
        """投资方 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()' + public.QUANJIAO_NUM + public.QUANJIAO_EN + u' ') for c in ustr):
                ret = u'有半角括号或者全角数字字母或者半角空格'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_invest_time(self, indexstr, ustr):
        """投资时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
