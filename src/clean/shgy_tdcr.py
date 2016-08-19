# -*- coding: utf-8 -*-
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class shgy_tdcr():
    """万方专利"""
    need_check_ziduan = [u'bbd_dotime',
                         u'convention_starting_time',
                         u'contract_date',
                         u'actual_starting_time',
                         u'project_name',
                         u'electron_supervise',
                         u'convention_endtime',
                         u'actual_completion_date',
                         u'agreed_delivery_time',
                         u'original_usename',
                         u'approval_unit',
                         u'deal_price_millon',
                         u'land_use_period',
                         u'contract_volume_ratelower',
                         u'contract_volume_rateupper',
                         u'payable_contract'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_convention_starting_time(self, indexstr, ustr):
        """约定开工时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_contract_date(self, indexstr, ustr):
        """合同签订日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_actual_starting_time(self, indexstr, ustr):
        """实际开工时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_project_name(self, indexstr, ustr):
        """项目名称 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()'+public.QUANJIAO_NUM+public.QUANJIAO_EN) for c in ustr):
                ret = u'有半角括号或者全角数字字母'
        return ret

    def check_electron_supervise(self, indexstr, ustr):
        """电子监管号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN+public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_convention_endtime(self, indexstr, ustr):
        """约定竣工时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_actual_completion_date(self, indexstr, ustr):
        """实际竣工时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_agreed_delivery_time(self, indexstr, ustr):
        """约定交地时间 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
    def check_original_usename(self, indexstr, ustr):
        """土地使用权人 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()'+public.QUANJIAO_NUM+public.QUANJIAO_EN) for c in ustr):
                ret = u'有半角括号或者全角数字字母'
        return ret

    def check_approval_unit(self, indexstr, ustr):
        """批准单位 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_deal_price_millon(self, indexstr, ustr):
        """成交价格（万元） 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_land_use_period(self, indexstr, ustr):
        """土地使用年限 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_contract_volume_ratelower(self, indexstr, ustr):
        """约定容积率下限 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_contract_volume_rateupper(self, indexstr, ustr):
        """约定容积率上限 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_payable_contract(self, indexstr, ustr):
        """分期支付约定 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret
