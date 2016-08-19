# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class ppp():
    """ppp项目"""
    need_check_ziduan = ['bbd_dotime',
                         'project_name',
                         'project_number',
                         'spplication_body',
                         'project_nisp',
                         'source_need',
                         'society_capacity_need',
                         'wheth_allowcons_cpag',
                         'social_limit_standards',
                         'policy_perf_guarantee',
                         'pre_qualification_method',
                         'bmdjb',
                         'pre_qualification_docplace',
                         'pre_qualification_docplace',
                         'pre_qualification_docaddr',
                         'pre_qualification_doc',
                         'signup_date',
                         'signup_place',
                         'contact_phone',
                         'prequalification_deaddate',
                         'prequalification_date',
                         'send_place',
                         'send_address',
                         'tender_name',
                         'contact_person',
                         'contact_phone01',
                         'contact_address',
                         'tender_agency_orgname',
                         'contact_person01',
                         'contact_phone02',
                         'contact_address01'
                         ]

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
        """可为空；若非空则为以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_project_name(self, indexstr, ustr):
        """项目名称"""
        """不可为空，至少包含2个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_project_number(self, indexstr, ustr):
        """项目编号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_spplication_body(self, indexstr, ustr):
        """授权主体"""
        """不可为空，至少包含2个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_project_nisp(self, indexstr, ustr):
        """项目实施机构"""
        """不可为空，至少包含2个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_source_need(self, indexstr, ustr):
        """采购需求"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_society_capacity_need(self, indexstr, ustr):
        """社会资本资格要求"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_wheth_allowcons_cpag(self, indexstr, ustr):
        """是否允许联合体参与采购活动"""
        """可为空，若非空为汉字"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^\u4e00-\u9fa5]').search(ustr):
                ret = u'有不是汉字呢'
        return ret

    def check_social_limit_standards(self, indexstr, ustr):
        """社会资本的数量及限定的方法和标准"""
        """可为空，若非空为汉字"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^\u4e00-\u9fa5]').search(ustr):
                ret = u'有不是汉字呢'
        return ret

    def check_policy_perf_guarantee(self, indexstr, ustr):
        """政策要求以及履约保证担保要求"""
        """可为空，若非空为汉字"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^\u4e00-\u9fa5]').search(ustr):
                ret = u'有不是汉字呢'
        return ret

    def check_pre_qualification_method(self, indexstr, ustr):
        """资格预审方法"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bmdjb(self, indexstr, ustr):
        """投标报名"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pre_qualification_date(self, indexstr, ustr):
        """获取资格预审文件时间"""
        """不可为空，日期格式必须为：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_pre_qualification_docplace(self, indexstr, ustr):
        """获取资格预审文件地点"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pre_qualification_docaddr(self, indexstr, ustr):
        """获取资格预审文件地址"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pre_qualification_doc(self, indexstr, ustr):
        """资格预审文件售价"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_signup_date(self, indexstr, ustr):
        """报名时间"""
        """不可为空，日期格式必须为：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_signup_place(self, indexstr, ustr):
        """报名地点"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_contact_phone(self, indexstr, ustr):
        """联系电话"""
        """不可为空，非空则必须为阿拉伯数字，可包含符号横杆-"""
        ret = None
        if ustr and len(ustr):
            if any(c not in public.BANJIAO_NUM + '-' for c in ustr):
                ret = u'不是数字或者-'
            pass
        else:
            ret = u'为空'
        return ret

    def check_prequalification_deaddate(self, indexstr, ustr):
        """提交资格预审申请文件截止时间"""
        """不可为空，日期格式必须为：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_prequalification_date(self, indexstr, ustr):
        """资格预审时间"""
        """不可为空，日期格式必须为：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_send_place(self, indexstr, ustr):
        """递交地点"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_send_address(self, indexstr, ustr):
        """递交地址"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_tender_name(self, indexstr, ustr):
        """招标人名称"""
        """不可为空，至少包含2个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_contact_person(self, indexstr, ustr):
        """联系人"""
        """不可为空，至少包含2个字符"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_contact_phone01(self, indexstr, ustr):
        """联系电话1"""
        """不可为空，非空则必须为阿拉伯数字，可包含符号横杆-"""
        ret = None
        if ustr and len(ustr):
            if any(c not in public.BANJIAO_NUM + '-' for c in ustr):
                ret = u'不是数字或者-'
            pass
        else:
            ret = u'为空'
        return ret

    def check_contact_address(self, indexstr, ustr):
        """联系地址"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_tender_agency_orgname(self, indexstr, ustr):
        """招标代理机构名称"""
        """不可为空，至少包含2个汉字"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_contact_person01(self, indexstr, ustr):
        """联系人1"""
        """不可为空，至少包含2个字符"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个汉字'
        return ret

    def check_contact_phone02(self, indexstr, ustr):
        """联系电话2"""
        """不可为空，非空则必须为阿拉伯数字，可包含符号横杆-"""
        ret = None
        if ustr and len(ustr):
            if any(c not in public.BANJIAO_NUM + '-' for c in ustr):
                ret = u'不是数字或者-'
            pass
        else:
            ret = u'为空'
        return ret

    def check_contact_address01(self, indexstr, ustr):
        """联系地址1"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret


if __name__ == '__main__':
    pass
