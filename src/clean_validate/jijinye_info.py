# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class jijinye_info():
    """中国基金业协会"""
    need_check_ziduan = ['fund_manager_chinese',
                         'fund_manager_english',
                         'regnum',
                         'pname_id',
                         'regdate',
                         'esdate',
                         'reg_address',
                         'office_address',
                         'regcap_millon',
                         '"pic_millon"',
                         'company_nature',
                         'regcap_paidpro',
                         'managed_fund_type',
                         'employees',
                         'frname_name',
                         'ifcareer_qualification',
                         'entitled_way',
                         'org_agency_endtime',
                         'frname_record',
                         'executive_info',
                         '_id',
                         'bbd_dotime',
                         'bbd_uptime',
                         'bbd_version'
                         ]

    def check_fund_manager_chinese(self, indexstr, ustr):
        """基金管理人全称(中文)"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_fund_manager_english(self, indexstr, ustr):
        """基金管理人全称(英文)"""
        # """不为空"""
        ret = None
        # if ustr and len(ustr.strip()):
        #     pass
        # else:
        #     ret = u'为空'
        return ret

    def check_regnum(self, indexstr, ustr):
        """登记编号"""
        """不为空；为“P”+“XXXXXXX”的组合，X为0到9的阿拉伯数字"""
        ret = None
        if ustr and len(ustr.strip()):
            if not re.compile(u'^P\d{7}$').match(ustr):
                ret = u'不为为“P”+“XXXXXXX”的组合'
            pass
        else:
            ret = u'为空'
        return ret

    def check_pname_id(self, indexstr, ustr):
        """组织机构代码"""
        """不为空；不含汉字"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[\u4e00-\u9fa5]').search(ustr):
                ret = u'有汉字'
            pass
        else:
            ret = u'为空'
        return ret

    def check_regdate(self, indexstr, ustr):
        """登记时间"""
        """不为空；为以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_esdate(self, indexstr, ustr):
        """成立时间"""
        """不为空；为以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_reg_address(self, indexstr, ustr):
        """注册地址"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_office_address(self, indexstr, ustr):
        """办公地址"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_regcap_millon(self, indexstr, ustr):
        """注册资本(万元)"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pic_millon(self, indexstr, ustr):
        """实缴资本(万元)"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_company_nature(self, indexstr, ustr):
        """企业性质"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_regcap_paidpro(self, indexstr, ustr):
        """注册资本实缴比例"""
        """不为空;为0或者百分数，可包含半角状态下的‘.’符号"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'[^\d\.]').search(ustr):
                ret = u'不符合格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_managed_fund_type(self, indexstr, ustr):
        """管理基金主要类别"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_employees(self, indexstr, ustr):
        """员工人数"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_frname_name(self, indexstr, ustr):
        """法定代表人/执行事务合伙人(委派代表)姓名"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_ifcareer_qualification(self, indexstr, ustr):
        """是否有从业资格"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_entitled_way(self, indexstr, ustr):
        """资格取得方式"""
        """可为空;若非空，为‘资格认定’或‘通过考试’两种"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'资格认定', u'通过考试'):
                ret = u'不为‘资格认定’或‘通过考试’两种'

        return ret

    def check_org_agency_endtime(self, indexstr, ustr):
        """机构信息最后报告时间"""
        """可为空；不为空则以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.date_format(ustr):
                ret = u'不为日期格式'
        return ret

    def check_frname_record(self, indexstr, ustr):
        """法定代表人/执行事务合伙人(委派代表)工作履历"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_executive_info(self, indexstr, ustr):
        """高管信息"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check__id(self, indexstr, ustr):
        """_id"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version"""
        """不为空"""
        ret = None
        if ustr and len(ustr.strip()):
            pass
        else:
            ret = u'为空'
        return ret


if __name__ == '__main__':
    a = jijinye_info()
    print a.check_regcap_paidpro(1, u'2-6')
    pass
