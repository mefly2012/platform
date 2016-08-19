# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class tdzr():
    """中标"""

    need_check_ziduan = [
        u'bbd_dotime',
        u'company_name',
        u'land_location',
        u'landmark',
        u'landno',
        u'original_usename',
        u'land_use_period',
        u'land_usetype',
        u'land_use_state',
        u'landuse',
        u'landlevel',
        u'area',
        u'transaction_time',
        u'administration_region',
        u'current_usename',
        u'transfer_price',
        u'transfer_mode'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.is_allchinese(ustr):
        #         ret = u"格式不正确"
        return ret

    def check_land_location(self, indexstr, ustr):
        """宗地座落 清洗验证"""
        ret = None

        return ret

    def check_landmark(self, indexstr, ustr):
        """宗地标识 清洗验证"""
        ret = None

        return ret

    def check_landno(self, indexstr, ustr):
        """宗地编号 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_original_usename(self, indexstr, ustr):
        """原土地使用权人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
                # else:
                #     sub = re.compile(u'[a-zA-Z\u4e00-\u9fa5;）（]').sub('', ustr)
                #     if len(sub) > 0:
                #         ret = u'还有其他字符'
        else:
            ret = u'为空'
        return ret

    def check_land_use_period(self, indexstr, ustr):
        """土地使用年限 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.date_format(ustr):
        #         ret = u'不合法日期'
        return ret

    def check_land_usetype(self, indexstr, ustr):
        """土地使用权类型 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不正确"
        return ret

    def check_land_use_state(self, indexstr, ustr):
        """土地利用状况 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_en(ustr, 1):
                ret = u"出现英文字母"
        return ret

    def check_landuse(self, indexstr, ustr):
        """土地用途 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_en(ustr, 1):
                ret = u"出现英文字母"
        return ret

    def check_landlevel(self, indexstr, ustr):
        """土地级别 清洗验证"""
        ret = None

        return ret

    def check_area(self, indexstr, ustr):
        """土地面积(公顷) 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_transaction_time(self, indexstr, ustr):
        """成交时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_administration_region(self, indexstr, ustr):
        """所在行政区 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2) \
            #         and not re.compile(u'^\d{9}$').match(ustr):
            #     ret = u'没有2个汉字,也不是9位数字'
        else:
            ret = u'为空'
        return ret

    def check_current_usename(self, indexstr, ustr):
        """现土地使用权人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u"格式不合法"
                # else:
                #     sub = re.compile(u'[\u4e00-\u9fa5;）（]').sub('', ustr)
                #     if len(sub) > 0:
                #         ret = u'还有其他字符'
        return ret

    def check_transfer_price(self, indexstr, ustr):
        """转让价格(万元) 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_transfer_mode(self, indexstr, ustr):
        """转让方式 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_en(ustr, 1):
                ret = u"出现英文字母"
        return ret
