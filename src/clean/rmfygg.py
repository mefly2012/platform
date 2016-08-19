# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class rmfygg():
    """人民法院公告"""
    need_check_ziduan = [u'bbd_dotime',
                         u'notice_people',
                         u'notice_time',
                         u'litigant'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验
        """
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_notice_people(self, indexstr, ustr):
        """公告人 校验
        """
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"包含半角括号"

        return ret

    def check_notice_time(self, indexstr, ustr):
        """公告时间 校验
        """
        ret = None
        if ustr and len(ustr):
            ustr = unicode(ustr).strip()
            if public.date_format(ustr) != True:
                ret = u"不合法日期"
        return ret

    def check_litigant(self, indexstr, ustr):
        """当事人 校验
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u"()；,，" for c in unicode(ustr)):
                ret = u"存在特殊字符"
            elif unicode(ustr).endswith(':') or unicode(ustr).endswith('：'):
                ret = u"以冒号结尾了"
        return ret
