# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_ck():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'issue_org',
        u'mining_mineral',
        u'validdate',
        u'certificate_no',
        u'area',
        u'company_name',
        u'project_type',
        u'issue_date',
        u'mine_name',
        u'mining_method',
        u'design_scale',
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

    def check_issue_org(self, indexstr, ustr):
        """发证机关 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_mining_mineral(self, indexstr, ustr):
        """开采 主矿种 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有汉字'
        else:
            ret = u'为空'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """许可证 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
        return ret

    def check_area(self, indexstr, ustr):
        """面积 (km²) 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_company_name(self, indexstr, ustr):
        """采矿权人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_project_type(self, indexstr, ustr):
        """项目类型 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'新立', u'延续', u'变更', u'注销'):
                ret = u'不是指定字段'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """公告 日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_mine_name(self, indexstr, ustr):
        """矿山名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_mining_method(self, indexstr, ustr):
        """开采方式 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'地下开采', u'露天开采', u'露天/地下开采'):
                ret = u'不是指定字段'
        return ret

    def check_design_scale(self, indexstr, ustr):
        """设计生产规模 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret

    pass
