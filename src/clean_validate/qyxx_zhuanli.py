# -*- coding: utf-8 -*-

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public




class qyxx_zhuanli():
    """中标"""
    need_check_ziduan = [
        u'bbd_version',
        u'bbd_uptime',
        u'bbd_dotime',
        u'company_name',
        u'_id',
        u'patent_type',
        u'application_date',
        u'application_code',
        u'title',
        u'class_code',
        u'address',
        u'nventor_designer',
        u'agent_name',
        u'patent_agency',
        u'application_announce_date',
        u'spplication_notification_num',
        u'priority',
        u'compare_file',
        u'pct_enter_national',
        u'pct_application_data',
        u'pct_publish_data',
        u'division_application',
        u'homeland_prority',
        u'fmgb',
        u'approval_num',
        u'approval_issue_date',
        u'biology_preserve',
        u'bg_publication_date',
        u'fmsq',
        u'xxsq',
        u'wgsq',
        u'decode_announce_date',
        u'bbd_source'
    ]
    def check_bbd_version(self, indexstr, ustr):
        """version 清洗验证"""
        ret = None

        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """uptime 清洗验证"""
        ret = None

        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """do_time 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_company_name(self, indexstr, ustr):
        """company_name 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) \
                    and not public.has_count_en(ustr, 2):
                ret = u'没有2个汉字也没有2个英文'
        else:
            ret = u'为空'
        return ret

    def check__id(self, indexstr, ustr):
        """_id 清洗验证"""
        ret = None

        return ret

    def check_patent_type(self, indexstr, ustr):
        """专利类型 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if ustr not in (u'发明公布', u'外观设计', u'实用新型', u'发明授权', u'发明审定'):
                ret = u'不是指定字段'
        else:
            ret = u'为空'
        return ret

    def check_application_date(self, indexstr, ustr):
        """申请日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        else:
            ret = u'为空'
        return ret

    def check_application_code(self, indexstr, ustr):
        """申请号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        else:
            ret = u'为空'
        return ret

    def check_title(self, indexstr, ustr):
        """标题 清洗验证"""
        ret = None
        if public.str_empty(indexstr, ustr):
            ret = u'为空了'
        return ret

    def check_class_code(self, indexstr, ustr):
        """分类号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        else:
            ret = u'为空'
        return ret

    def check_address(self, indexstr, ustr):
        """地址 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if re.compile(u'^\d{1,}$').match(ustr):
                ret = u'纯数字了'
            elif re.compile(u'^[a-zA-Z]{1,}$').match(ustr):
                ret = u'纯字母了'
        else:
            ret = u'为空'
        return ret

    def check_nventor_designer(self, indexstr, ustr):
        """发明人/设计人 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if not public.has_count_hz(ustr, 2) and \
                    not public.has_count_en(ustr, 2):
                ret = u'没有2个汉字or 字母'
        else:
            ret = u'为空'
        return ret

    def check_agent_name(self, indexstr, ustr):
        """代理人 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) and \
                    not public.has_count_en(ustr, 2):
                ret = u'没有2个汉字or 字母'
        return ret

    def check_patent_agency(self, indexstr, ustr):
        """专利代理机构 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.has_count_hz(ustr, 2) and \
                    not public.has_count_en(ustr, 2):
                ret = u'没有2个汉字or 字母'
        return ret

    def check_application_announce_date(self, indexstr, ustr):
        """申请/授权公告日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        # else:
        #     ret = u'为空'
        return ret

    def check_spplication_notification_num(self, indexstr, ustr):
        """申请/授权公告号 清洗验证"""
        ret = None
        if ustr and len(ustr.strip()):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        # else:
        #     ret = u'为空'
        return ret

    def check_priority(self, indexstr, ustr):
        """优先权 清洗验证"""
        ret = None

        return ret

    def check_compare_file(self, indexstr, ustr):
        """对比文件 清洗验证"""
        ret = None

        return ret

    def check_pct_enter_national(self, indexstr, ustr):
        """PCT进入国家阶段日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_pct_application_data(self, indexstr, ustr):
        """PCT申请数据 清洗验证"""
        ret = None

        return ret

    def check_pct_publish_data(self, indexstr, ustr):
        """PCT公布数据 清洗验证"""
        ret = None

        return ret

    def check_division_application(self, indexstr, ustr):
        """分案原申请 清洗验证"""
        ret = None

        return ret

    def check_homeland_prority(self, indexstr, ustr):
        """本国优先权 清洗验证"""
        ret = None

        return ret

    def check_fmgb(self, indexstr, ustr):
        """fmgb 清洗验证"""
        ret = None

        return ret

    def check_approval_num(self, indexstr, ustr):
        """审定号 清洗验证"""
        ret = None

        return ret

    def check_approval_issue_date(self, indexstr, ustr):
        """审定公告日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_biology_preserve(self, indexstr, ustr):
        """生物保藏 清洗验证"""
        ret = None

        return ret

    def check_bg_publication_date(self, indexstr, ustr):
        """更正文献出版日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_fmsq(self, indexstr, ustr):
        """fmsq 清洗验证"""
        ret = None

        return ret

    def check_xxsq(self, indexstr, ustr):
        """xxsq 清洗验证"""
        ret = None

        return ret

    def check_wgsq(self, indexstr, ustr):
        """wgsq 清洗验证"""
        ret = None

        return ret

    def check_decode_announce_date(self, indexstr, ustr):
        """解密公告日 清洗验证"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr):
                ret = u"不合法日期"
        return ret

    def check_bbd_source(self, indexstr, ustr):
        """数据源 清洗验证"""
        ret = None

        return ret

if __name__=='__main__':
    a=qyxx_zhuanli()
    print a.check_agent_name(1,u'쒃褄⑾譟廆쉝邐邐讐囿譗塾ﾅ蔏ᐏ왟呆币郃邐邐ﾋ譕菬僬噓？䎋謈籐㍗跶ࡻ쾋疉觴疉觤疉觠큵틿䖉㧼ࡵ蔏Ᏹ삅蔏Ꮹ䖋藤࿀솅Ț謀삅蔏᫃䖋诠㈑蕳࿀뾅Ț謀큽ﾅ蔏᫅譟廆譛工ೂ退邐邐')
