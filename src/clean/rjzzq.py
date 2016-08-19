# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class rjzzq():
    """计算机软件著作权登记公告"""

    need_check_ziduan = [u'bbd_dotime',
                         u'key',
                         u'rawdata',
                         u'retain1',
                         u'retain2',
                         u'bbd_url',
                         u'class_code',
                         u'version_num',
                         u'regnum',
                         u'regdate',
                         u'copyright_nationality',
                         u'copyright_owner',
                         u'soft_short',
                         u'date_first_publication'
                         ]
    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_key(self, indexstr, ustr):
        """key 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_rawdata(self, indexstr, ustr):
        """rawdata 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_retain1(self, indexstr, ustr):
        """retain1 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_retain2(self, indexstr, ustr):
        """retain2 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """url 校验"""
        ret = None
        if ustr and len(ustr):
            if u'null' == ustr:
                ret = u'还有null'
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_version_num(self, indexstr, ustr):
        """版本号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_regnum(self, indexstr, ustr):
        """登记号 校验"""
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_EN + public.QUANJIAO_NUM) for c in ustr):
                ret = u'还有全角数字或字母'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_copyright_nationality(self, indexstr, ustr):
        """著作权人国籍 校验"""
        ret = None
        if any(c in u')(' for c in ustr):
            ret = u'半角括号'
        return ret

    def check_copyright_owner(self, indexstr, ustr):
        """著作权人搜索条件 校验"""
        ret = None
        if ustr and len(ustr):
            if u'__' in ustr:
                ret = u'还有__'
        return ret

    def check_soft_short(self, indexstr, ustr):
        """软件简称 校验"""
        ret = None
        if ustr and len(ustr):
            if u'None' in ustr:
                ret = u'还有None'
        return ret

    def check_date_first_publication(self, indexstr, ustr):
        """首次发表日期 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret
