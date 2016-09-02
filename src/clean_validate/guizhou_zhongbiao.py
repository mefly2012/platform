# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class guizhou_zhongbiao():
    need_check_ziduan = [u'bbd_dotime',
                         u'main',
                         u'title',
                         u'pubdate',
                         u'company_name_invite',
                         u'bidwinning_pubdate'
                         ]

    def check_bbd_dotime(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_main(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_title(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个汉字"
        else:
            ret = u'为空'
        return ret

    def check_pubdate(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_company_name_invite(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u"没有2个汉字又没有2个英文"
        else:
            ret = u'为空'
        return ret

    def check_bidwinning_pubdate(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
