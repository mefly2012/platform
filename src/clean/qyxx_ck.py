# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_ck():
    """采矿许可证"""
    need_check_ziduan = [u'bbd_dotime',
                         u'company_key',
                         u'certificate_no',
                         u'company_name',
                         u'issue_date',
                         u'mine_name'
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

    def check_certificate_no(self, indexstr, ustr):
        """许可证 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_company_name(self, indexstr, ustr):
        """采矿权人 校验"""
        ret = None
        SPECIAL_STR = u" 　.。#＃＊*×,，?？/\\／＼＇'；;~•．·$￥@＄＾！!^…’‘%)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """公告 日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_mine_name(self, indexstr, ustr):
        """矿山名称 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u')(' for c in ustr):
                ret = u'半角括号'
        return ret
