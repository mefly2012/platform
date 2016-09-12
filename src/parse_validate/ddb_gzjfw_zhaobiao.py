# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ddb_gzjfw_zhaobiao():
    need_check_ziduan = ['source_funds',
                         'invite_starttime',
                         'invite_deadline',
                         'bid_opentime',
                         'data_sources',
                         'company_name_invite',
                         'agency_name',
                         'bidwinning_pubdate',
                         'company_name_win'
                         ]

    def check_source_funds(self, indexstr, ustr):
        """资金来源"""
        """可为空。"""
        ret = None

        return ret

    def check_invite_starttime(self, indexstr, ustr):
        """招标起始时间"""
        """可为空。若非空需要满足日期格式：yyyy-mm-dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不合法日期'
        return ret

    def check_invite_deadline(self, indexstr, ustr):
        """招标截止时间"""
        """可为空。若非空需要满足日期格式：yyyy-mm-dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不合法日期'
        return ret

    def check_bid_opentime(self, indexstr, ustr):
        """开标时间"""
        """可为空。若非空需要满足日期格式：yyyy-mm-dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不合法日期'
        return ret

    def check_data_sources(self, indexstr, ustr):
        """数据来源"""
        """可为空，若非空则为“贵州招标投标网”"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州公共资源交易中心':
                ret = u'贵州公共资源交易中心'
        return ret

    def check_company_name_invite(self, indexstr, ustr):
        """招标单位名称"""
        """可为空。若非空必须包含两个汉字以上（包含两个汉字）"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个汉字'
        return ret

    def check_agency_name(self, indexstr, ustr):
        """代理机构名称"""
        """可为空。若非空必须包含两个汉字以上（包含两个汉字）"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个汉字'
        return ret

    def check_bidwinning_pubdate(self, indexstr, ustr):
        """中标公告发布时间"""
        """可为空。若非空需要满足日期格式：yyyy-mm-dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不合法日期'
        return ret

    def check_company_name_win(self, indexstr, ustr):
        """中标企业"""
        """可为空。若非空则必须包含两个汉字以上（包含两个汉字），允许有“）”、“/”或“,”或“、”等符号（必须有中文）"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个汉字'
        return ret
