# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_sinablog_data():
    """新浪博客"""
    need_check_ziduan = [
        'company_key',
        'pubdate'
    ]

    def check_company_key(self, indexstr, ustr):
        ret = None

        bbd_seed = indexstr['bbd_seed']
        myustr = ''
        if isinstance(bbd_seed, basestring):
            myustr = bbd_seed
        elif isinstance(bbd_seed, dict):
            myustr = bbd_seed['company_name']

        myustr1 = myustr.replace(u'(', u'（').replace(u')', u'）')
        myustr2 = re.compile(u"[ 　.。#＃,，?？/、／＼\\\`~；;•·$￥@！!^…＇’‘＊\\\*%]").sub('',myustr1)

        if myustr2 != ustr:
            ret = u'不一致我的%s' % myustr2
            return ret

        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
                return ret

        return ret

    def check_pubdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        return ret

if __name__=='__main__':
    a=qyxg_sinablog_data()
    print a.check_company_key({'bbd_seed':u'ab*\\\\\de'},'')
