# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class zhuanli_zhuanyi():
    """专利转移"""
    need_check_ziduan = [u'ipc_main_class',
                         u'bbd_dotime',
                         u'bgxx',
                         u'reg_effect_date',
                         u'legal_announce_date',
                         u'application_code'
                         ]
    def check_ipc_main_class(self, indexstr, ustr):
        """IPC(主分类) 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bgxx(self, indexstr, ustr):
        """变更信息 校验"""
        ret = None
        return ret

    def check_reg_effect_date(self, indexstr, ustr):
        """登记生效日 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_legal_announce_date(self, indexstr, ustr):
        """法律状态公告日 校验"""
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
