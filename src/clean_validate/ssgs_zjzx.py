# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class ssgs_zjzx():
    """中标"""

    need_check_ziduan = [
        u'_id',
        u'bbd_uptime',
        u'public_offer',
        u'melon_case',
        u'manager_introduction',
        u'company_sitution',
        u'capital_structure',
        u'equity_division',
        u'floati_stockholder',
        u'rationed_shares',
        u'iposhoder',
        u'rights_issue',
        u'bbd_source'
    ]

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_public_offer(self, indexstr, ustr):
        """发行上市 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_melon_case(self, indexstr, ustr):
        """分红情况 清洗验证"""
        ret = None

        return ret

    def check_manager_introduction(self, indexstr, ustr):
        """高管简介 清洗验证"""
        ret = None

        return ret

    def check_company_sitution(self, indexstr, ustr):
        """公司概况 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_capital_structure(self, indexstr, ustr):
        """股本结构 清洗验证"""
        ret = None
        # if public.str_empty(indexstr, ustr):
        #     ret = u'为空'
        return ret

    def check_equity_division(self, indexstr, ustr):
        """股权分置 清洗验证"""
        ret = None

        return ret

    def check_floati_stockholder(self, indexstr, ustr):
        """流通股东 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_rationed_shares(self, indexstr, ustr):
        """配股 清洗验证"""
        ret = None
        # if public.str_empty(indexstr,ustr):
        #     ret = u'为空'
        return ret

    def check_iposhoder(self, indexstr, ustr):
        """十大股东 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_rights_issue(self, indexstr, ustr):
        """增股 清洗验证"""
        ret = None
        # if public.str_empty(indexstr,ustr):
        #     ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
