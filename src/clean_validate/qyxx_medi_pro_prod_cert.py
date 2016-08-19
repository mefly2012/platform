# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_medi_pro_prod_cert():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'frname',
        u'reg_address',
        u'produce_scope',
        u'produce_address',
        u'company_type',
        u'principal',
        u'issue_date',
        u'validdate',
        u'certificate_no',
        u'remark',
        u'bbd_url',
        u'province',
        u'code',
        u'bbd_source'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 清洗验证"""
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
        if ustr and len(ustr.strip()):
            if re.compile(u'^\d{1,}$').match(ustr):
                ret = u'不能为纯数字'
            elif re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'不能为纯字母'
        else:
            ret = u'为空'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人 清洗验证"""
        ret = None
        # if ustr and len(ustr.strip()):
        #     if not public.has_count_en(ustr, 2) \
        #             and not public.has_count_hz(ustr, 2):
        #         ret = u'没有2个汉字或者2个字母'
        # else:
        #     ret = u'为空'
        return ret

    def check_reg_address(self, indexstr, ustr):
        """住所/注册地址 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_produce_scope(self, indexstr, ustr):
        """生产范围 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) or public.all_num(ustr):
                ret = u'没有2个汉字或为纯数字'
        # else:
        #     ret = u'为空'
        return ret

    def check_produce_address(self, indexstr, ustr):
        """生产地址 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_company_type(self, indexstr, ustr):
        """企业类型 清洗验证"""
        ret = None
        if ustr and len(ustr):
            # if re.compile(u'[0-9a-zA-Z]').search(ustr):
            #     ret = u'还有数字字母'
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个中文'
        # else:
        #     ret = u'为空'
        return ret

    def check_principal(self, indexstr, ustr):
        """企业负责人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_en(ustr, 2) \
                    and not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字或者2个字母'
        # else:
        #     ret = u'为空'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期截止日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not re.compile(u'^[\u4e00-\u9fa5][a-zA-Z]{0,}\d{8}$').match(ustr):
            #     ret = u'不满足要求'
        else:
            ret = u'为空'
        return ret

    def check_remark(self, indexstr, ustr):
        """备注 清洗验证"""
        ret = None

        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_province(self, indexstr, ustr):
        """省市/省份 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.is_allchinese(ustr):
                ret = u"格式不合法"
        return ret

    def check_code(self, indexstr, ustr):
        """分类码 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
        #         ret = u'不是都为数字'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
