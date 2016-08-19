# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public




class cdfy_sfgk():
    """开庭公告"""
    need_check_ziduan = [u'city',
                         u'case_code',
                         u'trial_date',
                         u'bbd_dotime',
                         u'title'
                         ]
    def check_city(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if ustr != u'四川':
                ret = u"不为四川"
        return ret

    def check_case_code(self, source, ustr):
        """案号 校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"包含半角括号"
        return ret

    def check_trial_date(self, source, ustr):
        """开庭日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_bbd_dotime(self, source, ustr):
        """bbd_dotime 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_title(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"包含半角括号"
        return ret


if __name__=='__main__':
    a=cdfy_sfgk()
    print a.need_check_ziduan