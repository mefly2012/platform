# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class domain_name_website_info():
    """企业网站信息"""
    need_check_ziduan = ['_id',
                         'record_license',
                         'bbd_dotime',
                         'approval_time',
                         'bbd_uptime',
                         'bbd_version',
                         'site_certificate_no',
                         'chief_website_name',
                         'website_name',
                         'homepage_url',
                         'domain_name',
                         'organizer_name'
                         ]

    def check__id(self, indexstr, ustr):
        """_id"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_record_license(self, indexstr, ustr):
        """bei_an_hao_xu_ke_zheng_hao"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time"""
        """不为空；为合法的日期格式：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'不能为空'
        return ret

    def check_approval_time(self, indexstr, ustr):
        """shen_he_tong_guo_shi_jian"""
        """不为空。必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'不能为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """version"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_site_certificate_no(self, indexstr, ustr):
        """wang_zhan_bei_an_xu_ke_zheng_hao """
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_chief_website_name(self, indexstr, ustr):
        """wang_zhan_fu_ze_ren_xing_ming"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_website_name(self, indexstr, ustr):
        """wang_zhan_ming_cheng"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_homepage_url(self, indexstr, ustr):
        """wang_zhan_shou_ye_wang_zhi"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_domain_name(self, indexstr, ustr):
        """wang_zhan_yu_ming"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_organizer_name(self, indexstr, ustr):
        """zhu_ban_dan_wei_ming_cheng"""
        """不为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
