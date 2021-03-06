# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
import json
from common import public


class qyxg_jyyc():
    """经营异常"""
    need_check_ziduan = [
        u'regno_or_creditcode',
        # u'punish_org',
        # u'busexcep_list',
        u'jyyc',  # u'rank_date',
        # u'remove_date',
        # u'no',
        u'company_name',
        u'rank_busexcep_date',
        u'title'
    ]

    def check_regno_or_creditcode(self, source, ustr):
        """注册号/统一社会信用代码"""
        ret = None
        if ustr and len(ustr):
            if public.check_brackets_match(ustr):
                if any(c in ustr for c in ')('):
                    ret = u'还有成对的括号呢'
            elif len(ustr) > 18:
                ret = u'长度大于18'
            pass
        # else:
        #     ret = u'为空'
        return ret

    def check_jyyc(self, source, ustr):
        def check_punish_org(key, ustr):
            """作出决定机关"""
            ret = None
            # if ustr and len(ustr):
            #     if not public.has_count_hz(ustr, 2):
            #         ret = u'没有两个以上汉字'
            # else:
            #     ret = u'为空'
            return ret

        def check_busexcep_list(key, ustr):
            """列入经营异常名录原因"""
            ret = None
            if ustr and len(ustr):
                if not public.has_count_hz(ustr, 2):
                    ret = u'没有两个以上汉字'
            else:
                ret = u'为空'
            return ret

        def check_rank_date(key, ustr):
            """列入日期"""
            ret = None
            if ustr and len(ustr):
                if not public.date_format(ustr):
                    ret = u"不合法日期"
            return ret

        def check_remove_date(key, ustr):
            """移出日期"""
            ret = None
            if ustr and len(ustr):
                if not public.date_format(ustr):
                    ret = u'不合法日期'
            return ret

        if ustr and len(ustr.strip()):
            obj_jyyc = json.loads(ustr)

            ret = ''
            retlist = []
            for i in obj_jyyc:
                ret1 = check_rank_date('punish_org', i[u'rank_date'])
                ret2 = check_remove_date('punish_orgout', i[u'remove_date'])
                retlist.append(ret1)
                retlist.append(ret2)

            for i in retlist:
                if i:
                    ret += i
            return ret if ret != '' else None
            pass
        else:
            ret = u'为空'

    def check_no(self, source, ustr):
        """序号"""
        ret = None
        if ustr and len(ustr):
            if not public.all_num(ustr):
                ret = u'不是全数字'
        return ret

    def check_company_name(self, source, ustr):
        """企业名称"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        else:
            ret = u'为空'
        return ret

    def check_rank_busexcep_date(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        # else:
        #     ret = u'为空'
        return ret

    def check_title(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2):
                ret = u'没有两个以上汉字'
        return ret


if __name__ == '__main__':
    a = qyxg_jyyc()
    print a.check_regno_or_creditcode(1, u'eee我的')
