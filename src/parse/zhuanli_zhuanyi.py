# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public
import json


class zhuanli_zhuanyi():
    """万方专利"""
    need_check_ziduan = [
        u'company_name'
    ]

    def check_company_name(self, indexstr, ustr):
        ret = None
        try:
            bgxx = indexstr['bgxx']
            jsonbgxx = json.loads(bgxx)
            cmlist = []
            for bg in jsonbgxx:
                bgshixiang = bg[u'变更事项']
                if bgshixiang in (u'申请人', u'专利权人'):
                    cm1 = bg.get(u'变更后权利人', None)
                    cm2 = bg.get(u'变更前权利人', None)
                    if cm1:
                        cmlist.append(cm1)
                    if cm2:
                        cmlist.append(cm2)
            cmlist = u';'.join(cmlist)
            cmlist = cmlist.split(u';')
            if ustr and len(ustr):
                company_name_list = ustr.split(u';')
            else:
                company_name_list = []

            if set(company_name_list) != set(cmlist):
                ret = u'不一致，我的是-%s-' % (';'.join(cmlist))
        except Exception as e:
            ret = u'解析不出来'
            pass
        return ret


if __name__ == '__main__':
    a = '{"bbd_xgxx_id": "", "bbd_version": "1.0", "bbd_table": "zhuanli_zhuanyi", "bbd_dotime": "2016年06月14日", "bbd_source": "", "ipc_main_class": "B29C  70/42", "bbd_params": "", "bbd_xgxx_date": "2016年05月17日", "bbd_html": "", "bbd_customer_name": "bbd_dp_parse_user", "company_name": "上海日之升新技术发展有限公司;上海日之升科技有限公司", "bbd_type": "zhuanli_zhuanyi", "bbd_qyxx_branch": "[]", "bbd_uptime": "1.143944488E9", "bgxx": "[{\"变更事项\": \"申请人\", \"变更后权利人\": \"上海日之升科技有限公司\", \"变更前权利人\": \"上海日之升新技术发展有限公司\"}, {\"变更事项\": \"地址\", \"变更后权利人\": \"201107 上海市纪高路1399号1幢\", \"变更前权利人\": \"201109 上海市闵行区沪闵路3078号\"}]", "legal_announce_date": "2016年06月08日", "reg_effect_date": "2016年05月17日", "md5": "7fbc24bbc51490dbc2324b231834c266", "bbd_qyxx_company": "[\"上海日之升新技术发展有限公司\", \"上海日之升科技有限公司\"]", "law_state": "专利申请权、专利权的转移", "bbd_seed": "", "legal_status": "专利申请权的转移", "_id": "CN201310694393.6", "bbd_url": "", "application_code": "CN201310694393.6"}'
    js = json.loads(a)
    # zhuanli_zhuanyi=zhuanli_zhuanyi()
    # print zhuanli_zhuanyi.check_company_name(json.loads(a),u"广东轻工职业技术学院;广东轻工职业技术学院;广州市白云区芳祺化妆品厂")
