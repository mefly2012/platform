# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qylogo():
    """中标"""
    need_check_ziduan = [
        u'key',
        u'_id',
        u'data_source',
        u'bbd_version',
        u'bbd_url',
        u'rawdata',
        u'bbd_uptime',
        u'company_full_name',
        u'source',
        u'company_short',
        u'uuid',
        u'retain1',
        u'retain2',
        u'company_logo',
        u'bbd_dotime'
    ]
    def check_key(self, indexstr, ustr):
        """key 清洗验证"""
        ret = None

        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_data_source(self, indexstr, ustr):
        """datasource 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'猎聘', u'拉勾'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.all_num(ustr):
                ret = u'不是全数字'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_rawdata(self, indexstr, ustr):
        """rawdata 清洗验证"""
        ret = None

        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_company_full_name(self, indexstr, ustr):
        """企业全称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2):
            #     ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_source(self, indexstr, ustr):
        """Source 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'猎聘', u'拉勾'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
        return ret

    def check_company_short(self, indexstr, ustr):
        """企业简称 清洗验证"""
        ret = None

        return ret

    def check_uuid(self, indexstr, ustr):
        """uuid 清洗验证"""
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

    def check_company_logo(self, indexstr, ustr):
        """企业logo 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
