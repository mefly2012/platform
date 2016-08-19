# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class xgxx_shangbiao():
    """商标"""

    need_check_ziduan = [
        'bbd_dotime',
        'company_name',
        'applicant_name',
        'product_list',
        'similar_groups',
        'brand_image',
        'class_no',
        'application_no',
        'shangbiao',
        'brand_name',
        'commodity',
        'no',
        'bbd_source'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr):
            ustr = unicode(ustr).strip()
            if all(public.is_number(c) for c in ustr):
                ret = u"全为数字"
            elif not public.has_count_en(ustr, 2) \
                    and not public.has_count_hz(ustr, 2):
                ret = u'既没有2个汉字又没有2个英文'
        else:
            ret = u"为空"
        return ret

    def check_applicant_name(self, indexstr, ustr):
        """申请人名称 清洗验证"""
        ret = self.check_company_name(indexstr, ustr)
        return ret

    def check_product_list(self, indexstr, ustr):
        """商品/服务列表 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        elif unicode(ustr).strip() in (u'null', u'NULL'):
            ret = u"为null"
        return ret

    def check_similar_groups(self, indexstr, ustr):
        """类似群 清洗验证"""
        ret = self.check_product_list(indexstr, ustr)

        return ret

    def check_brand_image(self, indexstr, ustr):
        """商标图像 清洗验证"""
        ret = self.check_product_list(indexstr, ustr)
        return ret

    def check_class_no(self, indexstr, ustr):
        """类号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            try:
                num = int(ustr)
                if num > 45 or num < 1:
                    ret = u'不在[1,45]之间'
            except Exception as e:
                ret = u'无法解析成整数'
        else:
            ret = u"为空"
        return ret

    def check_application_no(self, indexstr, ustr):
        """申请号/注册号 清洗验证"""
        ret = None

        if ustr and len(ustr):
            if all(public.is_number(c) for c in ustr):
                if len(ustr) > 8:
                    ret = u"不是数字"
            else:
                ret = u"不全为数字"
            pass
        else:
            ret = u"为空"

        return ret

    def check_shangbiao(self, indexstr, ustr):
        """shangbiao 清洗验证"""
        ret = None

        return ret

    def check_brand_name(self, indexstr, ustr):
        """商标名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr).strip() in (u'null', u'NULL'):
                ret = u"为null"
        return ret

    def check_commodity(self, indexstr, ustr):
        """商品 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"

        return ret

    def check_no(self, indexstr, ustr):
        """序号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(not public.is_number(c) for c in ustr):
                ret = u'有不是数字的情况'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
