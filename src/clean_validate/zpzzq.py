# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class zpzzq():
    """中标"""

    need_check_ziduan = [u'_id',
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
                         u'production_name',
                         u'production_category',
                         u'creation_completion_date',
                         u'regnum',
                         u'regdate',
                         u'copyright_owner',
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
            if ustr != u'作品著作权登记公告':
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
                ret = u'不为int'
        return ret

    def check_production_name(self, indexstr, ustr):
        """作品名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2):
            #     ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_production_category(self, indexstr, ustr):
        """作品类别 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_creation_completion_date(self, indexstr, ustr):
        """创作完成日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_regnum(self, indexstr, ustr):
        """登记号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.is_allchinese(ustr):
                ret = u'纯汉字'
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

    def check_copyright_owner(self, indexstr, ustr):
        """著作权人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2):
            #     ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
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
