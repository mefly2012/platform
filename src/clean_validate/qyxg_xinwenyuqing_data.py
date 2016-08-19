# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class qyxg_xinwenyuqing_data():
    """双软认证"""
    need_check_ziduan = [
        '_id',
        'bbd_dotime',
        'bbd_table',
        'bbd_type',
        'bbd_uptime',
        'bbd_version',
        'main',
        'title',
        'plate',
        'source'
    ]

    def check__id(self, indexstr, ustr):
        """唯一id"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
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
        """不可为空"""
        ret = None
        if ustr and len(ustr):
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

    def check_main(self, indexstr, ustr):
        """main"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_title(self, indexstr, ustr):
        """标题"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_plate(self, indexstr, ustr):
        """所属网站板块"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_source(self, indexstr, ustr):
        """网站来源"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
