# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_miit_jlzzdwmd():
    """中标"""
    need_check_ziduan = [
        u'no',
        u'bbd_dotime',
        u'company_key',
        u'company_name',
        u'qualification_level',
        u'location',
        u'certificate_no',
        u'approval_date',
        u'fristissue_date',
        u'bbd_url',
        u'bbd_qyxx_company_id',
        u'bbd_qyxx_branch_id',
        u'bbd_source'
    ]
    def check_no(self, indexstr, ustr):
        """序号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.all_num(ustr):
                ret = u'不是纯数字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """dotime 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_key(self, indexstr, ustr):
        """company_key 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_company_name(self, indexstr, ustr):
        """单位名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_qualification_level(self, indexstr, ustr):
        """资质等级 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'甲级', u'乙级', u'丙级', u'丙级', u'丙级(暂定)'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
        return ret

    def check_location(self, indexstr, ustr):
        """所在省市 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            ret = None
            # if ustr not in public.PROVINCE:
            #     ret = u'不是合法省份'
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证书编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.match(u'^J\d{1,}$', ustr):
                ret = u'不满足J+数字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_approval_date(self, indexstr, ustr):
        """批准（备案）日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_fristissue_date(self, indexstr, ustr):
        """首次获证日期 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 清洗验证"""
        ret = None

        return ret

    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表 清洗验证"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret
