# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_medi_pro_prod_cert():
    """药品生产许可证"""
    need_check_ziduan = [
        'company_name',
        'frname',
        'reg_address',
        'produce_scope',
        'produce_address',
        'company_type',
        'principal',
        'issue_date',
        'validdate',
        'certificate_no',
        'code'
    ]

    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有空格 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)( 　]').search(ustr):
                ret = u'还有半角括号或者空格'
        return ret

    def check_reg_address(self, indexstr, ustr):
        """住所/注册地址"""
        """删掉所有的* """
        ret = None
        if ustr and len(ustr):
            if u'*' in ustr or u'＊' in ustr:
                ret = u'还有*号'
        return ret

    def check_produce_scope(self, indexstr, ustr):
        """生产范围"""
        """删掉所有的* """
        ret = None
        if ustr and len(ustr):
            if u'*' in ustr or u'＊' in ustr:
                ret = u'还有*号'
        return ret

    def check_produce_address(self, indexstr, ustr):
        """生产地址"""
        """删掉所有的* """
        ret = None
        if ustr and len(ustr):
            if u'*' in ustr or u'＊' in ustr:
                ret = u'还有*号'
        return ret

    def check_company_type(self, indexstr, ustr):
        """企业类型"""
        """将所有半角括号“()”转换成全角括号“（）” """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'
        return ret

    def check_principal(self, indexstr, ustr):
        """企业负责人"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有空格 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[)( 　]').search(ustr):
                ret = u'还有半角括号或者空格'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期截止日"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """编号"""
        """将全角数字和字母全部转为半角
        （如：将“辽２０１００２１１”清洗为“辽20100211”） """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
        return ret

    def check_code(self, indexstr, ustr):
        """分类码"""
        """将全角字母全部转换为半角 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'还有全角字母或者数字'
        return ret
