# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class jijinye_info():
    """中国基金业协会"""
    need_check_ziduan = ['fund_manager_chinese',
                         'regdate',
                         'esdate',
                         'org_agency_endtime',
                         'special_message',
                         'frname_record',
                         'executive_info'
                         ]

    def check_fund_manager_chinese(self, indexstr, ustr):
        """基金管理人全称(中文)"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_esdate(self, indexstr, ustr):
        """成立时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_org_agency_endtime(self, indexstr, ustr):
        """机构信息最后报告时间"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_special_message(self, indexstr, ustr):
        """特别提示信息"""
        ret = None
        if ustr and len(ustr):
            if '\\r\\n' in ustr:
                ret = u'还有\r\n'
        return ret

    def check_frname_record(self, indexstr, ustr):
        """法定代表人/执行事务合伙人(委派代表)工作履历"""
        ret = None
        if ustr and len(ustr):
            if '\\r\\n' in ustr:
                ret = u'还有\r\n'
        return ret

    def check_executive_info(self, indexstr, ustr):
        """高管信息"""
        ret = None
        if ustr and len(ustr):
            if '\\r\\n' in ustr:
                ret = u'还有\r\n'
        return ret


if __name__ == '__main__':
    pass
