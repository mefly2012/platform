# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_baidutiebawt():
    """百度贴吧"""
    need_check_ziduan = [
        '_id',
        'bbd_uptime',
        'bbd_dotime',
        'author',
        'bbd_table',
        'title',
        'bbd_seed',
        'post_name',
        'post_date',
        'bbd_source',
        'company_name',
        # 'rowkey',
        'bbd_type',
        'bbd_url'
    ]

    def check__id(self, indexstr, ustr):
        """_id"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_author(self, indexstr, ustr):
        """作者名称"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_table(self, indexstr, ustr):
        """bbd_table"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_title(self, indexstr, ustr):
        """帖子名称"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_seed(self, indexstr, ustr):
        """bbd_seed"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_post_name(self, indexstr, ustr):
        """贴吧名称"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_post_date(self, indexstr, ustr):
        """时间"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """bbd_source"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name"""
        """不可为空，至少包含两个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'必须包含2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_rowkey(self, indexstr, ustr):
        """rowkey"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_type(self, indexstr, ustr):
        """bbd_type"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
