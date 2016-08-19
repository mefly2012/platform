# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class xzcf():
    """中标"""

    need_check_ziduan = [
        u'_id',
        u'punish_org',
        u'punish_basis',
        u'punish_code',
        u'case_name',
        u'public_date',
        u'punish_type',
        u'name',
        u'case_details',
        u'basis_assert',
        u'punish_content',
        u'bbd_source'
    ]

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_punish_org(self, indexstr, ustr):
        """处罚机关 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_punish_basis(self, indexstr, ustr):
        """处罚依据 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个以上汉字"
        return ret

    def check_punish_code(self, indexstr, ustr):
        """文书号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_case_name(self, indexstr, ustr):
        """案件名称 清洗验证"""
        ret = None

        return ret

    def check_public_date(self, indexstr, ustr):
        """发布日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_punish_type(self, indexstr, ustr):
        """违法事实 清洗验证"""
        ret = None

        return ret

    def check_name(self, indexstr, ustr):
        """处罚对象 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_case_details(self, indexstr, ustr):
        """案件详情 清洗验证"""
        ret = None

        return ret

    def check_basis_assert(self, indexstr, ustr):
        """认定依据 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个以上汉字"
        return ret

    def check_punish_content(self, indexstr, ustr):
        """处罚结果 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"没有两个以上汉字"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
