# -*- coding: utf-8 -*-
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class zuzhijigoudm():
    """组织机构代码"""
    need_check_ziduan = [u'bbd_dotime',
                         u'jgdjzh',
                         u'jgdm',
                         u'jgmc'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_jgdjzh(self, indexstr, ustr):
        """jgdjzh 校验"""
        ret = None
        if ustr and len(ustr):
            try:
                tmp = eval(ustr)
                if isinstance(tmp, (int, float)):
                    ret = u'还有unicode码'
            except Exception as e:
                pass
        return ret

    def check_jgdm(self, indexstr, ustr):
        """jgdm 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_jgmc(self, indexstr, ustr):
        """jgmc 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'有特殊符号'
            else:
                try:
                    tmp = eval(ustr)
                    if isinstance(tmp, (int, float)):
                        ret = u'还有unicode码'
                except Exception as e:
                    pass

        return ret
