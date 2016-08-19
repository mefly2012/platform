# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_zhuanli():
    """万方专利"""
    need_check_ziduan = [u'bbd_dotime',
                         u'company_name',
                         u'application_date',
                         u'application_code',
                         u'class_code',
                         u'nventor_designer',
                         u'patent_agency',
                         u'application_announce_date',
                         u'spplication_notification_num',
                         u'pct_enter_national',
                         u'approval_num',
                         u'approval_issue_date',
                         u'bg_publication_date',
                         u'decode_announce_date'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()' + public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'有半角括号或者全角数字字母'
        return ret

    def check_application_date(self, indexstr, ustr):
        """申请日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_application_code(self, indexstr, ustr):
        """申请号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_nventor_designer(self, indexstr, ustr):
        """发明人/设计人 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in u'　 ' for c in ustr):
                ret = u'还有空格'
        return ret

    def check_patent_agency(self, indexstr, ustr):
        """专利代理机构 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (u'()' + public.QUANJIAO_NUM + public.QUANJIAO_EN) for c in ustr):
                ret = u'有半角括号或者全角数字字母'
        return ret

    def check_application_announce_date(self, indexstr, ustr):
        """申请/授权公告日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_spplication_notification_num(self, indexstr, ustr):
        """申请/授权公告号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_pct_enter_national(self, indexstr, ustr):
        """PCT进入国家阶段日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_approval_num(self, indexstr, ustr):
        """审定号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_approval_issue_date(self, indexstr, ustr):
        """审定公告日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bg_publication_date(self, indexstr, ustr):
        """更正文献出版日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_decode_announce_date(self, indexstr, ustr):
        """解密公告日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
