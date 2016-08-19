# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import time



class qyxx_nyscqyzzcx():
    """农药生产企业资质"""
    need_check_ziduan = [
        'valid_from',
        'validto'
    ]

    def check_valid_from(self, indexstr, ustr):
        """有效期限自"""
        ret = None
        validdate = indexstr['validdate'].strip()
        if validdate and len(validdate):
            err, time = public.get_date(validdate, 0)
            if err:
                ret = err
            else:
                frm = time
                if ustr != frm:
                    ret = u'不等我的是-%s-' % frm

        return ret

    def check_validto(self, indexstr, ustr):
        """有效期限至"""
        ret = None
        validdate = indexstr['validdate'].strip()
        if validdate and len(validdate):
            err, time = public.get_date(validdate, 1)
            if err:
                ret = err
            else:
                frm = time
                if ustr != frm:
                    ret = u'不等我的是-%s-' % frm

        return ret
