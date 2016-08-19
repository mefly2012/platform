# -*- coding: utf-8 -*-

import sys

import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class tddy():
    """中标"""

    need_check_ziduan = [
        u'bbd_dotime',
        u'company_name',
        u'land_location',
        u'landmark',
        u'landno',
        u'land_use_warrant',
        u'landuse',
        u'area',
        u'administration_region',
        u'land_rights_no',
        u'mortgage_name',
        u'mortgage_nature',
        u'mortgage_right_name',
        u'mortgagestartdate',
        u'mortgage_enddate',
        u'mortgage_usetype',
        u'mortgage_price',
        u'mortgage_area',
        u'evaluate_price',
        u'bbd_qyxx_company_id',
        u'bbd_qyxx_branch_id',
        u'bbd_source'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        """dotime  清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有包含2个汉字'
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

    def check_land_use_warrant(self, indexstr, ustr):
        """土地使用权证号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.is_allchinese(ustr):
                ret = u"全部为中文"
        return ret

    def check_landuse(self, indexstr, ustr):
        """抵押土地用途 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空'
        return ret

    def check_area(self, indexstr, ustr):
        """土地面积 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_administration_region(self, indexstr, ustr):
        """所在行政区 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if public.has_count_hz(ustr, 2):
            #     sub = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5->]').sub('', ustr)
            #     if len(sub) > 0:
            #         ret = u'还有其他字符'
            #     pass
            #
            # elif re.compile(u'^\d{9}$').match(ustr):
            #     pass
            # else:
            #     ret = u'没有2个汉字,也不是9位数字'

        else:
            ret = u'为空'
        return ret

    def check_land_rights_no(self, indexstr, ustr):
        """土地他项权利人证号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.is_allchinese(ustr):
                ret = u"全部为中文"
        return ret

    def check_mortgage_name(self, indexstr, ustr):
        """土地抵押人名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
                # else:
                #     sub = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5;）（]').sub('', ustr)
                #     if len(sub) > 0:
                #         ret = u'还有其他字符'
        else:
            ret = u'为空'
        return ret

    def check_mortgage_nature(self, indexstr, ustr):
        """土地抵押人性质 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.is_allchinese(ustr):
                ret = u"格式不正确"
        return ret

    def check_mortgage_right_name(self, indexstr, ustr):
        """土地抵押权人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
                # else:
                #     sub = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5;）（]').sub('', ustr)
                #     if len(sub) > 0:
                #         ret = u'还有其他字符'
        else:
            ret = u'为空'
        return ret

    def check_mortgagestartdate(self, indexstr, ustr):
        """土地抵押登记起始日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_mortgage_enddate(self, indexstr, ustr):
        """土地抵押登记结束日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_mortgage_usetype(self, indexstr, ustr):
        """抵押土地权属性质与使用权类型 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不正确"
        return ret

    def check_mortgage_price(self, indexstr, ustr):
        """抵押金额(万元) 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_mortgage_area(self, indexstr, ustr):
        """抵押面积(公顷) 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_evaluate_price(self, indexstr, ustr):
        """评估金额(万元) 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
