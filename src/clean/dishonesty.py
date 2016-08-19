# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class dishonesty():
    """失信被执行人"""
    need_check_ziduan = [u'bbd_dotime',
                         u'pname',
                         u'pname_id',
                         u'frname',
                         u'province',
                         u'exe_code',
                         u'case_create_time',
                         u'case_code',
                         u'pubdate'
                         ]
    ########################规则######################################

    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验
            可以为空
        """
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_pname(self, indexstr, ustr):
        """ 被执行人姓名/名称 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u"()、,，；/\\" for c in unicode(ustr)):
                ret = u"存在特殊字符"
            elif unicode(ustr).endswith(u'。'):
                ret = u"以。结尾"
        return ret

    def check_pname_id(self, indexstr, ustr):
        """身份证号码/组织机构代码 校验
            可为空
        """
        ret = None
        if ustr and len(ustr):
            for c in ustr:
                if public.is_number(c) \
                        or public.is_alphabet(c) \
                        or public.is_chinese(c) \
                        or c in '-*':
                    pass
                else:
                    ret = u"存在特殊字符"
                if u'--' in ustr:
                    ret = u'有--'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人或者负责人姓名 校验
            可为空
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u" 　()、,，/／。\\＼" for c in ustr):
                ret = u"存在特殊字符"
        return ret

    def check_province(self, indexstr, ustr):
        """省份 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if ustr not in public.PROVINCE:
                ret = u"不为省名"
        return ret

    def check_exe_code(self, indexstr, ustr):
        """执行依据文号 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u" 　()【】[]］［、,，；。.．：:" for c in unicode(ustr)):
                ret = u"存在特殊字符"
        return ret

    def check_case_create_time(self, indexstr, ustr):
        """立案时间 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_case_code(self, indexstr, ustr):
        """案号 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'()', ustr):
                ret = u"包含半角括号"
        return ret

    def check_exec_basunit(self, indexstr, ustr):
        """做出执行依据单位 校验
            可为空
        """
        ret = None
        if ustr and len(ustr):
            if any(c in u" 　()、,，；" for c in ustr):
                ret = u"存在特殊字符"
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间 校验
            不可为空
        """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"pubdate不合法日期"
        return ret
        ##############################################################


