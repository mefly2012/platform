# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class simutong():
    """中标"""

    need_check_ziduan = [
        u'investors',
        u'_id',
        u'invest_side',
        u'bbd_version',
        u'invest_event_title',
        u'src_data',
        u'financing_side',
        u'bbd_uptime',
        u'invest_region',
        u'invest_event',
        u'invest_stage',
        u'capcur',
        u'invest_amount',
        u'bbd_dotime',
        u'invest_time',
        u'invert_round',
        u'bbd_source'
    ]

    def check_investors(self, indexstr, ustr):
        """投资行业 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_invest_side(self, indexstr, ustr):
        """投资方 清洗验证"""
        ret = None
        # if public.str_empty(indexstr,ustr):
        #     ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u"类型不正确"
        return ret

    def check_invest_event_title(self, indexstr, ustr):
        """投资事件标题 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_src_data(self, indexstr, ustr):
        """src_data 清洗验证"""
        ret = None

        return ret

    def check_financing_side(self, indexstr, ustr):
        """融资方 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_invest_region(self, indexstr, ustr):
        """投资地区 清洗验证"""
        ret = None
        # if public.str_empty(indexstr,ustr):
        #     ret = u'为空'
        return ret

    def check_invest_event(self, indexstr, ustr):
        """投资事件 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_invest_stage(self, indexstr, ustr):
        """投资阶段 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'初创期', u'成熟期', u'种子期', u'扩张期'):
                ret = u'不是指定字段'
        # else:
        #     ret = u'为空'
        return ret

    def check_capcur(self, indexstr, ustr):
        """币种 清洗验证"""
        ret = None

        return ret

    def check_invest_amount(self, indexstr, ustr):
        """投资金额 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_invest_time(self, indexstr, ustr):
        """投资时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_invert_round(self, indexstr, ustr):
        """投资轮次 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.all_english(ustr):
        #         ret = u"格式不正确"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
