# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class rjzzq():
    """中标"""

    need_check_ziduan = [
        u'_id',
        u'data_source',
        u'bbd_dotime',
        u'key',
        u'rawdata',
        u'retain1',
        u'retain2',
        u'bbd_uptime',
        u'bbd_url',
        u'uuid',
        u'bbd_version',
        u'class_code',
        u'version_num',
        u'regnum',
        u'regdate',
        u'copyright_nationality',
        u'copyright_owner',
        u'soft_full_name',
        u'soft_short',
        u'date_first_publication',
        u'bbd_source'
    ]

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_data_source(self, indexstr, ustr):
        """datasource 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr != u'软件著作权登记公告':
                ret = u'不是指定字段'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_key(self, indexstr, ustr):
        """key 清洗验证"""
        ret = None

        return ret

    def check_rawdata(self, indexstr, ustr):
        """rawdata 清洗验证"""
        ret = None

        return ret

    def check_retain1(self, indexstr, ustr):
        """retain1 清洗验证"""
        ret = None

        return ret

    def check_retain2(self, indexstr, ustr):
        """retain2 清洗验证"""
        ret = None

        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_uuid(self, indexstr, ustr):
        """uuid 清洗验证"""
        ret = None

        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u"类型不正确"
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        return ret

    def check_version_num(self, indexstr, ustr):
        """版本号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        return ret

    def check_regnum(self, indexstr, ustr):
        """登记号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        else:
            ret = u'为空'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_copyright_nationality(self, indexstr, ustr):
        """著作权人国籍 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有汉字'
        else:
            ret = u'为空'
        return ret

    def check_copyright_owner(self, indexstr, ustr):
        """著作权人搜索条件 清洗验证"""
        ret = None

        return ret

    def check_soft_full_name(self, indexstr, ustr):
        """软件全称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2):
            #     ret = u'没有汉字'
        else:
            ret = u'为空'
        return ret

    def check_soft_short(self, indexstr, ustr):
        """软件简称 清洗验证"""
        ret = None

        return ret

    def check_date_first_publication(self, indexstr, ustr):
        """首次发表日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
