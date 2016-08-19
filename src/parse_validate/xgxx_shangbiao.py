# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class xgxx_shangbiao():
    """商标"""
    need_check_ziduan = [
        'class_brand',
        # 'bbd_qyxx_company_id',
        # 'bbd_qyxx_branch_id'
    ]

    def check_class_brand(self, indexstr, ustr):
        """商标类别"""
        """不为空。必须为“数字”+“-”+“汉字”格式。且数字为[1,45]之间的任意整数，整数对应的汉字必须满足附件《商标类别映射表V1.0 - 20160509》 """
        ret = None
        if ustr and len(ustr):
            match = re.compile(u'^(\d+)-[\u4e00-\u9fa5]+$').match(ustr)
            if match:
                num = int(match.group(1))
                if num > 45 or num < 1:
                    ret = u'数字不是1-45'
                pass
            else:
                ret = u'不满足数字-汉字的规则'
            pass
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
