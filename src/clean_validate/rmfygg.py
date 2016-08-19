# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class rmfygg():
    """人民法院公告"""

    need_check_ziduan = [
        'bbd_dotime',
        'notice_people',
        'notice_content',
        'notice_time',
        'notice_type',
        'litigant',
        'attachment',
        'bbd_source'
    ]

    def check_bbd_dotime(self, indexstr, ustr):
        """BBD_DOTIME 清洗校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_notice_people(self, indexstr, ustr):
        """公告人 清洗校验"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        # elif all(public.is_chinese(c) or \
        #                  public.is_include_specialchar(u'）（', c) for c in ustr):
        #     if u'法院' not in ustr:
        #         ret = u"全为汉字但没有法院"
        #     pass
        # else:
        #     ret = u"只要汉字和全角括号"
        return ret

    def check_notice_content(self, indexstr, ustr):
        """公告内容 清洗校验"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u"为空"
        return ret

    def check_notice_time(self, indexstr, ustr):
        """公告时间 清洗校验"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_notice_type(self, indexstr, ustr):
        """公告类型 清洗校验"""
        ret = None
        if ustr and len(ustr):
            ret = None
            # all_solution = [u'仲裁文书', u'公示催告', u'宣告失踪、死亡', u'开庭传票', u'执行文书', u'更正', u'清算公告',
            #                 u'破产文书', u'裁判文书', u'起诉状、上诉状副本', u'起诉状副本及开庭传票', u'拍卖公告', u'遗失声明', u'其他']
            # if ustr not in all_solution:
            #     ret = u"没有满足条件的字段"
        else:
            ret = u'为空'
        return ret

    def check_litigant(self, indexstr, ustr):
        """当事人 清洗校验"""
        ret = None
        if ustr and len(ustr):
            if all(public.is_number(c) for c in ustr):
                ret = u"全为数字"
            elif not public.has_count_hz(ustr, 2) and not public.has_count_en(ustr, 2):
                ret = u'既没有2个汉字又没有2个英文'

        return ret

    def check_attachment(self, indexstr, ustr):
        """附件 清洗校验"""
        ret = None

        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗校验"""
        ret = None

        return ret
