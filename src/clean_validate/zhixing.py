# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public

class zhixing():
    """被执行人"""

    need_check_ziduan = ['company_name',
                         'bbd_dotime',
                         'pname',
                         'case_state',
                         'pname_id',
                         'exec_court_name',
                         'case_create_time',
                         'case_code',
                         'exec_subject',
                         'bbd_source'
                         ]

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有一个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_pname(self, indexstr, ustr):
        """被执行人姓名/名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_case_state(self, indexstr, ustr):
        """案件状态 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'执行中', u'已结案'):
                ret = u'不合情况'
        return ret

    def check_pname_id(self, indexstr, ustr):
        """身份证号码/组织机构代码 清洗验证"""
        ret = None

        return ret

    def check_exec_court_name(self, indexstr, ustr):
        """执行法院 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if u'法院' not in ustr and u'审判庭' not in ustr and u'法庭' not in ustr and u'分院' not in ustr:
                ret = u'不包含法院/审判庭/法庭/分院'
        else:
            ret = u'为空'
        return ret

    def check_case_create_time(self, indexstr, ustr):
        """立案时间 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u"为空"
        return ret

    def check_case_code(self, indexstr, ustr):
        """案号 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'（\d{4}）.*号$').match(ustr):
                ret = u'需要满足格式'
        else:
            ret = u"为空"
        return ret

    def check_exec_subject(self, indexstr, ustr):
        """执行标的 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            try:
                float(ustr)
            except Exception as e:
                ret = u'不能解析成float'
        # else:
        #     ret = u"为空"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret

if __name__=='__main__':
    s={'pname':u"6#"}
    a=zhixing()
    print a.check_pname(1,"6#")

