# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_wechatofficialid():
    """微信公众号"""
    need_check_ziduan = [
        'title',
        'pubdate',
        'public_name',
        '_id',
        'bbd_table',
        'bbd_type',
        'bbd_uptime',
        'bbd_dotime',
        'bbd_version'
    ]

    def check_title(self, indexstr, ustr):
        """文章标题"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间"""
        """可为空，若非空必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
            pass
        return ret

    def check_public_name(self, indexstr, ustr):
        """微信公众号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check__id(self, indexstr, ustr):
        """唯一id"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_table(self, indexstr, ustr):
        """最终入库表名"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_type(self, indexstr, ustr):
        """表类型"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """时间戳"""
        """不可为空，10位整型，如（uptime: int(time.time())）"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{10}$').match(ustr):
                ret = u'不是10位整数'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
        """不可为空，日期格式，如（dotime: 2016-06-17）"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """版本号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
