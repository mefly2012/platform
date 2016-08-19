# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public


class ygcq_gycqg():
    """阳光产权_国有产权股"""
    need_check_ziduan = ['project_name',
                         'project_number',
                         'listed_price',
                         'listed_startdate',
                         'listed_endtime',
                         'listed_issue_date',
                         'pub_media_name',
                         'object_sitae',
                         'object_company_nature',
                         'esdate',
                         'approve_date',
                         'valuation_date',
                         '_id',
                         'bbd_table',
                         'bbd_type',
                         'bbd_uptime',
                         'bbd_dotime',
                         'bbd_version',
                         'bbd_seed',
                         'bbd_html'
                         ]

    def check_project_name(self, indexstr, ustr):
        """项目名称"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_project_number(self, indexstr, ustr):
        """项目编号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_listed_price(self, indexstr, ustr):
        """标题挂牌价格"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_listed_startdate(self, indexstr, ustr):
        """挂牌起始日期"""
        """不可为空，必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_listed_endtime(self, indexstr, ustr):
        """挂牌截止日期"""
        """不可为空，必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_listed_issue_date(self, indexstr, ustr):
        """标题挂牌公告期"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pub_media_name(self, indexstr, ustr):
        """发布媒体名称"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_object_sitae(self, indexstr, ustr):
        """标的所在地"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_object_company_nature(self, indexstr, ustr):
        """标的企业性质"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_esdate(self, indexstr, ustr):
        """成立时间"""
        """可为空，若非空必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        return ret

    def check_approve_date(self, indexstr, ustr):
        """核准（备案）日期"""
        """可为空，若非空必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        return ret

    def check_valuation_date(self, indexstr, ustr):
        """评估基准日"""
        """可为空，若非空必须满足日期格式：yyyy年mm月dd日"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        return ret

    def check__id(self, indexstr, ustr):
        """唯一id"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_table(self, indexstr, ustr):
        """最终入库表名"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_type(self, indexstr, ustr):
        """表类型"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """时间戳"""
        """不可为空，10位整型，如（uptime: int(time.time())）"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
        """不可为空，日期格式，如（dotime: 2016-06-17）"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        """版本号"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_seed(self, indexstr, ustr):
        """种子对象"""
        """可为空（对接数据平台的企业信息爬虫不可为空）"""
        ret = None

        return ret

    def check_bbd_html(self, indexstr, ustr):
        """网页原文"""
        """可为空（对接数据平台时，此字段置空）"""
        ret = None

        return ret


if __name__ == '__main__':
    pass
