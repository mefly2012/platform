# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public


class recruit():
    """招聘"""

    need_check_ziduan = [
        'agerequired',
        'bbd_dotime',
        'bbd_version',
        'benefits',
        'company_introduction',
        'company_name',
        'company_nature',
        'contact_information',
        'delivery_time',
        'department',
        'education_required',
        'e_mail',
        'enscale',
        'industry',
        'job_title',
        'job_descriptions',
        'jobfair_location',
        'jobfair_time',
        'job_functions',
        'job_nature',
        'language_required',
        'location',
        'majors_required',
        'page_content',
        'postcode',
        'pubdate',
        'recruit_numbers',
        'reportto',
        'responserate',
        'salary',
        'salary_system',
        'service_year',
        'sex_required',
        'source',
        'underling_numbers',
        'validdate',
        'view_rate',
        'website_address'
    ]

    def check_agerequired(self, indexstr, ustr):
        """年龄要求 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'年龄不限' and \
                    not re.compile(u'^\d{1,2}-\d{1,2}岁$').match(ustr):
                ret = u'不是年龄不限也不是dd-dd岁'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None
        # ustr = str(ustr)
        # if public.str_empty(indexstr, ustr):
        #     ret = u"为空"
        return ret

    def check_benefits(self, indexstr, ustr):
        """福利待遇 清洗验证"""
        ret = None

        return ret

    def check_company_introduction(self, indexstr, ustr):
        """公司简介 清洗验证"""
        ret = None

        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        return ret

    def check_company_nature(self, indexstr, ustr):
        """企业性质 清洗验证"""
        ret = None

        return ret

    def check_contact_information(self, indexstr, ustr):
        """联系人及联系方式 清洗验证"""
        ret = None

        return ret

    def check_delivery_time(self, indexstr, ustr):
        """简历投递时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_department(self, indexstr, ustr):
        """所属部门 清洗验证"""
        ret = None

        return ret

    def check_education_required(self, indexstr, ustr):
        """学历要求 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if all(c not in ustr for c in (u'本科', u'专科', u'大专', u'高中',
                                           u'硕士', u'无要求', u'不限', u'中技',
                                           u'初中', u'中专', u'博士')):
                ret = u'不是合法学历'
        return ret

    def check_e_mail(self, indexstr, ustr):
        """邮箱 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if u'@' not in ustr:
                ret = u'没有@'
        return ret

    def check_enscale(self, indexstr, ustr):
        """企业规模 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(c in public.BANJIAO_EN for c in ustr):
                ret = u'有字母'
        return ret

    def check_industry(self, indexstr, ustr):
        """所属行业 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if not public.is_allchinese(ustr):
        #         ret = u'不是汉字'
        return ret

    def check_job_title(self, indexstr, ustr):
        """job_title 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"不为空"
        return ret

    def check_job_descriptions(self, indexstr, ustr):
        """职位描述 清洗验证"""
        ret = None

        return ret

    def check_jobfair_location(self, indexstr, ustr):
        """招聘会地点 清洗验证"""
        ret = None

        return ret

    def check_jobfair_time(self, indexstr, ustr):
        """招聘会时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_job_functions(self, indexstr, ustr):
        """职位职能 清洗验证"""
        ret = None

        return ret

    def check_job_nature(self, indexstr, ustr):
        """工作性质 清洗验证"""
        ret = None

        return ret

    def check_language_required(self, indexstr, ustr):
        """语言要求 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.exect_chinese_num(ustr, 2):
                ret = u'不足2汉字'
        return ret

    def check_location(self, indexstr, ustr):
        """工作地点 清洗验证"""
        ret = None

        return ret

    def check_majors_required(self, indexstr, ustr):
        """专业要求 清洗验证"""
        ret = None

        return ret

    def check_page_content(self, indexstr, ustr):
        """招聘页面内容 清洗验证"""
        ret = None

        return ret

    def check_postcode(self, indexstr, ustr):
        """邮编 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(not public.is_number(c) for c in ustr):
                ret = u'不是数字'
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_recruit_numbers(self, indexstr, ustr):
        """招聘人数 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[a-zA-Z]').search(ustr):
                ret = u'包含字母'
        return ret

    def check_reportto(self, indexstr, ustr):
        """汇报对象 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(public.is_number(c) for c in ustr):
                ret = u'有数字'
        return ret

    def check_responserate(self, indexstr, ustr):
        """反馈率 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(c not in u'0123456789.%' for c in ustr):
                if not re.compile(u'^\d+(\.\d+)?%$').match(ustr):
                    ret = u'不是百分数'
            else:
                ret = u'有特殊字符'
        return ret

    def check_salary(self, indexstr, ustr):
        """职位薪资 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[a-zA-Z]').search(ustr):
                ret = u'包含字母'
        return ret

    def check_salary_system(self, indexstr, ustr):
        """薪资体系 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(not public.is_chinese(c) for c in ustr):
                ret = u'不是汉字'
        return ret

    def check_service_year(self, indexstr, ustr):
        """工作年限 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(c in public.BANJIAO_EN for c in ustr):
                ret = u'包含字母'
            elif u'招聘' in ustr:
                ret = u'包含招聘二字'
        return ret

    def check_sex_required(self, indexstr, ustr):
        """性别要求 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'男', u'女', u'不限'):
                ret = u'非男，女，不限'
        return ret

    def check_source(self, indexstr, ustr):
        """source 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        return ret

    def check_underling_numbers(self, indexstr, ustr):
        """下属人数 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{1,}人$').match(ustr):
                ret = u'不是dd人格式'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_view_rate(self, indexstr, ustr):
        """查看率 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(c not in u'0123456789.%' for c in ustr):
                if not re.compile(u'^\d+(\.\d+)?%$').match(ustr):
                    ret = u'不是百分数'
            else:
                ret = u'有特殊字符'
        return ret

    def check_website_address(self, indexstr, ustr):
        """公司网址 清洗验证"""
        ret = None

        return ret
