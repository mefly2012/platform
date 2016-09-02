# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_zzjgdm():
    """组织机构代码"""
    need_check_ziduan = [
        'jgmc',
        'certificate_date',
        'esdate',
        'validdate'
    ]

    def check_jgmc(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr.strip()):
            ustr = re.compile(u'\(.*\)').sub('', ustr)
            for n, v in enumerate(ustr):
                if v in u' 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%':
                    try:
                        qian = ustr[n - 1]
                    except:
                        qian = ''
                        pass
                    try:
                        hou = ustr[n + 1]
                    except:
                        hou = ''
                    so = qian + hou
                    if any(c in public.BANJIAO_EN for c in so):
                        pass
                    else:
                        ret = u'前后不是英文字符的特殊符号未清理'
                        return ret
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'

        return ret

    def check_certificate_date(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret

    def check_esdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret

    def check_validdate(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret


if __name__ == '__main__':
    a = qyxg_zzjgdm()
    c = a.check_company_name(1, 'a11a(b1*1b)cc(a(d1*1d)e)eee')
    print c
