# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import json
from common import public


class ssgs_zjzx():
    """中金在线"""
    need_check_ziduan = [
        'company_name'
    ]

    def check_company_name(self, indexstr, ustr):
        ret = None
        company_sitution = indexstr['company_sitution']  # 公司概况
        try:
            tmp = json.loads(company_sitution)
            if tmp[u'公司名称'].replace('(', u'（').replace(')', u'）') != ustr:
                ret = u'公司概况中的公司名称不等于解析的名称'
        except Exception as e:
            ret = u'获取公司名称出错'
        return ret
