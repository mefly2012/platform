# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class qyxx_ck():
    """采矿权许可"""
    need_check_ziduan = [
        'valid_from',
        'validto',
        'bbd_qyxx_company_id',
        'bbd_qyxx_branch_id'
    ]

    def check_valid_from(self, indexstr, ustr):
        """有效期自"""
        """不为空。必须满足日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        else:
            ret = u'为空'
        return ret

    def check_validto(self, indexstr, ustr):
        """有效期至"""
        """不为空。必须满足日期格式：yyyy年mm月dd日 """
        ret = None

        return ret

    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表"""
        """可为空 """
        ret = None

        return ret

    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表"""
        """可为空 """
        ret = None

        return ret
