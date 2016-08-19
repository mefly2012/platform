# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_industrial_production_permit():
    """中标"""
    need_check_ziduan = [
        u'bbd_dotime',
        u'company_name',
        u'issue_date',
        u'validdate',
        u'certificate_no',
        u'location',
        u'attachment',
        u'specification',
        u'instruction',
        u'bbd_source'
    ]
    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """许可证编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.exect_chinese_num(ustr, 1):
                ret = u'不符合格式'
        else:
            ret = u'为空'
        return ret

    def check_location(self, indexstr, ustr):
        """地区 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in public.PROVINCE:
                ret = u'不是合法省份'
        else:
            ret = u'为空'
        return ret

    def check_attachment(self, indexstr, ustr):
        """附件 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^\d{1,}$').match(ustr):
                ret = u'纯数字'
            elif re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'纯字母'
        else:
            ret = u'为空'
        return ret

    def check_specification(self, indexstr, ustr):
        """品种规格 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^\d{1,}$').match(ustr):
                ret = u'纯数字'
            elif re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'纯字母'
        # else:
        #     ret = u'为空'
        return ret

    def check_instruction(self, indexstr, ustr):
        """说明 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if re.compile(u'[\da-zA-Z]').search(ustr):
            #     ret = u'有数字或字母'
        # else:
        #     ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
