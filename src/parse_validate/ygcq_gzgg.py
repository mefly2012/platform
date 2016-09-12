# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ygcq_gzgg():
    need_check_ziduan = [
        u'pubdate',
    ]

    def check_pubdate(self, source, ustr):
        """发布时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
