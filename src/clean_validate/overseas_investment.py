# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class overseas_investment():
    """境外投资"""
    need_check_ziduan = ['operate_scope',
                         'country_region',
                         'domestic_invest_subject',
                         'province',
                         'approval_date',
                         'foreign_invest_enterprises',
                         'certificate_no',
                         'bbd_source',
                         'bbd_dotime'
                         ]
    def check_operate_scope(self, indexstr, ustr):
        """经营范围 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if all(public.is_number(c) for c in ustr):
            #     ret = u"全为数字"
            # elif all(c in public.BANJIAO_EN for c in ustr):
            #     ret = u'全为字母'
        else:
            ret = u'为空'
        return ret

    def check_country_region(self, indexstr, ustr):
        """国家/地区 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if len(re.compile(u'[\u4e00-\u9fa5|（|）]').sub(u'', ustr)) > 0:
            #     ret = u'包含不是汉字也不是括号的字符'
            # elif not public.check_brackets_match(ustr):
            #     ret = u'括号不成对匹配'
        else:
            ret = u'为空'
        return ret

    def check_domestic_invest_subject(self, indexstr, ustr):
        """境内投资主体 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if all(public.is_number(c) for c in ustr):
            #     ret = u"全为数字"
            # elif all(c in public.BANJIAO_EN for c in ustr):
            #     ret = u'全为字母'
            # elif not public.has_count_en(ustr,2) and not public.has_count_hz(ustr,2):
            #     ret = u'没有包含2个字母或中文'
        else:
            ret = u'为空'
        return ret

    def check_province(self, indexstr, ustr):
        """省市 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if any(not public.is_chinese(c) for c in ustr):
                ret = u'不是汉字'
        else:
            ret = u'为空'
        return ret

    def check_approval_date(self, indexstr, ustr):
        """核准日期 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u"为空了"
        return ret

    def check_foreign_invest_enterprises(self, indexstr, ustr):
        """境外投资企业（机构） 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if all(public.is_number(c) for c in ustr):
            #     ret = u"全为数字"
            # elif not public.has_count_en(ustr,2) and not public.has_count_hz(ustr,2):
            #     ret = u'没有包含2个字母或中文'
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.exect_chinese_num(ustr, 1):
                ret = u'出现汉子'
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret
