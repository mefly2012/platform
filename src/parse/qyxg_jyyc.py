# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
import json
from common import public


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

        obj_jyyc = json.loads(ustr)
        ret = ''
        ret1 = None
        ret2 = None
        ret3 = None
        ret4 = None
        ret5 = None

        for n, i in enumerate(obj_jyyc):
            busexcep_list = i[u'busexcep_list']  # 列入经营异常名录原因
            remove_busexcep_list = i[u'remove_busexcep_list']  # 移出经营异常名录原因
            decision_org = i[u'decision_org']  # 作出决定机关
            punish_org = i[u'punish_org']  # 作出决定机关（列入）
            punish_orgout = i[u'punish_orgout']  # 作出决定机关（移出）
            notice_type = i[u'notice_type']  # 公告类型
            decide_docno = i[u'decide_docno']  # 决定文书号

            if len(busexcep_list.strip()) and not len(remove_busexcep_list.strip()):
                if notice_type != u'列入':
                    ret += u'第%d条 公告类型不为列入\n' % n

                if len(decision_org) and decision_org != punish_org:
                    ret += u'第%d条 作出决定机关不为作出决定机关（列入）\n' % n
            elif not len(busexcep_list.strip()) and len(remove_busexcep_list.strip()):
                if notice_type != u'移出':
                    ret += u'第%d条 公告类型不为移出\n' % n
                if len(decision_org) and decision_org != punish_orgout:
                    ret += u'第%d条 作出决定机关不为作出决定机关（移出）\n' % n
            elif len(busexcep_list.strip()) and len(remove_busexcep_list.strip()):
                if notice_type != u'列入;移出':
                    ret += u'第%d条 公告类型不为列入;移出\n' % n
            if source[u'case_type'] == u'北京':
                if u';' in (punish_org, punish_orgout) or re.compile(u'\d{4}').search(punish_org) \
                        or re.compile(u'\d{4}').search(punish_orgout):
                    ret += u'第%d条 还有分号或者四个数字的在做出决定机关里面' % n

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
    a = jyyc()
    print a.check_company_name(1, u'我。我的')
