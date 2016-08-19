# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class ygcq_gzgg():
    need_check_ziduan = [u'title',
                         u'city',
                         u'pubdate',
                         u'data_sources',
                         u'company_name_invite'
                         ]

    def check_title(self, source, ustr):
        """title 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'更正公告':
                ret = u"不为更正公告"
        return ret

    def check_city(self, source, ustr):
        """地区 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州':
                ret = u"city不为贵州"
        return ret

    def check_pubdate(self, source, ustr):
        """发布时间 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != ustr.strip():
                ret = u'还有不可见字符'
            elif not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_data_sources(self, source, ustr):
        """数据来源 校验"""
        ret = None
        if ustr and len(ustr):
            if ustr != u'贵州阳光产权':
                ret = u"不为贵州阳光产权"
        return ret

    def check_company_name_invite(self, source, ustr):
        """招标单位名称 校验"""
        ret = None
        SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        if ustr and len(ustr):
            if re.compile(SPECIAL_STR).search(ustr):
                ret = u'包含特殊字符'
        return ret
