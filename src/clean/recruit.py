# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class recruit():
    """招聘"""

    need_check_ziduan = ['bbd_dotime',
                         'benefits',
                         'company_introduction',
                         'company_name',
                         'company_nature',
                         'contact_information',
                         'delivery_time',
                         'department',
                         'e_mail',
                         'industry',
                         'job_title',
                         'job_descriptions',
                         'jobfair_time',
                         'job_functions',
                         'job_nature',
                         'language_required',
                         'location',
                         'majors_required',
                         'postcode',
                         'pubdate',
                         'recruit_numbers',
                         'salary',
                         'salary_system',
                         'service_year',
                         'validdate',
                         'website_address'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_benefits(self, indexstr, ustr):
        """福利待遇"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'[]］［\"\\', unicode(ustr)):
                ret = u"包含特殊字符"
        return ret

    def check_company_introduction(self, indexstr, ustr):
        """公司简介"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) != unicode(ustr).strip():
                ret = u"文字前后空格未去除"
            elif public.is_include_specialchar(u'※●', unicode(ustr)):
                ret = u"特殊字符未去除"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name"""
        special_pa = re.compile(u'[【】\d)(、]')
        special_b = u'招聘'
        ret = None
        if ustr and len(ustr):
            if special_pa.search(ustr):
                ret = u"特殊字符未去除"
            elif special_b in ustr:
                ret = u"招聘未去除"
        return ret

    def check_company_nature(self, indexstr, ustr):
        """企业性质"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'/()', unicode(ustr)):
                ret = u"特殊字符未去除"
        return ret

    def check_contact_information(self, indexstr, ustr):
        """联系人及联系方式"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) != unicode(ustr).strip():
                ret = u"前后空格未去除"
            if public.is_include_specialchar(u'，　 ', unicode(ustr).strip()):
                ret = u"特殊字符未去除"
        return ret

    def check_delivery_time(self, indexstr, ustr):
        """简历投递时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_department(self, indexstr, ustr):
        """所属部门"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"特殊字符未去除"
        return ret

    def check_e_mail(self, indexstr, ustr):
        """e-mail"""
        ret = None
        if ustr and len(ustr):
            if not public.is_mail(unicode(ustr).strip()):
                ret = u"非邮箱格式"
        return ret

    def check_industry(self, indexstr, ustr):
        """所属行业"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) != unicode(ustr).strip():
                ret = u"文本前后空格未去除"
            elif public.is_include_specialchar(u'/、　 ', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_job_title(self, indexstr, ustr):
        """job_title"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'/，+、()', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_job_descriptions(self, indexstr, ustr):
        """职位描述"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) != unicode(ustr).strip():
                ret = u"前后空格未去除"
            elif public.is_include_specialchar(u'　 ', ustr):
                ret = u"特殊字符未去除"
            elif unicode(ustr).find('\\r\\n') > 0:
                ret = u"\\r\\n未去除"
        return ret

    def check_jobfair_time(self, indexstr, ustr):
        """招聘会时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_job_functions(self, indexstr, ustr):
        """职位职能"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u',，/、', unicode(ustr).strip()):
                ret = u"特殊字符未去除"
        return ret

    def check_job_nature(self, indexstr, ustr):
        """工作性质"""
        ret = None
        if ustr and len(ustr):
            if u'工作性质：' in unicode(ustr):
                ret = u"工作性质：未去除"
        return ret

    def check_language_required(self, indexstr, ustr):
        """语言要求"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u' 　', ustr):
                ret = u"空格未去除"
        return ret

    def check_location(self, indexstr, ustr):
        """工作地点"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u')(/、', ustr):
                ret = u"特殊字符未去除"
            elif public.is_include_specialchar(u'）（', ustr):
                if not public.check_brackets_match(ustr):
                    ret = u"括号不匹配"

        return ret

    def check_majors_required(self, indexstr, ustr):
        """专业要求"""
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) != unicode(ustr).strip():
                ret = u"前后空格未去除"
            elif public.is_include_specialchar(u'，、　 ', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_postcode(self, indexstr, ustr):
        """邮编"""
        ret = None
        if ustr and len(ustr):
            if any(c not in u'0123456789' for c in ustr):
                ret = u"非全数值"
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_recruit_numbers(self, indexstr, ustr):
        """招聘人数"""
        ret = None
        if ustr and len(ustr):
            if u'人' in ustr or u'招聘人数：' in ustr:
                ret = u"字符未删除"
        return ret

    def check_salary(self, indexstr, ustr):
        """职位薪资"""
        ret = None
        if ustr and len(ustr):
            if ustr in (u'面议', u'未提供'):
                pass
            elif not re.compile(u'^\d{1,}$').match(ustr) and \
                    not re.compile(u'^\d{1,}-\d{1,}$'):
                ret = u"错误的格式"
        return ret

    def check_salary_system(self, indexstr, ustr):
        """薪资体系"""
        ret = None
        if ustr and len(ustr):
            if u'/' in unicode(ustr):
                ret = u"包含斜杠"
        return ret

    def check_service_year(self, indexstr, ustr):
        """工作年限"""
        ret = None
        if ustr and len(ustr):
            if any(c in u'+/' for c in unicode(ustr)):
                ret = u"包含/+"
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_website_address(self, indexstr, ustr):
        """公司网址"""
        ret = None
        if ustr and len(ustr):
            if any(public.is_chinese(c) == True for c in unicode(ustr)):
                ret = u"包含汉字"
            if public.is_include_specialchar(u'（；。【 　', unicode(ustr)):
                ret = u"包含特殊字符"
        return ret
