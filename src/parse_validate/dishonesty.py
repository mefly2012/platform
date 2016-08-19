# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class dishonesty():
    """失信被执行人"""
    need_check_ziduan = [
        'idtype',
        # 'bbd_qyxx_company_id',
        # 'bbd_qyxx_branch_id'
    ]

    def check_idtype(self, indexstr, ustr):
        """证照类型"""
        ret = None
        if ustr and len(ustr):
            if ustr not in (u'身份证', u'组织机构代码', u'注册号', u'无法查证证照类型', u'统一社会信用代码'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
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
