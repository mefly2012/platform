# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class hnsw_all_info():
    """企业欠税"""
    need_check_ziduan = [
        'bbd_source',
        'defaulteroftax_name',
        'frname',
        'line_operation_address',
        'tax_authorities',
        'taxes_category'
    ]

    def check_bbd_source(self, indexstr, ustr):
        """数据源"""
        """不可为空，且必须为2个字以上的中文"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'不包含两个以上中文'
        else:
            ret = u'为空'
        return ret

    def check_defaulteroftax_name(self, indexstr, ustr):
        """欠税人名称"""
        """不可为空，至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'不包含两个以上中文也没有2个以上英文'
        else:
            ret = u'为空'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'不包含两个以上中文也没有2个以上英文'
        return ret

    def check_line_operation_address(self, indexstr, ustr):
        """生产经营地址"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'不包含两个以上中文也没有2个以上英文'
        return ret

    def check_tax_authorities(self, indexstr, ustr):
        """主管税务机关"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'不包含两个以上中文也没有2个以上英文'
        return ret

    def check_taxes_category(self, indexstr, ustr):
        """欠税税种"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'不包含两个以上中文也没有2个以上英文'
        return ret
