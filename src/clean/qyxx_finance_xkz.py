# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_finance_xkz():
    """金融许可证"""
    need_check_ziduan = [u'company_name',
                         u'bbd_dotime',
                         u'issue_date',
                         u'approval_esdate'
                         ]
    def check_company_name(self, indexstr, ustr):
        """company_name 校验"""
        ret = None
        if any(c in u')(' for c in ustr):
            ret = u'半角括号'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_approval_esdate(self, indexstr, ustr):
        """批准成立日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
