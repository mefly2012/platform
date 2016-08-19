# -*- coding: utf-8 -*-


import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_gmpauth_prod_cert():
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'location',
        u'legalize_scope',
        u'issue_date',
        u'valid_period',
        u'certificate_no',
        u'remark',
        u'bbd_url',
        u'province',
        u'legalize_version',
        u'continue_legalize_scope',
        u'continue_date',
        u'validdate',
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
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_location(self, indexstr, ustr):
        """住所/地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if re.findall('^\d+$', ustr) or public.all_english(ustr):
                ret = u'格式不合法'
        return ret

    def check_legalize_scope(self, indexstr, ustr):
        """认证范围 清洗验证"""
        ret = None

        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        # else:
        #     ret = u'为空'
        return ret

    def check_valid_period(self, indexstr, ustr):
        """有效期/有效期截止日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号/许可证编号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^a-zA-Z0-9\u4e00-\u9fa5]').search(ustr):
                ret = u'还有数字字母汉字之外的字符'
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
        if ustr and len(ustr.strip()):
            ret = None
            # if ustr not in public.PROVINCE:
            #     ret = u'不是合法省份'
        else:
            ret = u'为空'
        return ret

    def check_legalize_version(self, indexstr, ustr):
        """认证GMP版本 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'^按\d{4}年修订药品GMP认证$').match(ustr):
                ret = u'不满足按xxxx年修订药品GMP认证'
        # else:
        #     ret = u'为空'
        return ret

    def check_continue_legalize_scope(self, indexstr, ustr):
        """批准延续的认证范围 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.has_count_hz(ustr, 2):
        #         ret = u'没有2个汉字'
        return ret

    def check_continue_date(self, indexstr, ustr):
        """批准延续日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期延续至 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
