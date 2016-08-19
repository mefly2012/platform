# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_finance_xkz():
    """中标"""

    need_check_ziduan = [
        u'_id',
        u'company_name',
        u'bbd_dotime',
        u'bbd_uptime',
        u'bbd_url',
        u'issue_org',
        u'issue_date',
        u'orgcode',
        u'org_address',
        u'org_short',
        u'org_place',
        u'longitude',
        u'approval_esdate',
        u'latitude',
        u'postalcode',
        u'id_serial_num',
        u'bbd_source'
    ]
    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
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

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_issue_org(self, indexstr, ustr):
        """发证机关 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[^\u4e00-\u9fa5]').search(ustr):
                ret = u'不是汉字'
        else:
            ret = u'为空'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_orgcode(self, indexstr, ustr):
        """机构编码 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if len(ustr) != 15:
                ret = u'长度不为15'
            elif re.compile(u'[^\da-zA-Z]').search(ustr):
                ret = u'有数字字母之外的字符'
        else:
            ret = u'为空'
        return ret

    def check_org_address(self, indexstr, ustr):
        """机构地址 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        else:
            ret = u'为空'
        return ret

    def check_org_short(self, indexstr, ustr):
        """机构简称 清洗验证"""
        ret = None

        return ret

    def check_org_place(self, indexstr, ustr):
        """机构所在地 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[\da-zA-Z]').search(ustr):
                ret = u'有数字或字母'
            elif not public.has_count_hz(ustr, 2):
                ret = u'不包含2个以上汉字'

        else:
            ret = u'为空'
        return ret

    def check_longitude(self, indexstr, ustr):
        """经度 清洗验证"""
        ret = None

        return ret

    def check_approval_esdate(self, indexstr, ustr):
        """批准成立日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_latitude(self, indexstr, ustr):
        """纬度 清洗验证"""
        ret = None

        return ret

    def check_postalcode(self, indexstr, ustr):
        """邮政编码 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.exect_chinese_num(ustr, 1):
                ret = u"出现汉字"
        return ret

    def check_id_serial_num(self, indexstr, ustr):
        """证件流水号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if len(ustr) != 8:
                ret = u'长度不为8'
            elif re.compile(u'[^\d]').search(ustr):
                ret = u'有数字之外的字符'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
