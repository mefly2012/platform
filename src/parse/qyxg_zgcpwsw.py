# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_zgcpwsw():
    need_check_ziduan = [u'title',
                         u'main',
                         u'casecode',
                         u'sentence_date',
                         u'applicable_law',
                         u'update'
                         ]

    def check_title(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'有特殊符号'
            else:
                try:
                    tmp = eval(ustr)
                    if not isinstance(tmp, (int, float)):
                        ret = u'还有unicode码'
                except Exception as e:
                    pass
        return ret

    def check_main(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'有特殊符号'
            else:
                try:
                    tmp = eval(ustr)
                    if not isinstance(tmp, (int, float)):
                        ret = u'还有unicode码'
                except Exception as e:
                    pass
        return ret

    def check_casecode(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'有特殊符号'
            else:
                try:
                    tmp = eval(ustr)
                    if not isinstance(tmp, (int, float)):
                        ret = u'还有unicode码'
                except Exception as e:
                    pass
        return ret

    def check_sentence_date(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_applicable_law(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'有特殊符号'
            else:
                try:
                    tmp = eval(ustr)
                    if not isinstance(tmp, (int, float)):
                        ret = u'还有unicode码'
                except Exception as e:
                    pass
        return ret

    def check_update(self, source, ustr):
        """裁判日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
