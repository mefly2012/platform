# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import re


class zhixing():
    """被执行人"""
    need_check_ziduan = [
        'idtype'
    ]

    def check_idtype(self, indexstr, ustr):
        """证照类型"""
        ret = None
        pname_id = indexstr['pname_id']
        len1 = len(pname_id)

        if len1 in (8, 9, 10):
            if public.is_organization_code(pname_id):
                if ustr != u'组织机构代码':
                    ret = u'应该为 组织机构代码'
            else:
                if ustr != u'无法查证证照类型':
                    ret = u'应为 无法查证证照类型'
        elif len1 in (13, 15, 16):

            if public.is_registration_number(pname_id):
                if ustr != u'注册号':
                    ret = u'应为注册号'
            else:
                if ustr != u'无法查证证照类型':
                    ret = u'应为 无法查证证照类型'
        elif len1 in (18, 19):
            if len1 == 19:
                if '****' in pname_id:
                    pname_id = unicode(pname_id).replace('****', '***')

            if public.is_identity_code(pname_id):
                if ustr != u'身份证':
                    ret = u'应该为身份证'
            elif public.is_Credit_code(pname_id):
                if ustr != u'统一社会信用代码':
                    ret = u'应该为统一社会信用代码'
            else:
                if ustr != u'无法查证证照类型':
                    ret = u'应为 无法查证证照类型'
        elif len1 > 19:
            if re.compile(u'^[\u4e00-\u9fa5]{7,8}\d{6}号$').match(pname_id):
                if ustr != u'注册号':
                    ret = u'应为注册号'
        else:
            if ustr != u'无法查证证照类型':
                ret = u'应为 无法查证证照类型'
        if ret:
            ret = ret + pname_id
        return ret


if __name__ == '__main__':
    import json

    a = '{"province": "广西", "bbd_xgxx_id": "", "bbd_version": "1.0", "idtype": "身份证", "bbd_table": "dishonesty", "bbd_dotime": "", "bbd_source": "", "concrete_situation": "被执行人无正当理由拒不履行执行和解协议,其他有履行能力而拒不履行生效法律文书确定义务,其它规避执行", "bbd_params": "", "id": "753412", "pubdate": "2014年11月26日", "frname": "", "bbd_html": "", ' \
        '"pname_id": "330822197410100013", "bbd_customer_name": "bbd_dp_parse_user", "bbd_type": "dishonesty", "exec_court_name": "大化瑶族自治县人民法院", "exec_basunit": "大化瑶族自治县人民法院", "bbd_qyxx_branch": "[]", "bbd_uptime": "1.547402526E9", "case_create_time": "2014年03月31日", "pname": "韦银龙", "case_code": "（2014）大法执字第00108号", "exe_code": "（2013）大民初字第667号民事调解书", "md5": "2ff69e2550243aa21ca37be0fb1b5bd9", "bbd_qyxx_company": "[]", "perform_degree": "部分未履行", "bbd_xgxx_date": "2014年03月31日", "bbd_seed": "", "_id": "753412_2015-05-15", "definiteo_bligation": "", "bbd_url": ""}'
    print json.dumps(json.loads(a), ensure_ascii=False, indent=2)
    zhixing = zhixing()
    print zhixing.check_idtype(json.loads(a), u'')
