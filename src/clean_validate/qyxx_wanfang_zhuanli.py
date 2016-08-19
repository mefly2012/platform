# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_wanfang_zhuanli():
    """中标"""

    need_check_ziduan = [
        u'address',
        u'agent_name',
        u'applicant',
        u'application_code',
        u'application_date',
        u'class_code',
        u'company_name',
        u'independent_claim',
        u'inventor',
        u'law_state',
        u'main_classcode',
        u'npc_code',
        u'patent_agency',
        u'patent_type',
        u'public_code',
        u'publidate',
        u'title',
        u'bbd_source'
    ]
    def check_address(self, indexstr, ustr):
        """主申请人地址 清洗验证"""
        ret = None
        # if ustr and len(ustr.strip()):
        #     if not public.has_count_hz(ustr, 2):
        #         ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_agent_name(self, indexstr, ustr):
        """代理人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) and \
                    not public.has_count_en(ustr, 2):
                ret = u"既没有2个中文又没有2汉字"
        return ret

    def check_applicant(self, indexstr, ustr):
        """申请（专利权）人 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if u'∴' in ustr:
        #         ret = u'有特殊字符∴'
        #     else:
        #         if not public.has_count_hz(ustr, 2) \
        #                 and public.has_count_en(ustr, 2):
        #             ret = u'既没有2个中文又没有2汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_application_code(self, indexstr, ustr):
        """申请（专利）号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            ret = None
            # if re.compile(u'[^\d0-9a-zA-Z\.]').search(ustr):
            #     ret = u'还有数字字母.号之外的字符'
            # elif not unicode(ustr).startswith(u'CN'):
            #     ret = u'不是CN开头'
        else:
            ret = u'为空'
        return ret

    def check_application_date(self, indexstr, ustr):
        """申请日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        # else:
        #     ret = u'为空'
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        else:
            ret = u'为空'
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) and \
                    not public.has_count_en(ustr, 2):
                ret = u'既没有2个中文又没有2汉字'
            elif u'∴' in ustr:
                ret = u'有∴在里面'

        return ret

    def check_independent_claim(self, indexstr, ustr):
        """主权项 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'格式不合法'
        return ret

    def check_inventor(self, indexstr, ustr):
        """发明（设计）人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_law_state(self, indexstr, ustr):
        """法律状态 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if all(c not in ustr for c in (u'公开', u'授权')):
                ret = u'不包含指定字段'

        return ret

    def check_main_classcode(self, indexstr, ustr):
        """主分类号 清洗验证"""
        ret = None
        # if ustr and len(ustr):
        #     if public.has_count_hz(ustr, 1):
        #         ret = u'有汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_npc_code(self, indexstr, ustr):
        """国别省市代码 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_patent_agency(self, indexstr, ustr):
        """专利代理机构 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 4):
                ret = u"内容格式不合法"
        return ret

    def check_patent_type(self, indexstr, ustr):
        """专利类型 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'发明专利', u'实用新型', u'外观设计', u'发明公布', u'发明授权'):
                ret = u'不是指定字段'
        # else:
        #     ret = u'为空'
        return ret

    def check_public_code(self, indexstr, ustr):
        """公开（公告）号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            ret = None
            # if not ustr.startwith(u'CN') or \
            #         not public.digst_english(ustr):
            #     ret = u'内容格式不合法'
        else:
            ret = u'为空'
        return ret

    def check_publidate(self, indexstr, ustr):
        """公开（公告）日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_title(self, indexstr, ustr):
        """标题 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有汉字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
