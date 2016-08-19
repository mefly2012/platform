# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class ppp():
    """ppp项目"""
    need_check_ziduan = ['project_number',
                         'spplication_body',
                         'project_nisp',
                         'pre_qualification_docplace',
                         'signup_date',
                         'prequalification_deaddate',
                         'prequalification_date',
                         ' tender_name',
                         'contact_person',
                         'tender_agency_orgname',
                         'contact_person01'
                         ]

    def check_project_number(self, indexstr, ustr):
        """项目编号"""
        ret = None
        if ustr and len(ustr):
            if any(c in public.QUANJIAO_EN + public.QUANJIAO_NUM for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_spplication_body(self, indexstr, ustr):
        """授权主体"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_project_nisp(self, indexstr, ustr):
        """项目实施机构"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_pre_qualification_docplace(self, indexstr, ustr):
        """获取资格预审文件时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_signup_date(self, indexstr, ustr):
        """报名时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_prequalification_deaddate(self, indexstr, ustr):
        """提交资格预审申请文件截止时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_prequalification_date(self, indexstr, ustr):
        """资格预审时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_tender_name(self, indexstr, ustr):
        """招标人名称"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_contact_person(self, indexstr, ustr):
        """联系人"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_tender_agency_orgname(self, indexstr, ustr):
        """招标代理机构名称"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_contact_person01(self, indexstr, ustr):
        """联系人1"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret


if __name__ == '__main__':
    a = cdfy_sfgk()
    print a.need_check_ziduan
