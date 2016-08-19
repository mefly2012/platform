# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class ygcq_gycqg():
    """阳光产权_国有产权股"""
    need_check_ziduan = [u'listed_startdate',
                         u'listed_endtime',
                         u'object_company_name',
                         u'esdate',
                         u'approve_date',
                         u'valuation_date',
                         u'transfer_name'
                         ]

    def check_listed_startdate(self, source, ustr):
        """挂牌起始日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_listed_endtime(self, source, ustr):
        """挂牌截止日期校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_object_company_name(self, source, ustr):
        """标的企业名称"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'还有半角括号'
        return ret

    def check_esdate(self, source, ustr):
        """成立时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_approve_date(self, source, ustr):
        """核准（备案）日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_valuation_date(self, source, ustr):
        """评估基准日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_transfer_name(self, source, ustr):
        """转让方名称"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'还有半角括号'
        return ret


if __name__ == '__main__':
    pass