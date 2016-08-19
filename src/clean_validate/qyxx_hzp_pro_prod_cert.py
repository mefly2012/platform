# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_hzp_pro_prod_cert():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_name',
        u'location',
        u'produce_address',
        u'issue_date',
        u'validdate',
        u'certificate_no',
        u'details',
        u'bbd_url',
        u'province',
        u'product_name',
        u'bbd_source'
    ]
    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
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
        """住所 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_produce_address(self, indexstr, ustr):
        """生产地址 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
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
        """有效期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号/许可证编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not re.compile(u'^XK\d{2}-\d{3} \d{4}$').match(ustr):
            #     ret = u'不符合格式'
        else:
            ret = u'为空'
        return ret

    def check_details(self, indexstr, ustr):
        """明细 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
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

    def check_product_name(self, indexstr, ustr):
        """产品名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'^[\u4e00-\u9fa5]{1,}$').match(ustr):
                ret = u'不纯汉字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
