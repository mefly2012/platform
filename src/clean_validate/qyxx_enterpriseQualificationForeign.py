# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_enterpriseQualificationForeign():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'certificate_no',
        u'issue_date',
        u'validdate',
        u'issue_org',
        u'qualification_type',
        u'qualification_level',
        u'punishment_info',
        u'bbd_url',
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

    def check_company_name(self, indexstr, ustr):
        """企业名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """资质证书编号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^通信([\u4e00-\u9fa5]{0,})|（[\u4e00-\u9fa5]{0,}）\d{1,}号{0,1}$').match(ustr) and \
                    not re.compile(u'^通信([\u4e00-\u9fa5]{0,})|（[\u4e00-\u9fa5]{0,}）\d{1,}').match(ustr) and \
                    not re.compile(u'^通([\u4e00-\u9fa5]{0,})|（[\u4e00-\u9fa5]{0,}）\d{1,}').match(ustr) and \
                    not re.compile(u'^通([\u4e00-\u9fa5]{0,})|（[\u4e00-\u9fa5]{0,}）\d{1,}号{0,1}$').match(ustr) and \
                    not public.exect_digst_num(ustr, 6):
                ret = u'不满足格式'
        else:
            ret = u'为空'
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
        """证书有效期 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'^\d{1,}年$').match(ustr):
                ret = u'不满足x年'
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

    def check_qualification_type(self, indexstr, ustr):
        """资质类型 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_qualification_level(self, indexstr, ustr):
        """资质等级 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'甲级', u'乙级', u'丙级',):
                ret = u'不是指定字段'
        return ret

    def check_punishment_info(self, indexstr, ustr):
        """奖惩信息 清洗验证"""
        ret = None

        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
