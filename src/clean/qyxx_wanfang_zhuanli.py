# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_wanfang_zhuanli():
    """万方专利"""
    need_check_ziduan = ['address',
                         'agent_name',
                         'applicant',
                         'application_code',
                         'application_date',
                         'bbd_dotime',
                         'class_code',
                         'company_name',
                         'independent_claim',
                         'inventor',
                         'law_state',
                         'main_classcode',
                         'npc_code',
                         'patent_agency',
                         'public_code',
                         'publidate',
                         'title'
                         ]
    def check_address(self, indexstr, ustr):
        """主申请人地址校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'　 ', ustr):
                ret = u"包含空格"
            elif not re.compile(u'^\d{7,}').search(ustr):
                str7 = ustr[0:6]
                if all(public.is_number(c) for c in str7):
                    if ustr[6] != u';':
                        ret = u"前六个数字未分割"
            elif re.compile(u'^\d{7,};').search(ustr):
                ret = u'没必要分割'
        return ret

    def check_agent_name(self, indexstr, ustr):
        """代理人校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'　 ,，', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_applicant(self, indexstr, ustr):
        """申请（专利权）人校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'　 ,，)(', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_application_code(self, indexstr, ustr):
        """申请（专利）号校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(public.QUANJIAO_EN + public.QUANJIAO_NUM, ustr):
                ret = u"全角字符"
        return ret

    def check_application_date(self, indexstr, ustr):
        """申请日期校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(public.QUANJIAO_EN + public.QUANJIAO_NUM, ustr):
                ret = u"全角字符"
            elif public.is_include_specialchar(u',，', ustr):
                ret = u"有，"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'　 ,，)(', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_independent_claim(self, indexstr, ustr):
        """主权项校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u')(', ustr):
                ret = u"半角字符"
        return ret

    def check_inventor(self, indexstr, ustr):
        """发明（设计）人校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u',，', ustr):
                ret = u"有，"
        return ret

    def check_law_state(self, indexstr, ustr):
        """法律状态校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u')(', ustr):
                ret = u"半角字符"
        return ret

    def check_main_classcode(self, indexstr, ustr):
        """主分类号校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(public.QUANJIAO_EN + public.QUANJIAO_NUM, ustr):
                ret = u"全角字符"
            elif public.is_include_specialchar(u',，', ustr):
                ret = u"有，"
        return ret

    def check_npc_code(self, indexstr, ustr):
        """国别省市代码校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u')(（）', ustr):
                ret = u"特殊字符"
        return ret

    def check_patent_agency(self, indexstr, ustr):
        """专利代理机构校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'　 )(', ustr):
                ret = u"特殊字符未去除"
        return ret

    def check_public_code(self, indexstr, ustr):
        """公开（公告）号校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(public.QUANJIAO_EN + public.QUANJIAO_NUM, ustr):
                ret = u"全角字符"
        return ret

    def check_publidate(self, indexstr, ustr):
        """公开（公告）日校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_title(self, indexstr, ustr):
        """标题校验"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u')(', ustr):
                ret = u"半角字符"
        return ret
