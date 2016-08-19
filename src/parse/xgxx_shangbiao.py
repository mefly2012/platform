# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from common import public



class xgxx_shangbiao():
    """商标"""
    need_check_ziduan = [u'classBrand'
                         ]

    def __init__(self):
        self.leibie = {1: u"工业化学品",
                       2: u"颜料油漆",
                       3: u"日用化学品",
                       4: u"工业用油",
                       5: u"医药制剂",
                       6: u"五金器具",
                       7: u"机械设备",
                       8: u"手工用具",
                       9: u"电子产品",
                       10: u"医疗用品",
                       11: u"家用电器",
                       12: u"运载工具",
                       13: u"军火烟花",
                       14: u"珠宝首饰",
                       15: u"乐器",
                       16: u"文具用品",
                       17: u"橡胶绝缘",
                       18: u"皮革皮具",
                       19: u"建筑材料",
                       20: u"家具工艺",
                       21: u"日用器具",
                       22: u"缆绳袋子",
                       23: u"纺织纱线",
                       24: u"床上用品",
                       25: u"服装鞋帽",
                       26: u"饰品编带",
                       27: u"地席墙帷",
                       28: u"娱乐器械",
                       29: u"食品调料",
                       30: u"副食调料",
                       31: u"林业农业",
                       32: u"啤酒饮料",
                       33: u"酒精饮料",
                       34: u"烟草烟具",
                       35: u"广告销售",
                       36: u"金融地产",
                       37: u"建筑维修",
                       38: u"通讯服务",
                       39: u"运输旅行",
                       40: u"材料处理",
                       41: u"教育娱乐",
                       42: u"设计开发",
                       43: u"餐饮住宿",
                       44: u"医疗美容",
                       45: u"法律服务"
                       }

    def check_classBrand(self, indexstr, ustr):
        """classBrand"""
        ret = None
        if ustr and len(ustr):
            classNo = indexstr.get('classNo', '')
            if classNo:
                leibie = self.leibie.get(classNo, None)
            else:
                ret = u'没获取到classNo'

            if leibie:
                if leibie != ustr:
                    ret = u'类号对应的类别跟解析的不对'
            else:
                ret = u'没获取到类别呢'

        return ret
