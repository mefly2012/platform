# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public


class zgcpwsw():
    """裁判文书"""
    need_check_ziduan = ['action_cause',
                         'caseout_come',
                         'court_litigant',
                         'pro_litigant',
                         'def_litigant',
                         'pro_other_related',
                         'def_other_related',
                         'applicable_law',
                         'company_name'

                         ]

    # def check_action_cause(self, indexstr, ustr):
    #     """案由"""
    #     """可为空，若非空至少包含2个中文汉字"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2):
    #             ret = u'没有2个以上汉字'
    #     return ret
    #
    # def check_caseout_come(self, indexstr, ustr):
    #     """案件结果"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_court_litigant(self, indexstr, ustr):
    #     """法院当事人"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_pro_litigant(self, indexstr, ustr):
    #     """起诉方当事人"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_def_litigant(self, indexstr, ustr):
    #     """被诉方当事人"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_pro_other_related(self, indexstr, ustr):
    #     """起诉方其他相关人"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_def_other_related(self, indexstr, ustr):
    #     """被诉方其他相关人"""
    #     """可为空，若非空至少包含两个中文汉字或两个英文字母"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 2) \
    #                 and not public.has_count_en(ustr, 2):
    #             ret = u'没有2个以上汉字页没有2个英文字母'
    #     return ret
    #
    # def check_applicable_law(self, indexstr, ustr):
    #     """适用法条"""
    #     """可为空，若非空必须存在5个以上的汉字"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not public.has_count_hz(ustr, 5):
    #             ret = u'没有5个汉字'
    #     return ret
    #
    # def check_litigant_type(self, indexstr, ustr):
    #     """当事人类型"""
    #     """可为空"""
    #     ret = None
    #
    #     return ret
    #
    # def check_court_acceptance_fee(self, indexstr, ustr):
    #     """受理费"""
    #     """可为空，若非空为数字+单位的格式"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if not re.compile(u'^\d{1,}(元|\$)$').match(ustr):
    #             ret = u'不符合格式数字+单位'
    #     return ret
    #
    # def check_doc_type(self, indexstr, ustr):
    #     """文书类型"""
    #     """可为空"""
    #     ret = None
    #
    #     return ret
    #
    # def check_historycase(self, indexstr, ustr):
    #     """历审案例"""
    #     """可为空，必须全为汉字，且包含“法院”两字"""
    #     ret = None
    #     if ustr and len(ustr):
    #         if public.is_allchinese(ustr):
    #             if u'法院' not in ustr:
    #                 ret = u'不包含法院二字'
    #         else:
    #             ret = u'不全为汉字'
    #     return ret
    ##################以下是因为合表
    def check_action_cause(self, indexstr, ustr):
        """案由"""
        """可为空，若非空至少包含2个中文汉字"""
        bbd_table = indexstr['bbd_type']
        ret = None
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2):
                    ret = u'%s没有2个以上汉字' % bbd_table
        return ret

    def check_caseout_come(self, indexstr, ustr):
        """案件结果"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'itslaw', 'qyxg_zgcpwsw', 'qyxg_wscpws'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_court_litigant(self, indexstr, ustr):
        """法院当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw', 'qyxg_wscpws'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_pro_litigant(self, indexstr, ustr):
        """起诉方当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_def_litigant(self, indexstr, ustr):
        """被诉方当事人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_pro_other_related(self, indexstr, ustr):
        """起诉方其他相关人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_def_other_related(self, indexstr, ustr):
        """被诉方其他相关人"""
        """可为空，若非空至少包含两个中文汉字或两个英文字母"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2) \
                        and not public.has_count_en(ustr, 2):
                    ret = u'%s没有2个以上汉字页没有2个英文字母' % bbd_table
        return ret

    def check_applicable_law(self, indexstr, ustr):
        """适用法条"""
        """可为空，若非空必须存在5个以上的汉字"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('zgcpwsw', 'itslaw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 5):
                    ret = u'%s没有5个汉字' % bbd_table
        return ret

    def check_company_name(self, indexstr, ustr):
        """历审案例"""
        """可为空，必须全为汉字，且包含“法院”两字"""
        ret = None
        bbd_table = indexstr['bbd_type']
        if bbd_table in ('qyxg_zgcpwsw'):
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 5):
                    ret = u'%s没有5个汉字' % bbd_table
            else:
                ret = u'%s为空' % bbd_table
        return ret
