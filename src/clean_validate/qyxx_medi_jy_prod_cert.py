# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_medi_jy_prod_cert():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'frname',
        u'reg_address',
        u'business_scope',
        u'warehouse_address',
        u'operate_mode',
        u'principal',
        u'quality_principal',
        u'issue_date',
        u'validdate',
        u'certificate_no',
        u'issueunit',
        u'remark',
        u'bbd_url',
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
        if ustr and len(ustr):
            if re.compile(u'^\d{1,}$').match(ustr) or \
                    re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'不全为数字或字母'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1) and \
                    not public.has_count_en(ustr, 2):
                ret = u'格式不合法'
        return ret

    def check_reg_address(self, indexstr, ustr):
        """注册地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'格式不合法'
        return ret

    def check_business_scope(self, indexstr, ustr):
        """经营范围 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'格式不合法'
            elif re.compile(u'[0-9a-zA-Z]').search(ustr):
                ret = u'有数字或者字母'
        return ret

    def check_warehouse_address(self, indexstr, ustr):
        """仓库地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u"格式不合法"
        return ret

    def check_operate_mode(self, indexstr, ustr):
        """经营方式 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'格式不合法'
            elif re.compile(u'[0-9a-zA-Z]').search(ustr):
                ret = u'有数字或者字母'
        return ret

    def check_principal(self, indexstr, ustr):
        """企业负责人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1) and \
                    not public.has_count_en(ustr, 2):
                ret = u'格式不合法'
        return ret

    def check_quality_principal(self, indexstr, ustr):
        """质量负责人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1) and \
                    not public.has_count_en(ustr, 2):
                ret = u'格式不合法'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期至 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            ret = None
            # if re.compile(u'[^a-zA-Z0-9]').search(ustr):
            #     ret = u'还有数字或者字母以外的字符'
        else:
            ret = u"为空"
        return ret

    def check_issueunit(self, indexstr, ustr):
        """发证部门 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.is_allchinese(ustr):
                ret = u'不是全中文'
            elif not unicode(ustr).endswith(u'局'):
                ret = u"不是以局结尾"
        return ret

    def check_remark(self, indexstr, ustr):
        """备注 清洗验证"""
        ret = None

        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
