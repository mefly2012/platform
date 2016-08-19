# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_medi_jy_prod_cert():
    """药品经营许可证"""
    need_check_ziduan = [
        'company_name',
        'frname',
        'warehouse_address',
        'principal',
        'quality_principal',
        'issue_date',
        'validdate',
        'certificate_no'
    ]
    def check_company_name(self, indexstr, ustr):
        """企业名称"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有全半角状态的空格/*？~﹡ ?#$ ￥ @ ！\ """
        ret = None
        SPECIAL_STR = u" 　#＃＊*×?？/\\／＼~$￥@＄！!)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_frname(self, indexstr, ustr):
        """法定代表人"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有全半角状态的空格/*？~﹡ ?#$ ￥ @ ！，;；\ """
        ret = None
        SPECIAL_STR = u" 　#＃＊*×?？/\\／＼~$￥@＄！!)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_warehouse_address(self, indexstr, ustr):
        """仓库地址"""
        """将包含以下字符的值（模糊匹配）清洗为空值  *  ;  / ﹡ 无"""
        ret = None
        if ustr and len(ustr):
            if public.is_include_specialchar(u'*;/无', ustr):
                ret = u'还有*;/无'
        return ret

    def check_principal(self, indexstr, ustr):
        """企业负责人"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有全半角状态的空格/-*？~﹡ ?#$ ￥ @ ！、，；\ """
        ret = None
        SPECIAL_STR = u" 　#＃＊*×?？/\\／＼~$￥@＄！!)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_quality_principal(self, indexstr, ustr):
        """质量负责人"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）删掉所有全半角状态的空格/-*？~﹡ ?#$ ￥ @ ！、，；\ """
        ret = None
        SPECIAL_STR = u" 　#＃＊*×?？/\\／＼~$￥@＄！!)("
        if ustr and len(ustr):
            if any(c in SPECIAL_STR for c in ustr):
                ret = u'包含特殊字符'
        return ret

    def check_issue_date(self, indexstr, ustr):
        """发证日期"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_validdate(self, indexstr, ustr):
        """有效期至"""
        """需要将所有日期格式统一为：yyyy年mm月dd日。可能出现的日期格式有：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd等合法的日期格式 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_certificate_no(self, indexstr, ustr):
        """证号"""
        """（1）将所有半角括号“()”转换成全角括号“（）”
        （2）将全角数字和字母全部转为半角 """
        ret = None
        if ustr and len(ustr):
            if any(c in (public.QUANJIAO_NUM + public.QUANJIAO_EN + u')(') for c in ustr):
                ret = u'还有全角字母或者数字或者半角括号'
        return ret
