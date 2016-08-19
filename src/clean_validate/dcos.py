# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class dcos():
    """双软认证"""
    need_check_ziduan = [
        u'no',
        u'bbd_dotime',
        u'original_company_name',
        u'company_name',
        u'original_frname',
        u'frname',
        u'original_product_name',
        u'product_name',
        u'certificate_num',
        u'regdate',
        u'publish_date',
        u'issue_date',
        u'type',
        u'bbd_url',
        u'current_city'
    ]
    def check_no(self, indexstr, ustr):
        """序号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile('^\d{1,}$').match(ustr):
                ret = u'不是纯数字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_original_company_name(self, indexstr, ustr):
        """原企业名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不合法"
        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
                # else:
                #     sub = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5;）（]').sub('', ustr)
                #     if len(sub) > 0:
                #         ret = u'还有其他字符'
        else:
            ret = u'为空'
        return ret

    def check_original_frname(self, indexstr, ustr):
        """原法定代表人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不合法"
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不合法"
        return ret

    def check_original_product_name(self, indexstr, ustr):
        """原产品名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if len(ustr.strip()) < 2:
                ret = u'没有2位以上'
        return ret

    def check_product_name(self, indexstr, ustr):
        """产品名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if len(ustr.strip()) < 2:
                ret = u'没有2位以上'
        return ret

    def check_certificate_num(self, indexstr, ustr):
        """证书编号 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not re.compile(u'^[\4e00-\u9fa5]{1,}[A-Z]{1,}-[0-9]{4}-[0-9]{4}$').match(ustr):
        #         ret = u'格式不正确'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_publish_date(self, indexstr, ustr):
        """公布年度 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{4}$').match(ustr):
                ret = u"格式不正确"
        return ret

    def check_issue_date(self, indexstr, ustr):
        """认定日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_type(self, indexstr, ustr):
        """type 清洗验证"""
        ret = None

        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_current_city(self, indexstr, ustr):
        """所在城市 清洗验证"""
        ret = None

        return ret
