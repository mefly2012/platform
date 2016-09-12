# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_zzjgdm():
    """组织机构代码"""
    need_check_ziduan = [
        '_id',
        'bbd_table',
        'bbd_type',
        'bbd_uptime',
        'bbd_dotime',
        'bbd_version',
        'jgdm',
        'jgmc',
        'jgdjzh',
        'credit_code',
        'organization_type',
        'certificate_date',
        'certificate_orgname',
        'esdate',
        'validdate'
    ]

    def check__id(self, indexstr, ustr):
        """唯一id"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_table(self, indexstr, ustr):
        """最终入库表名"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_type(self, indexstr, ustr):
        """表类型"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """时间戳"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """版本号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_jgdm(self, indexstr, ustr):
        """机构代码"""
        """不为空；需满足9位“数字、字母”的组合（必须有数字）或9位纯数字"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^[\da-zA-Z]{9}$').match(ustr):
                if not re.compile(u'[\d]').search(ustr):
                    ret = u'没有数字'
            else:
                ret = u'不满足9位“数字、字母”的组合'
        else:
            ret = u'为空'
        return ret

    def check_jgmc(self, indexstr, ustr):
        """机构名称"""
        """不为空；四个汉字以上，允许有全角括号、数字、英文（但必须有汉字）"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 4):
                ret = u'没有4个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_jgdjzh(self, indexstr, ustr):
        """机构登记证号"""
        """可为空；若非空必须含有数字"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'[\d]').search(ustr):
                ret = u'没有数字'
        return ret

    def check_credit_code(self, indexstr, ustr):
        """统一社会信用代码"""
        """可为空；若非空，需满足18位“数字、字母、*、-”的组合（必须有数字）"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^[\da-zA-Z\*-]{18}$').match(ustr):
                if not re.compile(u'[\d]').search(ustr):
                    ret = u'没有数字'
            else:
                ret = u'不满足18位数字字母*-'
        return ret

    def check_organization_type(self, indexstr, ustr):
        """机构类型"""
        """可为空；若非空则必须为汉字"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.is_allchinese(ustr):
                ret = u'不全为汉字'
        return ret

    def check_certificate_date(self, indexstr, ustr):
        """办证日期"""
        """可为空;不为空则以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr=ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_orgname(self, indexstr, ustr):
        """办证机构名称"""
        """可为空；若非空必须含有汉字"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 1):
                ret = u'没有汉字'
        return ret

    def check_esdate(self, indexstr, ustr):
        """注册日期"""
        """可为空;不为空则以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr):
                ret = u'不满足日期格式'
        return ret

    def check_validdate(self, indexstr, ustr):
        """截止日期"""
        """可为空;不为空则以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr and len(ustr.strip()):
                if not public.date_format(ustr):
                    ret = u'不满足日期格式'
        return ret


if __name__ == '__main__':
    a = qyxg_zzjgdm()
    c = a.check_jgmc(1, 'a11a(b1*1b)cc(a(d1*1d)e)eee')
    print c
