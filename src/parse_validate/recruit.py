# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class recruit():
    """招聘"""
    need_check_ziduan = [
        'bbd_industry',
        'bbd_recruit_num',
        'bbd_salary',
        # 'bbd_qyxx_company_id',
        # 'bbd_qyxx_branch_id',
        'pubdate_doublet'
    ]

    def check_bbd_industry(self, indexstr, ustr):
        """bbd行业划分"""
        """不为空，若非空为汉字 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^\u4e00-\u9fa5;、]').search(ustr):
                ret = u'不全为汉字和英文分号'
        else:
            ret = u'为空'
        return ret

    def check_bbd_recruit_num(self, indexstr, ustr):
        """bbd招聘人数"""
        """不为空，若非空为整数 """
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u'不全为数字'
        else:
            ret = u'为空'
        return ret

    def check_bbd_salary(self, indexstr, ustr):
        """bbd职位薪资"""
        """不为空，为float型数值 """
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^0-9;]').search(ustr):
                ret = u'不全为整数和英文分号'
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

    def check_pubdate_doublet(self, indexstr, ustr):
        """发布时间(排重)"""
        """不为空，格式为：yyyy年mm月 """
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{4}年\d{2}月$').match(ustr):
                ret = u'不合法日期'
        else:
            ret = u'为空'
        return ret
