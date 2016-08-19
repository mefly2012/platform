# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class shgy_zhongbjg():
    """招标"""
    need_check_ziduan = [
        'project_name',
        # 'project_number',
        'invite_starttime',
        'invite_deadline',
        'bid_opentime',
        # 'data_sources',
        'company_name_invite',
        # 'telephone',
        # 'email',
        # 'fax',
        'agency_name',
        # 'agency_telephone',
        # 'agency_email',
        # 'agency_fax',
        'bidwinning_pubdate',
        'company_name_win',
        # 'bbd_qyxx_company_id',
        # 'bbd_qyxx_branch_id'
    ]

    def check_project_name(self, indexstr, ustr):
        """项目名称　"""
        """可为空。若非空必须包含两个汉字以上（包含两个汉字） """
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
        return ret

    def check_project_number(self, indexstr, ustr):
        """招标项目编号"""
        """可为空"""
        ret = None
        # if ustr and len(ustr):
        #     if not re.compile(u'[a-zA-Z]').search(ustr) \
        #             and not re.compile(u'[0-9]').search(ustr):
        #         ret = u'必须包含数字和字母'
        return ret

    def check_invite_starttime(self, indexstr, ustr):
        """招标起始时间"""
        """可为空。若非空需要满足日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_invite_deadline(self, indexstr, ustr):
        """招标截止时间"""
        """可为空。若非空需要满足日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_bid_opentime(self, indexstr, ustr):
        """开标时间"""
        """可为空。若非空需要满足日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_data_sources(self, indexstr, ustr):
        """数据来源"""
        """可为空 """
        ret = None

        return ret

    def check_company_name_invite(self, indexstr, ustr):
        """招标单位名称"""
        """可为空。若非空必须包含两个汉字以上（包含两个汉字） """
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
        return ret

    def check_telephone(self, indexstr, ustr):
        """联系电话"""
        """可为空 """
        ret = None

        return ret

    def check_email(self, indexstr, ustr):
        """电子邮件"""
        """可为空 """
        ret = None

        return ret

    def check_fax(self, indexstr, ustr):
        """传真"""
        """可为空 """
        ret = None

        return ret

    def check_agency_name(self, indexstr, ustr):
        """代理机构名称"""
        """可为空。若非空必须包含两个汉字以上（包含两个汉字） """
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
        return ret

    def check_agency_telephone(self, indexstr, ustr):
        """代理机构电话"""
        """可为空 """
        ret = None

        return ret

    def check_agency_email(self, indexstr, ustr):
        """代理机构电子邮件"""
        """可为空 """
        ret = None

        return ret

    def check_agency_fax(self, indexstr, ustr):
        """代理机构传真"""
        """可为空 """
        ret = None

        return ret

    def check_bidwinning_pubdate(self, indexstr, ustr):
        """中标公告发布时间"""
        """可为空。若非空需要满足日期格式：yyyy年mm月dd日 """
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_company_name_win(self, indexstr, ustr):
        """中标企业"""
        """可为空。若非空则必须包含两个汉字以上（包含两个汉字），允许有“）”、“/”或“,”或“、”等符号（必须有中文） """
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有2个以上汉字'
        return ret

    def check_bbd_qyxx_company_id(self, indexstr, ustr):
        """公司关联企业唯一ID列表"""
        """可为空 """
        ret = None

        return ret

    def check_bbd_qyxx_branch_id(self, indexstr, ustr):
        """分支机构关联企业唯一ID列表"""
        """可为空 """
        ret = None

        return ret
