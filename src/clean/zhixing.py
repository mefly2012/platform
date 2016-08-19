# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public




class zhixing():
    """被执行人"""
    need_check_ziduan = [
        'company_name',
        'bbd_dotime',

        'pname',
        'case_state',
        'pname_id',
        'case_create_time',
        'case_code',
    ]
    def check_company_name(self, indexstr, ustr):
        """公司名 校验
            不可为空
        """
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%]"
        SPECIAL_STR2 = u'[^ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%]'
        if ustr and len(ustr):
            if re.compile(u'[()]').search(ustr):
                ret = u'包含半角括号'
            elif re.compile(SPECIAL_STR).search(ustr):
                all_str = re.compile(SPECIAL_STR2).sub('', ustr)
                if public.is_allchinese(all_str):
                    ret = u"全中文包含特殊字符"
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """bbd_dotime 校验
            可为空
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
        return ret

    def check_case_state(self, indexstr, ustr):
        """案件状态 校验
            可为空
        """
        ret = None
        if ustr and len(ustr):
            if unicode(ustr) in (u'1', u'0'):
                ret = u"01未清洗"
        return ret

    def check_pname_id(self, indexstr, ustr):
        """身份证号码/组织机构代码 校验
        """
        ret = None
        if ustr and len(ustr):
            Q_Number_English = public.QUANJIAO_EN + public.QUANJIAO_NUM
            delete_str = [u'注册号：', u'工商注册号：', u'执照注册号：', u'无.注册号：', u'渝州注册号：', u'企业法人营业执照注册号：']

            if public.is_allchinese(ustr):
                ret = u"全为汉字未删除"
            elif len(ustr) in (11, 12, 14, 17):
                ret = u"特别的长度未删除"
            elif len(ustr) < 8:
                ret = u"长度<8未删除"
            elif re.compile('[' + Q_Number_English + ']').search(ustr):
                ret = u"存在全角数字或字母"
            elif any(sub in ustr for sub in delete_str):
                ret = u"存在未删除字符串"
            else:
                for c in ustr:
                    if public.is_number(c) \
                            or public.is_alphabet(c) \
                            or public.is_chinese(c) \
                            or c in u'-*、;；':
                        pass
                    else:
                        ret = u"有不为汉字字母数字等的"

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
            if public.is_include_specialchar(u'()', unicode(ustr)):
                ret = u"包含半角括号"
        return ret
