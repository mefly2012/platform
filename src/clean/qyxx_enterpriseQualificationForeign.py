# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_enterpriseQualificationForeign():
    """通信建设企业资质"""
    need_check_ziduan = [u'bbd_dotime',
                         u'company_key',
                         u'company_name',
                         u'certificate_no',
                         u'issue_date',
                         u'punishment_info'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_key(self, indexstr, ustr):
        """company_key 校验"""
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_company_name(self, indexstr, ustr):
        """企业名称 校验"""
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """资质证书编号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()' + public.QUANJIAO_NUM) for c in ustr):
                ret = u'有半角括号或者全角数字'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_punishment_info(self, indexstr, ustr):
        """奖惩信息 校验"""
        ret = None
        if ustr and len(ustr):
            if ur'奖励 \r\n\t\t\t\t\t\t\t\t\t\t\t 惩罚' in ustr:
                ret = u'还有特殊字符'
        return ret
