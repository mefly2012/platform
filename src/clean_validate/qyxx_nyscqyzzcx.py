# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_nyscqyzzcx():
    """中标"""
    need_check_ziduan = [
        u'no',
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'reg_address',
        u'produce_address',
        u'type',
        u'validdate',
        u'bbd_url',
        u'province',
        u'bbd_source'
    ]
    def check_no(self, indexstr, ustr):
        """序号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.match('^\d+$', ustr):
                ret = u'不全是数字'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """dotime  清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_key(self, indexstr, ustr):
        """company_key 清洗验证"""
        ret = None

        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_reg_address(self, indexstr, ustr):
        """注册地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_produce_address(self, indexstr, ustr):
        """生产地址  清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     ret = None
        #     # if not public.has_count_hz(ustr, 2):
        #     #     ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_type(self, indexstr, ustr):
        """类型  清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.has_count_hz(ustr, 2):
        #         ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_province(self, indexstr, ustr):
        """省份 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in public.PROVINCE:
                ret = u'不是合法省份'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
