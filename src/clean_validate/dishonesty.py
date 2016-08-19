# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public




class dishonesty():
    """失信被执行人"""
    need_check_ziduan = ['bbd_dotime',
                         'pname',
                         'pname_id',
                         'frname',
                         'exec_court_name',
                         'province',
                         'exe_code',
                         'case_create_time',
                         'case_code',
                         'exec_basunit',
                         'definiteo_bligation',
                         'perform_degree',
                         'concrete_situation',
                         'pubdate',
                         'bbd_source'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_pname(self, indexstr, ustr):
        """被执行人姓名或名称 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if all(public.is_number(c) for c in ustr):
                ret = u'是纯数字'
            elif all(public.is_alphabet(c) for c in ustr):
                ret = u'是纯字母'
        else:
            ret = u'为空'
        return ret

    def check_pname_id(self, indexstr, ustr):
        """身份证号码或组织机构代码 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(public.is_chinese(c) for c in ustr):
                ret = u'有汉字'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人或者负责人姓名 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     ret = None
        #     # if all(c in public.BANJIAO_NUM for c in ustr):
        #     #     ret = u'不能为纯数字'
        #     # else:
        #     #     if re.compile(u'[\u4e00-\u9fa5]').search(ustr) ==None and\
        #     #         len(re.compile(u'[^a-zA-Z]').sub('',ustr))<2:
        #     #         ret = u'没有汉字也没有两个以上字母'
        # else:
        #     ret = u'为空'
        return ret

    def check_exec_court_name(self, indexstr, ustr):
        """执行法院 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if u'法院' not in ustr and u'法庭' not in ustr:
                ret = u'不包含法院或法庭二字'
        else:
            ret = u'为空'
        return ret

    def check_province(self, indexstr, ustr):
        """省份 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(not public.is_chinese(c) for c in ustr):
                ret = u'不全为汉字'
        else:
            ret = u'为空'
        return ret

    def check_exe_code(self, indexstr, ustr):
        """执行依据文号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            ret = None
            # if all(public.is_number(c) for c in ustr):
            #     ret = u'是纯数字'
        else:
            ret = u'为空'
        return ret

    def check_case_create_time(self, indexstr, ustr):
        """立案时间 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_case_code(self, indexstr, ustr):
        """案号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'.*号$').match(ustr):
                ret = u'需要满足“以号结尾”格式'
        else:
            ret = u"为空"
        return ret

    def check_exec_basunit(self, indexstr, ustr):
        """做出执行依据单位 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(c in u'（）()' for c in ustr):
                ret = u'有全角或者半角括号'
        return ret

    def check_definiteo_bligation(self, indexstr, ustr):
        """生效法律文书确定义务 清洗验证"""
        ret = None

        return ret

    def check_perform_degree(self, indexstr, ustr):
        """被执行人的履行情况 清洗验证"""
        ret = None
        if ustr or len(ustr.strip):
            if ustr not in (u'部分未履行', u'全部未履行'):
                ret = u'不是部分未履行或者全部未履行'
        else:
            ret = u"为空了"
        return ret

    def check_concrete_situation(self, indexstr, ustr):
        """失信被执行人行为具体情形 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if any(public.is_number(c) or public.is_alphabet(c) for c in ustr):
                ret = u'数字或字母'
        else:
            ret = u'为空'
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u"为空了"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
