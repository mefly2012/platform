# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public

doc_type = 'ktgg'
ip_port = 'dataom3:9200'
db_index = 'dp_cleaner_test_20160524'




class ktgg():
    """开庭公告"""
    need_check_ziduan = [
        u'city',
        u'bbd_dotime'

    ]

    def check_city(self, source, ustr):
        ret = None
        if ustr and len(ustr):
            if unicode(ustr).strip() not in public.PROVINCE:
                ret = u"不为省名"
        return ret

    def check_bbd_dotime(self, source, ustr):
        """bbd_dotime 校验"""
        ret = None
        if ustr and len(ustr):
            if not public.bbd_dotime_date_format(ustr):
                ret = u"不合法日期"
        return ret


