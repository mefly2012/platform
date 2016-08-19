# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_food_prod_cert():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'product_name',
        u'company_name',
        u'location',
        u'issue_unit',
        u'issue_date',
        u'test_mode',
        u'produce_address',
        u'validdate',
        u'certificate_no',
        u'bbd_url',
        u'bbd_qyxx_company_id',
        u'bbd_qyxx_branch_id',
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
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_product_name(self, indexstr, ustr):
        """产品名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有一个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有一个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_location(self, indexstr, ustr):
        """住所 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"汉子不足两位"
        return ret

    def check_issue_unit(self, indexstr, ustr):
        """发证单位 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
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

    def check_test_mode(self, indexstr, ustr):
        """检验方式 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"汉子不足两位"
        else:
            ret = u'为空'
        return ret

    def check_produce_address(self, indexstr, ustr):
        """生产地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"汉字不足两位"
        return ret

    def check_validdate(self, indexstr, ustr):
        """证书有效期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.match(u'^QS\d{1,}$', ustr):
                ret = u'不满足QS+数字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
