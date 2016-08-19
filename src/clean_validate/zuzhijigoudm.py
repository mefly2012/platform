# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class zuzhijigoudm():
    """中标"""

    need_check_ziduan = [
        u'_id',
        u'bbd_dotime',
        u'jgdjzh',
        u'jgdm',
        u'jgmc',
        u'bbd_uptime',
        u'version',
        u'bbd_source'
    ]

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_jgdjzh(self, indexstr, ustr):
        """jgdjzh 清洗验证"""
        ret = None

        return ret

    def check_jgdm(self, indexstr, ustr):
        """jgdm 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^0-9a-zA-Z]').search(ustr):
                ret = u'还有字母数字之外的字符'
            elif all(c in public.BANJIAO_EN for c in ustr):
                ret = u'要纯数字或者数字与字母的组合'
        else:
            ret = u'为空'
        return ret

    def check_jgmc(self, indexstr, ustr):
        """jgmc 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
