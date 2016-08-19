# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from common import public
import re
import json


class sfpm_taobao():
    """司法拍卖淘宝网"""
    need_check_ziduan = [
        u'auctioneer'
    ]

    def check_auctioneer(self, indexstr, ustr):
        """拍品所有人"""
        ret = None
        try:
            auction_invest_table = indexstr['auction_invest_table']

            items = json.loads(auction_invest_table)
        except Exception as e:
            items = list()
        all_pe = []
        for item in items:
            pe = item.get(u'拍品所有人', '')
            pe = pe.strip(u',;:：、')
            pe = pe.replace(u'\n','')
            pe = pe.split(u'。')[0]
            tmp = None
            match_list = [
                # re.compile(u'^被执行人?：?:?(.+?)。.*$').match(pe),
                # re.compile(u'^被执行人?：(.+?)$').match(pe),
                # re.compile(u'^为被执行人?(.+?)所有$').match(pe),
                # re.compile(u'^被执行人(.?)所有$').match(pe),
                # re.compile(u'^.*为被执行人?(.+?)$').match(pe),
                re.compile(u'^.*?被执行人?为?:?：?(.?|.+?|$)(，女|，男|。|标的|的?名下|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）|钥匙无配|$).*?$').match(pe),
                re.compile(u'^.*?所有权人为?:?：?(.?|.+?|$)(，女|，男|。|标的|的?名下|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）|钥匙无配|$).*?$').match(pe),
                re.compile(u'^.*?登记产权人为?:?：?(.?|.+?|$)(，女|，男|。|标的|的?名下|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）|钥匙无配|$).*?$').match(pe),
                re.compile(u'^登记人?在?为?(.?|.+?|$)(，女|，男|。|标的|的?名下|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）|钥匙无配|$).*?$').match(pe),
                re.compile(u'^为?(.?|.+?|$)(.登记日期|，女|，男|。|标的|的?名下$|的?名下所有|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）|钥匙无配|$).*?$').match(pe),
                # re.compile(u'^.*?被执行人?为?:?：?(.?|.+?|$)(，女|，男|。|标的|的?名下|共同共?有?|所有|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）).*?$').match(pe),
                # re.compile(u'^.*?所有权人为?:?：?(.?|.+?|$)(，女|，男|。.*?|标的.*?|的?名下.*?|共同共?有?.*?|所有.*?|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）){0,1}$').match(pe),
                # re.compile(u'^.*?登记产权人为?:?：?(.?|.+?|$)(，女|，男|。.*?|标的.*?|的?名下.*?|共同共?有?.*?|所有.*?|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）){0,1}$').match(pe),
                # re.compile(u'^登记在?为?(.?|.+?|$)(，女|，男|。.*?|标的.*?|的?名下.*?|共同共?有?.*?|所有.*?|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）){0,1}$').match(pe),
                # re.compile(u'^为?(.?|.+?|$)(，女|，男|，.*?|。.*?|标的.*?|共同共?有?.*?|所有.*?|\(隐去部分内容\)|（隐去部分内容）|(自然人)|（自然人）){0,1}$').match(pe),

                # re.compile(u'^被执行人(.?)$').match(pe),
                # re.compile(u'^为(.+?)[,，].*$').match(pe),
                re.compile(u'^(^|.+?)标的.*$').match(pe)
            ]
            flag = 0
            for match in match_list:
                if match:
                    flag = 1
                    tmp = match.group(1)
                    break

            if flag == 0:
                tmp = pe

            tmp = tmp.lstrip(u'）)').rstrip(u'(（')
            tmp = tmp.strip(u',;；:：、')

            if tmp.count('*') == len(tmp):
                tmp = ''

            tmp = tmp.replace(u',', u';').replace(u'，', u';').replace(u'、', u';').replace(u' ', u';').split(u';')
            all_pe.extend(tmp)

        ustr = set(ustr.split(u';'))
        if ustr != set(all_pe):
            ret = u'不等于我解析的:%s' % ';'.join(all_pe)
        return ret


if __name__ == '__main__':
    a = {
        "auction_invest_table": "[{\"拍品所有人\":\"为罗兴明；登记日期为2012年4月9日。\",\"任春日（登记在吴太洙名下）\":\"房屋用途及土地性质1、住宅用地；2、国有出让土地。钥匙有（√）无（）租赁情况有租赁\",\"权证情况\":\"1、法院执行裁定书；2、房屋所有权证（复印件）；3、土地使用权证（复印件）；\",\"拍品名称\":\"龙泉市龙渊镇水南大水田房产（龙泉市水南二弄63号）\",\"提供的文件\":\"1、法院裁定书；2、协助执行通知书；3、拍卖成交确认书\",\"拍品介绍\":\"1、拍卖对象：坐落于龙泉市龙渊镇水南大水田房产（龙泉市剑池街道水南二弄63号），混合结构，房屋总楼层5层，所在楼层第1、4、5层。权证编号：龙房权证龙渊镇字第00003372号。证载建筑面积共178.8平方米；1层建筑面积：47.30平方米，4层建筑面积：103.46平方米，5层建筑面积：28.04平方米。土地证号:浙龙国用（2007）第2062号，土地使用权面积共33.02平方米，土地使用权类型：出让；地类（用途）：住宅用地，终止日期:2062年12月17日。该房产1层层高约3.42米，4层层高约为3米，5层层高约为3米。2、限购情况：不限购。3、税费负担情况：过户涉及的相关税费，请各竞买人自行向相关职能部门咨询确认，并全部由买受人承担。4、物业情况：物业等费用缴纳情况不明，如存在欠缴，由买受人负担。5、具体看样时间请咨询法院或关注公众微信号：龙泉市人民法院司法网拍\",\"权利限制情况\":\"1、被法院查封2、有抵押\",\"处置依据\":\"司法裁定\"}]",
        "bbd_seed": "", "disposal_unit": "龙泉市人民法院", "_id": "https://sf.taobao.com/sf_item/44834832087.htm|_|4f6b03b2-3540-11e6-9ea5-0cc47a478814|_|2016-06-18",
        "bbd_url": "https://sf.taobao.com/sf_item/44834832087.htm"}
    b = sfpm_taobao().check_auctioneer(a, u'武汉龙达房地产开发有限公司')
    print b
