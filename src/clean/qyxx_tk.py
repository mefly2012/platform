# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_tk():
    """探矿许可证"""
    need_check_ziduan = [u'bbd_dotime',
                         u'company_key',
                         u'issue_org',
                         u'certificate_no',
                         u'company_name',
                         u'issue_date',
                         u'explore_unit'
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

    def check_issue_org(self, indexstr, ustr):
        """发证机关 校验"""
        ret = None
        if ustr and len(ustr):
            if u'内蒙' in ustr:
                if u'内蒙古' not in ustr:
                    ret = u'没有替换完呢'
                elif u'内蒙古古' in ustr:
                    ret = u'替换过头了吧'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """许可证 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_company_name(self, indexstr, ustr):
        """探矿权人 校验"""
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

    def check_explore_unit(self, indexstr, ustr):
        """勘查单位 校验"""
        ret = None
        if any(c in u')(' for c in ustr):
            ret = u'半角括号'
        return ret
