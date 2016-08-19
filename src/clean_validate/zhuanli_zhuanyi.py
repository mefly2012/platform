# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class zhuanli_zhuanyi():
    """中标"""

    need_check_ziduan = [
        u'ipc_main_class',
        u'_id',
        u'bbd_dotime',
        u'bbd_uptime',
        u'bbd_version',
        u'bgxx',
        u'reg_effect_date',
        u'law_state',
        u'legal_announce_date',
        u'legal_status',
        u'application_code',
        u'bbd_source'
    ]

    def check_ipc_main_class(self, indexstr, ustr):
        """IPC(主分类) 清洗验证"""
        ret = None
        # if ustr and len(ustr.strip()):
        #     if public.has_count_hz(ustr, 1):
        #         ret = u'有汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u"不为整型数"
        return ret

    def check_bgxx(self, indexstr, ustr):
        """变更信息 清洗验证"""
        ret = None

        return ret

    def check_reg_effect_date(self, indexstr, ustr):
        """登记生效日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_law_state(self, indexstr, ustr):
        """法律状态 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_legal_announce_date(self, indexstr, ustr):
        """法律状态公告日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_legal_status(self, indexstr, ustr):
        """法律状态信息 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_application_code(self, indexstr, ustr):
        """申请号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
