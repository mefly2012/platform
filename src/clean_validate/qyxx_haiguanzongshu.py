# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_haiguanzongshu():
    """中标"""
    need_check_ziduan = [
        u'company_name',
        u'bbd_dotime',
        u'enterprise_manage_type',
        u'customs_type',
        u'validdate',
        u'customs_code',
        u'bbd_source'
    ]
    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^\d{1,}$').match(ustr):
                ret = u'纯数字'
            elif re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'纯字母'
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

    def check_enterprise_manage_type(self, indexstr, ustr):
        """企业管理类别 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.exect_digst_num(ustr, 1):
                ret = u'出现数字'
                # sub = re.compile(u'[^a-zA-Z\u4e00-\u9fa5]').sub('', ustr)
                # if sub != ustr:
                #     ret = u'还有其他字符'
                # elif public.is_allchinese(sub):
                #     ret = u'不是汉字与字母组合'
                # elif public.all_num(sub):
                #     ret = u'全是数字'
        # else:
        #     ret = u'为空'
        return ret

    def check_customs_type(self, indexstr, ustr):
        """报关类别 清洗验证"""
        ret = None
        # if ustr and len(ustr.strip()):
        #     if ustr not in (u'无报关权', u'自理报关', u'代理报关', u'专业报关'):
        #         ret = u'不是指定字段'
        return ret

    def check_validdate(self, indexstr, ustr):
        """注册有效期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_customs_code(self, indexstr, ustr):
        """海关编码 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if len(ustr) != 10:
                ret = u'长度不为10'
            elif re.compile('[^a-zA-Z\d]').search(ustr):
                ret = u'有不为字母或者数字的字符'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
