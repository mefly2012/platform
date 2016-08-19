# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public


class sfpm_taobao():
    """司法拍卖淘宝网"""
    need_check_ziduan = ['title',
                         'bbd_version',
                         'bbd_table',
                         'bbd_dotime',
                         'bbd_source',
                         'start_price',
                         'bid_announce',
                         'disposal_unit',
                         'bbd_type',
                         'main',
                         'bbd_uptime',
                         'auction_court',
                         'bbd_need_parse',
                         'auction_invest_table',
                         'bid_instructions'
                         ]

    def check_title(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_version(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_table(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_dotime(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u'不为日期格式'
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_source(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_start_price(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bid_announce(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_disposal_unit(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_type(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_main(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_uptime(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_auction_court(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bbd_need_parse(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_auction_invest_table(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret

    def check_bid_instructions(self, indexstr, ustr):
        ret = None
        if ustr and len(ustr):
            pass
        else:
            ret = u'为空'
        return ret
