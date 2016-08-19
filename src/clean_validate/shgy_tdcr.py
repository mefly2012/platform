# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

class shgy_tdcr():
    """中标"""

    need_check_ziduan = [u'bbd_version',
                         u'bbd_url',
                         u'bbd_uptime',
                         u'bbd_html',
                         u'bbd_dotime',
                         u'val',
                         u'forway',
                         u'convention_starting_time',
                         u'_id',
                         u'contract_date',
                         u'land_source',
                         u'actual_starting_time',
                         u'landuse',
                         u'project_name',
                         u'landlevel',
                         u'electron_supervise',
                         u'convention_endtime',
                         u'project_location',
                         u'region',
                         u'company_industry',
                         u'actual_completion_date',
                         u'agreed_delivery_time',
                         u'original_usename',
                         u'area_ha',
                         u'approval_unit',
                         u'deal_price_millon',
                         u'land_use_period',
                         u'contract_volume_ratelower',
                         u'contract_volume_rateupper',
                         u'payable_contract',
                         u'bbd_source'
                         ]

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u"类型不合法"
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_bbd_html(self, indexstr, ustr):
        """html 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_val(self, indexstr, ustr):
        """val 清洗验证"""
        ret = None

        return ret

    def check_forway(self, indexstr, ustr):
        """供地方式 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'拍卖出让', u'挂牌出让', u'协议出让', u'划拨', u'租赁', u'招标', u'招标出让'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
        return ret

    def check_convention_starting_time(self, indexstr, ustr):
        """约定开工时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_contract_date(self, indexstr, ustr):
        """合同签订日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_land_source(self, indexstr, ustr):
        """土地来源 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[\da-zA-Z]').search(ustr):
                ret = u'有数字字母'
        else:
            ret = u'为空'
        return ret

    def check_actual_starting_time(self, indexstr, ustr):
        """实际开工时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_landuse(self, indexstr, ustr):
        """土地用途 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[\da-zA-Z]').search(ustr):
                ret = u'有数字字母'
        else:
            ret = u'为空'
        return ret

    def check_project_name(self, indexstr, ustr):
        """项目名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) and not \
                    public.has_count_en(ustr, 2):
                ret = u'没有2个汉字or 字母'
        else:
            ret = u'为空'
        return ret

    def check_landlevel(self, indexstr, ustr):
        """土地级别 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'^[\u4e00-\u9fa5]{1,}$').match(ustr):
                ret = u'不纯汉字'
        else:
            ret = u'为空'
        return ret

    def check_electron_supervise(self, indexstr, ustr):
        """电子监管号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if len(ustr) < 16:
            #     ret = u'长度小于16'
            # elif re.compile(u'[^\da-zA-Z]').search(ustr):
            #     ret = u'有数字和字母以外的字符'
        else:
            ret = u'为空'
        return ret

    def check_convention_endtime(self, indexstr, ustr):
        """约定竣工时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_project_location(self, indexstr, ustr):
        """项目位置 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_region(self, indexstr, ustr):
        """行政区 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if re.compile(u'[^\u4e00-\u9fa5]').search(ustr):
            #     ret = u'不是汉字'
        else:
            ret = u'为空'
        return ret

    def check_company_industry(self, indexstr, ustr):
        """行业分类 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[\da-zA-Z]').search(ustr):
                ret = u'有数字字母'
        else:
            ret = u'为空'
        return ret

    def check_actual_completion_date(self, indexstr, ustr):
        """实际竣工时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_agreed_delivery_time(self, indexstr, ustr):
        """约定交地时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_original_usename(self, indexstr, ustr):
        """土地使用权人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if not public.has_count_hz(ustr, 2) and \
            #         not public.has_count_en(ustr,2):
            #     ret = u'既没有2个中文又没有2汉字'
        else:
            ret = u'为空'
        return ret

    def check_area_ha(self, indexstr, ustr):
        """面积（公顷） 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_approval_unit(self, indexstr, ustr):
        """批准单位 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u"格式不正确"
        return ret

    def check_deal_price_millon(self, indexstr, ustr):
        """成交价格（万元） 清洗验证"""
        ret = None
        if ustr and len(ustr):
            try:
                float(ustr)
            except Exception as e:
                ret = u'没法解析成float数值'
        return ret

    def check_land_use_period(self, indexstr, ustr):
        """土地使用年限 清洗验证"""
        ret = None

        return ret

    def check_contract_volume_ratelower(self, indexstr, ustr):
        """约定容积率下限 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1) or \
                    public.has_count_en(ustr, 1):
                ret = u"出现中文或英文"
        return ret

    def check_contract_volume_rateupper(self, indexstr, ustr):
        """约定容积率上限 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1) or \
                    public.has_count_en(ustr, 1):
                ret = u"出现中文或英文"
        return ret

    def check_payable_contract(self, indexstr, ustr):
        """分期支付约定 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
