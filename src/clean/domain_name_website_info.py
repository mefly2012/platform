# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class domain_name_website_info():
    """企业网站信息"""
    need_check_ziduan = [u'bbd_dotime',
                         u'approval_time',
                         u'organizer_name'
                         ]

    ########################规则######################################

    def check_bbd_dotime(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_approval_time(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_organizer_name(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if any(c in ustr for c in u")("):
                ret = u'半角括号'
        return ret
