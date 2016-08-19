# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_jzsgxkz():
    """中标"""
    need_check_ziduan = [
        u'no',
        u'bbd_dotime',
        u'company_name',
        u'location',
        u'certificate_no',
        u'business_scope',
        u'bbd_qyxx_company_id',
        u'bbd_qyxx_branch_id',
        u'bbd_source'
    ]
    def check_no(self, indexstr, ustr):
        """序号 清洗验证"""
        ret = None
        if ustr != '' and ustr != None:
            if not re.compile('^\d{1,}$').match(str(ustr)):
                ret = u'不是纯数字'
            pass
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

    def check_company_name(self, indexstr, ustr):
        """单位名称 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_location(self, indexstr, ustr):
        """所在省 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in public.PROVINCE:
                ret = u'不是合法省份'
        else:
            ret = u'为空'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """资质证书编号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.digst_english(ustr):
                ret = u'不满足英文+数字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_business_scope(self, indexstr, ustr):
        """业务范围 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
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
