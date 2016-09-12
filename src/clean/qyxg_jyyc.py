# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
import json
from common import public
import os


class qyxg_jyyc():
    """经营异常"""
    need_check_ziduan = [u'regno_or_creditcode',
                         u'jyyc',  # u'punish_org',
                         # u'jyyc',#u'punish_orgout',
                         # u'jyyc',#ujyyc'decide_docno',
                         # u'jyyc',#u'rank_date',
                         # u'jyyc',#u'remove_date',
                         u'company_name',
                         u'rank_busexcep_date',
                         u'title',
                         ]

    def check_regno_or_creditcode(self, source, ustr):
        """注册号/统一社会信用代码"""
        ret = None
        if ustr and len(ustr):
            if re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5\-]').search(ustr):
                ret = u'还有数字字母汉字-之外的符号'
        return ret

    def check_jyyc(self, source, ustr):

        def check_punish_org(key, ustr):
            """作出决定机关(列入）"""
            ret = None
            if ustr and len(ustr):
                if re.compile(u'\d{4}').search(ustr):  # 有决定文书号
                    if u' ' in ustr:
                        ret = key + u' 还有空格'
                elif any(c in ustr for c in u'】【][)(〔〕［］' + public.QUANJIAO_NUM + public.QUANJIAO_EN):
                    ret = key + u' 还有特殊字符'

            return ret

        def check_punish_orgout(key, ustr):
            """作出决定机关(列出）"""
            ret = None
            if ustr and len(ustr):
                if re.compile(u'\d{4}').search(ustr):  # 有决定文书号
                    if u' ' in ustr:
                        ret = key + u' 还有空格'
                elif any(c in ustr for c in u'】【][)(〔〕［］' + public.QUANJIAO_NUM + public.QUANJIAO_EN):
                    ret = key + u' 还有特殊字符'
            return ret

        def check_decide_docno(key, ustr):
            """决定文书号"""
            ret = None
            if ustr and len(ustr):
                if any(c in ustr for c in u'】【][)(〔〕［］' + public.QUANJIAO_NUM + public.QUANJIAO_EN):
                    ret = key + u' 还有特殊字符'
            return ret

        def check_rank_date(key, ustr):
            """列入日期"""
            ret = None
            if ustr and len(ustr):
                if not public.date_format(ustr):
                    ret = key + u" 不合法日期"
            return ret

        def check_remove_date(key, ustr):
            """移出日期"""
            ret = None
            if ustr and len(ustr):
                if not public.date_format(ustr):
                    ret = key + u' 不合法日期'
            return ret

        need_list = [
            u'punish_org',
            u'punish_orgout',
            u'decide_docno',
            u'rank_date',
            u'remove_date',
        ]
        obj_jyyc = json.loads(ustr)
        ret = ''
        ret1 = None
        ret2 = None
        ret3 = None
        ret4 = None
        ret5 = None
        retlist = []
        for i in obj_jyyc:
            ret1 = check_punish_org('punish_org', i[u'punish_org'])
            ret2 = check_punish_orgout('punish_orgout', i[u'punish_orgout'])
            ret3 = check_decide_docno('decide_docno', i[u'decide_docno'])
            ret4 = check_rank_date('rank_date', i[u'rank_date'])
            ret5 = check_remove_date('remove_date', i[u'remove_date'])

            retlist.extend([ret1, ret2, ret3, ret4, ret5])

        for i in retlist:
            if i:
                ret += i + os.linesep
        return ret if ret != '' else None

    def check_company_name(self, source, ustr):
        """企业名称"""
        ret = None
        # SPECIAL_STR = ur"[ 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%)(]"
        # if ustr and len(ustr):
        #     if re.compile(SPECIAL_STR).search(ustr):
        #         ret = u'包含特殊字符'
        if ustr and len(ustr.strip()):
            for n, v in enumerate(ustr):
                if v in u' 　.。#＃,，?？/、\`~；;•·$￥@！!^…＇’‘＊*%':
                    try:
                        qian = ustr[n - 1]
                    except:
                        qian = ''
                        pass
                    try:
                        hou = ustr[n + 1]
                    except:
                        hou = ''
                    so = qian + hou
                    if any(c in public.BANJIAO_EN for c in so):
                        pass
                    else:
                        ret = u'前后不是英文字符的特殊符号未清理'
                        return ret
            if re.compile(u'[)(]').search(ustr):
                ret = u'还有半角括号'

            return ret

    def check_rank_busexcep_date(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u'不合法日期'
        return ret

    def check_title(self, source, ustr):
        """被列入经营异常名录日期"""
        ret = None
        if ustr and len(ustr):
            if any(x in ustr for x in u')('):
                ret = u'还有半角括号'
        return ret


if __name__ == '__main__':
    a = qyxg_jyyc()
    print a.check_company_name(1, u'我。我的')
