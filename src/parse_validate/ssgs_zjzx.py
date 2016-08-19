# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class ssgs_zjzx():
    """中金在线"""
    need_check_ziduan = [
        # 'bbd_qyxx_company_id',
        # 'bbd_qyxx_branch_id',
        'company_name'
    ]
    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表　"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表　"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
    def check_company_name(self, indexstr, ustr):
        """公司名称　"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

