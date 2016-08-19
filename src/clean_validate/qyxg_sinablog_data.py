# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class qyxg_sinablog_data():
    """新浪博客"""
    need_check_ziduan = [
        'bbd_table',
        'bbd_type',
        'bbd_dotime',
        'bbd_uptime',
        'bbd_version',
        'status',
        'table_name',
        'company_key',
        # 'rowkey',
        'bbd_seed',
        'bbd_url',
        'img_src',
        'weibo_account',
        'main',
        'pubdate',
        'transfer_num',
        'comment_num'
    ]

    def check_bbd_table(self, indexstr, ustr):
        """表名"""
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

    def check_bbd_dotime(self, indexstr, ustr):
        """日期"""
        """不可为空，必须为以下日期格式之一：yyyy年mm月dd日、yyyy-mm-dd、yyyy/mm/dd、yyyymmdd、yyyy.mm.dd"""
        ret = None
        if ustr and len(ustr):
            if not public.date_format(ustr=ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        """时间戳"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
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

    def check_status(self, indexstr, ustr):
        """status"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_table_name(self, indexstr, ustr):
        """table_name"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_company_key(self, indexstr, ustr):
        """company_key"""
        """不可为空，必须为两个以上字符"""
        ret = None
        if ustr and len(ustr.strip()):
            if len(ustr) < 2:
                ret = u'没有两个字符'
        else:
            ret = u'为空'
        return ret

    def check_rowkey(self, indexstr, ustr):
        """rowkey"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_seed(self, indexstr, ustr):
        """种子对象"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_url(self, indexstr, ustr):
        """搜索内容的url点进去之后的链接"""
        """可为空，不能包含汉字"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        return ret

    def check_img_src(self, indexstr, ustr):
        """图片"""
        """可为空，不能包含汉字"""
        ret = None
        if ustr and len(ustr):
            if public.has_count_hz(ustr, 1):
                ret = u'有汉字'
        return ret

    def check_weibo_account(self, indexstr, ustr):
        """微博名称"""
        """不可为空，必须为两个以上字符"""
        ret = None
        if ustr and len(ustr.strip()):
            if len(ustr) < 2:
                ret = u'没有两个字符'
            pass
        else:
            ret = u'为空'
        return ret

    def check_main(self, indexstr, ustr):
        """微博内容"""
        """不可为空"""
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_pubdate(self, indexstr, ustr):
        """发布时间"""
        """不可为空，必须为：XXXX-XX-XX XX:XX的格式，X为阿拉伯数字"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$').match(ustr):
                ret = u'不满足格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_transfer_num(self, indexstr, ustr):
        """转发量"""
        """不可为空，必须为整数"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d+$').match(ustr):
                ret = u'不是整数'
        else:
            ret = u'为空'
        return ret

    def check_comment_num(self, indexstr, ustr):
        """评论数"""
        """不可为空，必须为整数"""
        ret = None
        if ustr and len(ustr):
            if not re.compile(u'^\d+$').match(ustr):
                ret = u'不是整数'
        else:
            ret = u'为空'
        return ret


if __name__ == '__main__':
    a = qyxg_sinablog_data()
