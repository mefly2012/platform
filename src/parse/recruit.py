# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
import codecs
import time
import os
from common import public


class recruit():
    """招聘"""
    need_check_ziduan = ['bbd_industry',
                         'bbd_recruit_num',
                         'bbd_salary',
                         'pubdate_doublet'
                         ]

    def __init__(self):

        self.industry_hangye = {
            u'化学操作': u'制造业',
            u'品牌专员/助理': u'其他',
            u'商务经理/主管': u'其他',
            u'实习生': u'其他',
            u'家用电器/数码产品研发': u'制造业',
            u'房地产项目策划专员/助理': u'房地产业',
            u'担保业务': u'金融业',
            u'招聘专员/助理': u'其他',
            u'汽车售后服务/客户服务': u'其他',
            u'物业招商管理': u'其他',
            u'用户界面（UI）设计': u'信息传输、软件和信息技术服务业',
            u'电子商务经理/主管': u'其他',
            u'畜牧师': u'农、林、牧、渔业',
            u'科研人员': u'科学研究和技术服务业',
            u'CNC/数控工程师': u'制造业',
            u'光源/照明工程师': u'制造业',
            u'化妆师': u'其他',
            u'化妆师/造型师/服装/道具': u'其他',
            u'印刷操作': u'文化、体育和娱乐业',
            u'后勤人员': u'其他',
            u'客户服务经理': u'其他',
            u'广告客户总监': u'其他',
            u'投资银行业务': u'金融业',
            u'服务员': u'其他',
            u'法务专员/助理': u'租赁和商务服务业',
            u'法语翻译': u'租赁和商务服务业',
            u'珠宝/收藏品鉴定': u'其他',
            u'硬件工程师': u'信息传输、软件和信息技术服务业',
            u'缝纫工': u'制造业',
            u'美发/发型师': u'居民服务、修理和其他服务业',
            u'风险控制': u'其他',
            u'保险产品开发/项目策划': u'金融业',
            u'公关主管': u'其他',
            u'售前/售后技术支持工程师': u'其他',
            u'塑料工程师': u'制造业',
            u'情报信息分析': u'信息传输、软件和信息技术服务业',
            u'服装/纺织/皮革跟单': u'制造业',
            u'测试工程师': u'信息传输、软件和信息技术服务业',
            u'游戏界面设计': u'信息传输、软件和信息技术服务业',
            u'牙科医生': u'卫生和社会工作',
            u'生产项目经理/主管': u'制造业',
            u'税务专员/助理': u'租赁和商务服务业',
            u'记者/采编': u'其他',
            u'贸易跟单': u'交通运输、仓储和邮政业',
            u'高中教师': u'教育',
            u'ERP实施顾问': u'租赁和商务服务业',
            u'业务拓展经理/主管': u'其他',
            u'人力资源总监': u'其他',
            u'儿科医生': u'卫生和社会工作',
            u'医疗器械维修/保养': u'制造业',
            u'医疗管理人员': u'卫生和社会工作',
            u'小学教师': u'教育',
            u'市场主管': u'其他',
            u'服装/纺织/皮革项目管理': u'制造业',
            u'演员/模特': u'其他',
            u'生产物料管理（PMC）': u'制造业',
            u'美术教师': u'教育',
            u'销售数据分析': u'信息传输、软件和信息技术服务业',
            u'饲料销售': u'农、林、牧、渔业',
            u'IT文档工程师': u'信息传输、软件和信息技术服务业',
            u'动物营养/饲料研发': u'农、林、牧、渔业',
            u'工艺/制程工程师': u'制造业',
            u'建筑制图': u'建筑业',
            u'数据分析师': u'信息传输、软件和信息技术服务业',
            u'机械设备工程师': u'制造业',
            u'首席执行官CEO/总裁/总经理': u'其他',
            u'IC验证工程师': u'其他',
            u'产品/品牌专员': u'其他',
            u'人力资源经理': u'其他',
            u'会务/会展主管': u'其他',
            u'园林/景观设计': u'农、林、牧、渔业',
            u'建筑工程师': u'建筑业',
            u'总裁助理/总经理助理': u'其他',
            u'汽车销售': u'批发和零售业',
            u'理货/分拣/打包': u'批发和零售业',
            u'移动通信工程师': u'信息传输、软件和信息技术服务业',
            u'证券/投资客户代表': u'金融业',
            u'通信研发工程师': u'信息传输、软件和信息技术服务业',
            u'音乐教师': u'教育',
            u'IT项目经理/主管': u'信息传输、软件和信息技术服务业',
            u'公关专员': u'其他',
            u'出纳员': u'其他',
            u'医疗器械生产/质量管理': u'制造业',
            u'医药化学分析': u'制造业',
            u'物料经理': u'制造业',
            u'电子/电器维修/保养': u'制造业',
            u'系统架构设计师': u'信息传输、软件和信息技术服务业',
            u'进出口/信用证结算': u'其他',
            u'销售工程师': u'其他',
            u'项目经理/项目主管': u'信息传输、软件和信息技术服务业',
            u'首席财务官CFO': u'其他',
            u'IT技术支持/维护经理': u'信息传输、软件和信息技术服务业',
            u'三维/3D设计/制作': u'其他',
            u'专业顾问': u'租赁和商务服务业',
            u'产品主管': u'其他',
            u'团购经理/主管': u'其他',
            u'培训专员/助理': u'教育',
            u'客户主管': u'其他',
            u'家教': u'教育',
            u'成本会计': u'其他',
            u'手缝工': u'制造业',
            u'文字编辑/组稿': u'其他',
            u'水利/水电工程师': u'水利、环境和公共设施管理业',
            u'汽车喷漆': u'其他',
            u'活动执行': u'其他',
            u'物流总监': u'交通运输、仓储和邮政业',
            u'电子商务专员/助理': u'租赁和商务服务业',
            u'电气线路设计': u'制造业',
            u'航空乘务': u'交通运输、仓储和邮政业',
            u'项目总监': u'信息传输、软件和信息技术服务业',
            u'食品加工/处理': u'住宿和餐饮业',
            u'CTO/CIO': u'其他',
            u'制造工程师': u'制造业',
            u'医药技术研发管理人员': u'卫生和社会工作',
            u'厨工': u'住宿和餐饮业',
            u'大堂经理/领班': u'其他',
            u'媒介策划/管理': u'其他',
            u'嵌入式硬件开发(主板机…)': u'信息传输、软件和信息技术服务业',
            u'工业设计': u'制造业',
            u'市场营销经理': u'其他',
            u'市政工程师': u'建筑业',
            u'平面设计': u'制造业',
            u'广告美术指导': u'其他',
            u'机械设计师': u'制造业',
            u'电力工程师/技术员': u'电力、热力、燃气及水生产和供应业',
            u'船舶乘务': u'交通运输、仓储和邮政业',
            u'运输经理/主管': u'交通运输、仓储和邮政业',
            u'销售行政经理/主管': u'其他',
            u'IT质量管理经理/主管': u'信息传输、软件和信息技术服务业',
            u'互联网软件工程师': u'信息传输、软件和信息技术服务业',
            u'产品专员/助理': u'其他',
            u'企业律师/合规经理/主管': u'租赁和商务服务业',
            u'会务/会展专员': u'其他',
            u'地勤人员': u'其他',
            u'外贸/贸易经理/主管': u'交通运输、仓储和邮政业',
            u'幕墙工程师': u'建筑业',
            u'房地产项目开发报建': u'房地产业',
            u'电脑放码员': u'信息传输、软件和信息技术服务业',
            u'货运代理': u'交通运输、仓储和邮政业',
            u'资产评估': u'租赁和商务服务业',
            u'项目经理/主管': u'信息传输、软件和信息技术服务业',
            u'IT项目执行/协调人员': u'信息传输、软件和信息技术服务业',
            u'业务拓展专员/助理': u'其他',
            u'作家/编剧/撰稿人': u'其他',
            u'包装工程师': u'制造业',
            u'培训助理/助教': u'教育',
            u'嵌入式软件开发': u'信息传输、软件和信息技术服务业',
            u'店员/营业员/导购员': u'其他',
            u'意大利语翻译': u'租赁和商务服务业',
            u'房地产销售/置业顾问': u'房地产业',
            u'核保理赔': u'金融业',
            u'电器研发工程师': u'制造业',
            u'移动互联网开发': u'信息传输、软件和信息技术服务业',
            u'系统工程师': u'信息传输、软件和信息技术服务业',
            u'证券/投资客户总监': u'金融业',
            u'食品/饮料研发': u'住宿和餐饮业',
            u'供应商/采购质量管理': u'交通运输、仓储和邮政业',
            u'农艺师': u'农、林、牧、渔业',
            u'医疗器械推广': u'制造业',
            u'合同管理': u'其他',
            u'园艺师': u'农、林、牧、渔业',
            u'安防系统工程师': u'信息传输、软件和信息技术服务业',
            u'按摩/足疗': u'居民服务、修理和其他服务业',
            u'数据库管理员': u'信息传输、软件和信息技术服务业',
            u'物业管理专员/助理': u'房地产业',
            u'特效设计': u'信息传输、软件和信息技术服务业',
            u'生物工程/生物制药': u'制造业',
            u'网络与信息安全工程师': u'信息传输、软件和信息技术服务业',
            u'网络工程师': u'信息传输、软件和信息技术服务业',
            u'美容顾问(BA)': u'租赁和商务服务业',
            u'药品研发': u'卫生和社会工作',
            u'软件研发工程师': u'信息传输、软件和信息技术服务业',
            u'通信项目管理': u'信息传输、软件和信息技术服务业',
            u'产品工艺/制程工程师': u'制造业',
            u'化学分析': u'制造业',
            u'后期制作': u'其他',
            u'服装打样/制版': u'制造业',
            u'物业维修': u'房地产业',
            u'证券/投资客户经理': u'金融业',
            u'配置管理工程师': u'信息传输、软件和信息技术服务业',
            u'银行客户主管': u'金融业',
            u'会计经理/主管': u'其他',
            u'助理/秘书/文员': u'其他',
            u'包装设计': u'制造业',
            u'单证员': u'其他',
            u'商务专员/助理': u'租赁和商务服务业',
            u'客户代表': u'其他',
            u'市场调研与分析': u'信息传输、软件和信息技术服务业',
            u'投资/理财服务': u'金融业',
            u'拍卖师': u'金融业',
            u'文科教师': u'教育',
            u'电子/电器工程师': u'制造业',
            u'网店模特': u'其他',
            u'网络/在线销售': u'信息传输、软件和信息技术服务业',
            u'能源/矿产项目管理': u'采矿业',
            u'营养师': u'居民服务、修理和其他服务业',
            u'银行经理/主任': u'金融业',
            u'中医科医生': u'卫生和社会工作',
            u'保姆/母婴护理': u'卫生和社会工作',
            u'化工项目管理': u'制造业',
            u'广告制作执行': u'其他',
            u'店面/展览/展示/陈列设计': u'制造业',
            u'数据库开发工程师': u'信息传输、软件和信息技术服务业',
            u'校长/副校长': u'教育',
            u'水处理工程师': u'电力、热力、燃气及水生产和供应业',
            u'汽车装配工艺工程师': u'制造业',
            u'生产主管/督导/组长': u'制造业',
            u'生产运营管理': u'制造业',
            u'电路工程师/技术员': u'制造业',
            u'行政总监': u'其他',
            u'行长/副行长': u'金融业',
            u'阿拉伯语翻译': u'租赁和商务服务业',
            u'IT技术/研发经理/主管': u'信息传输、软件和信息技术服务业',
            u'IT技术文员/助理': u'信息传输、软件和信息技术服务业',
            u'产品管理': u'其他',
            u'典当业务': u'金融业',
            u'化验/检验科医师': u'卫生和社会工作',
            u'培训师/讲师': u'教育',
            u'培训督导': u'教育',
            u'机动车司机/驾驶': u'其他',
            u'物流/仓储调度': u'交通运输、仓储和邮政业',
            u'环境评价工程师': u'水利、环境和公共设施管理业',
            u'生产总监': u'制造业',
            u'电脑操作/打字/录入员': u'信息传输、软件和信息技术服务业',
            u'网络/在线客服': u'信息传输、软件和信息技术服务业',
            u'ERP技术开发': u'信息传输、软件和信息技术服务业',
            u'保安经理': u'房地产业',
            u'分公司/代表处负责人': u'其他',
            u'医疗器械研发': u'制造业',
            u'地质勘查/选矿/采矿': u'采矿业',
            u'培训生': u'教育',
            u'外汇交易': u'金融业',
            u'外贸/贸易专员/助理': u'交通运输、仓储和邮政业',
            u'成本经理/主管': u'其他',
            u'房地产评估': u'房地产业',
            u'房地产销售主管': u'房地产业',
            u'搬运工': u'建筑业',
            u'收银员': u'金融业',
            u'旅游顾问': u'租赁和商务服务业',
            u'服装/纺织/皮革工艺师': u'制造业',
            u'架线和管道工程技术': u'制造业',
            u'水工/木工/油漆工': u'建筑业',
            u'系统集成工程师': u'信息传输、软件和信息技术服务业',
            u'绩效考核专员/助理': u'其他',
            u'网站编辑': u'信息传输、软件和信息技术服务业',
            u'配音员': u'其他',
            u'采购经理/主管': u'交通运输、仓储和邮政业',
            u'销售运营经理/主管': u'其他',
            u'信息技术经理/主管': u'信息传输、软件和信息技术服务业',
            u'切割技工': u'制造业',
            u'前台/总机/接待': u'其他',
            u'化验/检验': u'其他',
            u'工艺品/珠宝设计': u'制造业',
            u'德语翻译': u'租赁和商务服务业',
            u'汽车底盘/总装工程师': u'制造业',
            u'测试/可靠性工程师': u'信息传输、软件和信息技术服务业',
            u'渠道/分销专员': u'其他',
            u'财务助理/文员': u'其他',
            u'韩语/朝鲜语翻译': u'租赁和商务服务业',
            u'IT项目总监': u'信息传输、软件和信息技术服务业',
            u'保险项目经理/主管': u'金融业',
            u'公交/地铁乘务': u'交通运输、仓储和邮政业',
            u'品牌主管': u'其他',
            u'外语教师': u'教育',
            u'客户总监': u'其他',
            u'智能大厦/布线/弱电/安防': u'制造业',
            u'楼面管理': u'房地产业',
            u'生产设备管理': u'制造业',
            u'统计员': u'信息传输、软件和信息技术服务业',
            u'网络管理员': u'信息传输、软件和信息技术服务业',
            u'艺术指导/舞美设计': u'文化、体育和娱乐业',
            u'调研员': u'信息传输、软件和信息技术服务业',
            u'需求工程师': u'信息传输、软件和信息技术服务业',
            u'仓库管理员': u'交通运输、仓储和邮政业',
            u'公关总监': u'其他',
            u'公关经理/主管': u'其他',
            u'医药代表': u'卫生和社会工作',
            u'家居用品设计': u'制造业',
            u'文案策划': u'其他',
            u'机械结构工程师': u'制造业',
            u'校对/录入': u'其他',
            u'电子/电器设备工程师': u'制造业',
            u'质量管理/测试工程师': u'信息传输、软件和信息技术服务业',
            u'销售业务跟单': u'其他',
            u'仓库/物料管理员': u'交通运输、仓储和邮政业',
            u'医药招商': u'卫生和社会工作',
            u'客户经理': u'其他',
            u'嵌入式硬件开发': u'信息传输、软件和信息技术服务业',
            u'工厂厂长/副厂长': u'其他',
            u'市场总监': u'其他',
            u'店长/卖场管理': u'其他',
            u'总编/副总编': u'其他',
            u'机电工程师': u'制造业',
            u'核力/火力工程师': u'制造业',
            u'电话销售': u'其他',
            u'船员/水手': u'交通运输、仓储和邮政业',
            u'融资总监': u'金融业',
            u'财务总监': u'其他',
            u'IT质量管理工程师': u'信息传输、软件和信息技术服务业',
            u'SEO/SEM': u'信息传输、软件和信息技术服务业',
            u'不限': u'其他',
            u'临床协调员': u'卫生和社会工作',
            u'仪器/仪表/计量工程师': u'制造业',
            u'促销员': u'其他',
            u'公关经理': u'其他',
            u'兽医': u'农、林、牧、渔业',
            u'副总裁/副总经理': u'其他',
            u'原画师': u'其他',
            u'审计经理/主管': u'其他',
            u'工业工程师': u'制造业',
            u'建筑设计师': u'建筑业',
            u'律师': u'租赁和商务服务业',
            u'手机软件开发工程师': u'信息传输、软件和信息技术服务业',
            u'活动策划': u'其他',
            u'财务分析员': u'其他',
            u'销售行政专员/助理': u'其他',
            u'首席运营官COO': u'其他',
            u'保险业务管理': u'金融业',
            u'化工研发工程师': u'制造业',
            u'区域销售经理/主管': u'其他',
            u'合伙人': u'其他',
            u'咨询经理/主管': u'信息传输、软件和信息技术服务业',
            u'市场经理': u'其他',
            u'理疗师': u'居民服务、修理和其他服务业',
            u'财务经理': u'其他',
            u'项目专员/助理': u'信息传输、软件和信息技术服务业',
            u'储备干部': u'其他',
            u'日语翻译': u'租赁和商务服务业',
            u'汽车项目管理': u'制造业',
            u'电焊工/铆焊工': u'制造业',
            u'系统管理员': u'信息传输、软件和信息技术服务业',
            u'自动化工程师': u'制造业',
            u'认证/体系工程师/审核员': u'其他',
            u'调酒师/茶艺师/咖啡师': u'住宿和餐饮业',
            u'软件工程师': u'信息传输、软件和信息技术服务业',
            u'采购专员/助理': u'交通运输、仓储和邮政业',
            u'销售主管': u'其他',
            u'销售运营专员/助理': u'其他',
            u'个人业务': u'其他',
            u'会务/会展经理': u'其他',
            u'会展策划/设计': u'其他',
            u'保险代理/经纪人/客户经理': u'金融业',
            u'信息技术专员': u'信息传输、软件和信息技术服务业',
            u'列车乘务': u'交通运输、仓储和邮政业',
            u'区域销售总监': u'其他',
            u'客户关系/投诉协调人员': u'其他',
            u'导演/编导': u'文化、体育和娱乐业',
            u'嵌入式软件开发(Linux/单片机/PLC/DSP…)': u'信息传输、软件和信息技术服务业',
            u'广告创意/设计总监': u'其他',
            u'林业技术人员': u'农、林、牧、渔业',
            u'线路结构设计': u'制造业',
            u'药品市场推广经理/主管': u'卫生和社会工作',
            u'证券分析/金融研究': u'金融业',
            u'银行会计/柜员': u'金融业',
            u'银行大堂经理': u'金融业',
            u'银行客户代表': u'金融业',
            u'保险精算师': u'金融业',
            u'保险顾问/财务规划师': u'金融业',
            u'储备经理人': u'其他',
            u'公务员/事业单位人员': u'其他',
            u'发行管理': u'其他',
            u'培训/招生/课程顾问': u'教育',
            u'多媒体/动画设计': u'信息传输、软件和信息技术服务业',
            u'大学教师': u'教育',
            u'排版设计': u'制造业',
            u'物流经理/主管': u'交通运输、仓储和邮政业',
            u'现场应用工程师（FAE）': u'其他',
            u'石油/天然气技术人员': u'采矿业',
            u'职业技术教师': u'教育',
            u'船舶驾驶/操作': u'交通运输、仓储和邮政业',
            u'药品注册': u'卫生和社会工作',
            u'销售培训师/讲师': u'其他',
            u'音效师': u'文化、体育和娱乐业',
            u'WEB前端开发': u'信息传输、软件和信息技术服务业',
            u'临床数据分析员': u'信息传输、软件和信息技术服务业',
            u'互联网产品经理/主管': u'信息传输、软件和信息技术服务业',
            u'产品经理': u'其他',
            u'会计/会计师': u'其他',
            u'保安': u'房地产业',
            u'信托服务': u'金融业',
            u'公关专员/助理': u'其他',
            u'外科医生': u'卫生和社会工作',
            u'报关员': u'其他',
            u'服装/纺织品设计': u'制造业',
            u'系统测试': u'信息传输、软件和信息技术服务业',
            u'给排水/暖通/空调工程': u'制造业',
            u'网络运营专员/助理': u'信息传输、软件和信息技术服务业',
            u'计算机硬件维护工程师': u'信息传输、软件和信息技术服务业',
            u'语音/视频/图形开发': u'信息传输、软件和信息技术服务业',
            u'质量检验员/测试员': u'信息传输、软件和信息技术服务业',
            u'集装箱业务': u'交通运输、仓储和邮政业',
            u'临时': u'其他',
            u'客户服务/续期管理': u'其他',
            u'市场专员/助理': u'其他',
            u'建筑工程安全管理': u'建筑业',
            u'水利/港口工程技术': u'水利、环境和公共设施管理业',
            u'电气设计': u'制造业',
            u'科研管理人员': u'科学研究和技术服务业',
            u'软件测试': u'信息传输、软件和信息技术服务业',
            u'银行卡/电子银行业务推广': u'金融业',
            u'会计助理/文员': u'其他',
            u'体育老师/教练': u'文化、体育和娱乐业',
            u'保险契约管理': u'金融业',
            u'兼职教师': u'教育',
            u'初中教师': u'教育',
            u'前厅接待/礼仪/迎宾': u'其他',
            u'医药销售经理/主管': u'卫生和社会工作',
            u'客户服务主管': u'其他',
            u'广告创意/设计经理/主管': u'其他',
            u'心理医生': u'卫生和社会工作',
            u'快递员/速递员': u'交通运输、仓储和邮政业',
            u'旅游产品销售': u'居民服务、修理和其他服务业',
            u'汽车电工': u'制造业',
            u'渠道/分销经理/主管': u'其他',
            u'电气工程师': u'制造业',
            u'艺术/设计总监': u'文化、体育和娱乐业',
            u'药房管理/药剂师': u'卫生和社会工作',
            u'融资经理/主管': u'金融业',
            u'证券/期货/外汇经纪人': u'金融业',
            u'质量管理/测试主管': u'信息传输、软件和信息技术服务业',
            u'选址拓展/新店开发': u'其他',
            u'列车驾驶/操作': u'交通运输、仓储和邮政业',
            u'市场文案策划': u'其他',
            u'文档/资料管理': u'其他',
            u'环境/健康/安全经理/主管': u'水利、环境和公共设施管理业',
            u'理科教师': u'教育',
            u'社会工作者/社工': u'卫生和社会工作',
            u'空调/热能工程师': u'制造业',
            u'网站推广': u'其他',
            u'财务主管/总帐主管': u'其他',
            u'财务助理': u'其他',
            u'银行客户总监': u'金融业',
            u'高级硬件工程师': u'信息传输、软件和信息技术服务业',
            u'Helpdesk': u'其他',
            u'医疗器械注册': u'制造业',
            u'广告客户主管': u'其他',
            u'房地产中介/交易': u'房地产业',
            u'房地产项目招投标': u'房地产业',
            u'教学/教务管理人员': u'教育',
            u'旅游产品/线路策划': u'居民服务、修理和其他服务业',
            u'模具工程师': u'制造业',
            u'渠道/分销总监': u'其他',
            u'CAD设计/制图': u'制造业',
            u'IT技术/研发总监': u'信息传输、软件和信息技术服务业',
            u'保险内勤': u'金融业',
            u'内科医生': u'卫生和社会工作',
            u'包装工': u'制造业',
            u'大客户销售代表': u'其他',
            u'游戏设计/开发': u'信息传输、软件和信息技术服务业',
            u'物业经理/主管': u'房地产业',
            u'电子技术研发工程师': u'制造业',
            u'网页设计/制作/美工': u'信息传输、软件和信息技术服务业',
            u'美容整形科医生': u'卫生和社会工作',
            u'药品市场推广专员/助理': u'卫生和社会工作',
            u'道路/桥梁/隧道工程技术': u'建筑业',
            u'银行客户经理': u'金融业',
            u'销售管理': u'其他',
            u'人力资源主管': u'其他',
            u'前台接待/总机/接待生': u'其他',
            u'化工工程师': u'制造业',
            u'医学影像/放射科医师': u'卫生和社会工作',
            u'客户服务专员/助理': u'其他',
            u'工程监理/质量管理': u'其他',
            u'工程资料管理': u'建筑业',
            u'律师助理': u'租赁和商务服务业',
            u'旅游计划调度': u'居民服务、修理和其他服务业',
            u'服装/纺织品/皮革质量管理': u'制造业',
            u'汽车装饰美容': u'制造业',
            u'渠道/分销经理': u'其他',
            u'眼科医生/验光师': u'卫生和社会工作',
            u'葡萄牙语翻译': u'租赁和商务服务业',
            u'针灸/推拿': u'居民服务、修理和其他服务业',
            u'ERP技术/开发应用': u'信息传输、软件和信息技术服务业',
            u'互联网产品专员/助理': u'信息传输、软件和信息技术服务业',
            u'健身/美体/舞蹈教练': u'居民服务、修理和其他服务业',
            u'员工关系/企业文化/工会': u'文化、体育和娱乐业',
            u'售前/售后技术支持管理': u'其他',
            u'土木/土建/结构工程师': u'建筑业',
            u'岩土工程': u'建筑业',
            u'工程造价/预结算': u'建筑业',
            u'志愿者/义工': u'其他',
            u'放映管理': u'文化、体育和娱乐业',
            u'机械制图员': u'制造业',
            u'汽车电子工程师': u'制造业',
            u'物业顾问': u'租赁和商务服务业',
            u'行政专员/助理': u'其他',
            u'裁剪工': u'制造业',
            u'资金专员': u'金融业',
            u'促销主管/督导': u'其他',
            u'保险培训师': u'金融业',
            u'医药学术推广': u'卫生和社会工作',
            u'发动机/总装工程师': u'制造业',
            u'城市规划与设计': u'制造业',
            u'审计专员/助理': u'其他',
            u'幼教': u'教育',
            u'救生员': u'其他',
            u'水运/空运/陆运操作': u'交通运输、仓储和邮政业',
            u'法务经理/主管': u'租赁和商务服务业',
            u'注塑工程师': u'制造业',
            u'玩具设计': u'制造业',
            u'经纪人/星探': u'其他',
            u'美容师/美甲师': u'居民服务、修理和其他服务业',
            u'证券总监/部门经理': u'金融业',
            u'资产/资金管理': u'金融业',
            u'通信技术工程师': u'信息传输、软件和信息技术服务业',
            u'银行客户服务': u'其他',
            u'区域销售专员/助理': u'其他',
            u'咨询顾问/咨询员': u'信息传输、软件和信息技术服务业',
            u'培训策划': u'教育',
            u'奢侈品销售': u'其他',
            u'媒介经理/主管': u'其他',
            u'家具设计': u'制造业',
            u'市场助理': u'其他',
            u'市场营销主管': u'其他',
            u'房地产销售经理': u'房地产业',
            u'摄影师/摄像师': u'其他',
            u'海关事务管理': u'交通运输、仓储和邮政业',
            u'物流/仓储项目管理': u'交通运输、仓储和邮政业',
            u'环保技术工程师': u'电力、热力、燃气及水生产和供应业',
            u'环境/健康/安全工程师': u'水利、环境和公共设施管理业',
            u'电工': u'制造业',
            u'系统分析员': u'信息传输、软件和信息技术服务业',
            u'西班牙语翻译': u'租赁和商务服务业',
            u'销售代表': u'其他',
            u'仓库经理/主管': u'交通运输、仓储和邮政业',
            u'企业培训师/讲师': u'教育',
            u'会务经理/主管': u'其他',
            u'化学技术应用': u'制造业',
            u'印刷排版/制版': u'文化、体育和娱乐业',
            u'建筑工程测绘/测量': u'建筑业',
            u'建筑施工现场管理': u'建筑业',
            u'游戏策划': u'信息传输、软件和信息技术服务业',
            u'理货员': u'交通运输、仓储和邮政业',
            u'行政经理/主管/办公室主任': u'其他',
            u'证券/投资项目管理': u'金融业',
            u'调度员': u'其他',
            u'麻醉医生': u'卫生和社会工作',
            u'买手': u'其他',
            u'品牌经理': u'其他',
            u'导游/票务': u'居民服务、修理和其他服务业',
            u'广告/会展项目管理': u'其他',
            u'房地产项目管理': u'房地产业',
            u'汽车质量管理/检验检测': u'其他',
            u'用户体验（UE/UX）设计': u'信息传输、软件和信息技术服务业',
            u'硬件测试': u'信息传输、软件和信息技术服务业',
            u'FAE 现场应用工程师': u'其他',
            u'医药项目招投标管理': u'卫生和社会工作',
            u'医药项目管理': u'卫生和社会工作',
            u'大客户销售经理': u'其他',
            u'市场策划/企划经理/主管': u'其他',
            u'技术文档工程师': u'其他',
            u'施工员': u'建筑业',
            u'机械工程师': u'制造业',
            u'汽车钣金': u'制造业',
            u'物流专员/助理': u'交通运输、仓储和邮政业',
            u'生产经理/车间主任': u'制造业',
            u'生产项目工程师': u'制造业',
            u'生态治理/规划': u'水利、环境和公共设施管理业',
            u'综合业务专员/助理': u'其他',
            u'视觉设计': u'信息传输、软件和信息技术服务业',
            u'风险管理/控制/稽查': u'金融业',
            u'仪器/仪表/计量分析师': u'制造业',
            u'企业律师/合规顾问': u'租赁和商务服务业',
            u'其他语种翻译': u'租赁和商务服务业',
            u'客户咨询热线/呼叫中心人员': u'信息传输、软件和信息技术服务业',
            u'市场营销专员/助理': u'其他',
            u'房地产项目策划经理/主管': u'房地产业',
            u'招聘经理/主管': u'其他',
            u'普工/操作工': u'制造业',
            u'汽车定损/车险理赔': u'其他',
            u'清算人员': u'其他',
            u'激光/光电子技术': u'制造业',
            u'版图设计工程师': u'制造业',
            u'空调工/电梯工/锅炉工': u'制造业',
            u'订单处理员': u'其他',
            u'临床研究员': u'科学研究和技术服务业',
            u'主持人/司仪': u'其他',
            u'医疗器械销售': u'制造业',
            u'咨询总监': u'信息传输、软件和信息技术服务业',
            u'咨询项目管理': u'信息传输、软件和信息技术服务业',
            u'培训经理/主管': u'教育',
            u'学术推广': u'科学研究和技术服务业',
            u'教育产品开发': u'教育',
            u'电池/电源开发': u'制造业',
            u'签证业务办理': u'居民服务、修理和其他服务业',
            u'财务顾问': u'租赁和商务服务业',
            u'销售总监': u'其他',
            u'信贷管理/资信评估/分析': u'金融业',
            u'室内装潢设计': u'建筑业',
            u'电信网络工程师': u'信息传输、软件和信息技术服务业',
            u'知识产权/专利顾问/代理人': u'租赁和商务服务业',
            u'税务经理/主管': u'租赁和商务服务业',
            u'融资专员/助理': u'金融业',
            u'财务分析经理/主管': u'其他',
            u'Flash设计/开发': u'信息传输、软件和信息技术服务业',
            u'人力资源专员/助理': u'其他',
            u'信审核查': u'其他',
            u'厨师/面点师': u'住宿和餐饮业',
            u'媒介专员/助理': u'其他',
            u'广告/会展业务拓展': u'其他',
            u'广告客户代表': u'其他',
            u'广告文案策划': u'其他',
            u'房地产项目配套工程师': u'房地产业',
            u'汽车零部件设计师': u'制造业',
            u'物流主管': u'交通运输、仓储和邮政业',
            u'猎头顾问/助理': u'租赁和商务服务业',
            u'电子元器件工程师': u'制造业',
            u'销售经理': u'其他',
            u'面料辅料开发/采购': u'交通运输、仓储和邮政业',
            u'高级建筑工程师/总工': u'建筑业',
            u'IT技术支持/维护工程师': u'信息传输、软件和信息技术服务业',
            u'二手车评估师': u'批发和零售业',
            u'会务专员/助理': u'其他',
            u'供应链管理': u'其他',
            u'信息技术标准化工程师': u'信息传输、软件和信息技术服务业',
            u'动物育种/养殖': u'农、林、牧、渔业',
            u'安全消防': u'其他',
            u'广告创意/设计师': u'其他',
            u'广告客户经理': u'其他',
            u'护士/护理人员': u'卫生和社会工作',
            u'服装/纺织设计总监': u'制造业',
            u'机械维修/保养': u'制造业',
            u'电子/电器工艺/制程工程师': u'制造业',
            u'电子/电器项目管理': u'制造业',
            u'英语翻译': u'租赁和商务服务业',
            u'酒店管理': u'住宿和餐饮业',
            u'俄语翻译': u'租赁和商务服务业',
            u'化学制剂研发': u'制造业',
            u'政府事务管理': u'其他',
            u'汽车维修/保养': u'制造业',
            u'电话采编': u'其他',
            u'绘画': u'其他',
            u'综合门诊/全科医生': u'卫生和社会工作',
            u'网络运营管理': u'信息传输、软件和信息技术服务业',
            u'美术编辑/美术设计': u'文化、体育和娱乐业',
            u'股票/期货操盘手': u'金融业',
            u'设计管理人员': u'其他',
            u'飞机驾驶/操作': u'交通运输、仓储和邮政业',
            u'储备干部/培训生/实习生': u'其他',
            u'其他': u'其他',
            u'加油站工作员': u'其他',
            u'半导体技术': u'制造业',
            u'团购业务员': u'其他',
            u'安全管理': u'其他',
            u'安检员': u'其他',
            u'客户服务总监': u'其他',
            u'射频工程师': u'制造业',
            u'市场策划/企划专员/助理': u'其他',
            u'施工队长': u'建筑业',
            u'无线电工程师': u'制造业',
            u'油漆/化工涂料研发': u'制造业',
            u'物业租赁/销售': u'房地产业',
            u'生产计划': u'制造业',
            u'药品生产/质量管理': u'其他',
            u'薪酬福利专员/助理': u'其他',
            u'裁床': u'制造业',
            u'证券/投资客户主管': u'金融业',
            u'部门/事业部管理': u'其他',
            u'高级软件工程师': u'信息传输、软件和信息技术服务业'

        }

        self.all_city = {}
        cunrrent_path = os.path.dirname(os.path.abspath(__file__))
        father_path = os.path.dirname(cunrrent_path)
        father_father_path = os.path.dirname(father_path)
        filepath = father_father_path + os.sep + 'res' + os.sep + 'hangye_salary.txt'

        file1 = codecs.open(filepath, 'r', encoding='utf-8')
        line1 = file1.readline().strip()
        hangyes = line1.split('\t')[1:]
        for line in file1:
            linelist = line.strip().split('\t')
            city = linelist[0]
            salarys = linelist[1:]
            lenhangye = len(hangyes)
            lensalarys = len(salarys)
            mp = {}
            for i in range(lenhangye):
                if i < lensalarys:
                    mp[hangyes[i]] = salarys[i]
                else:
                    mp[hangyes[i]] = ''

            # mp = map(mydict, hangyes, salarys)
            # oneaddr={city:mp}
            self.all_city[city] = mp
        # 这里把缺失的平均值都事先计算好
        self.averages = {}
        all_sheng = self.all_city.keys()
        self.all_hangyes = all_hangye = self.all_city[u'北京'].keys()  # 这里随便取一个地区的所有行业
        for hangye in all_hangye:
            sums = 0
            count = 0
            average = ''
            for sheng in all_sheng:
                salary = self.all_city[sheng][hangye]
                if salary:
                    sums += int(salary)
                    count += 1
            if count:  # 不全为空，以防某个行业全没数据
                average = sums // count
            self.averages[hangye] = average  # 记录下每个行业的平均值
            for sheng in all_sheng:
                if not self.all_city[sheng][hangye]:
                    self.all_city[sheng][hangye] = average
                    # 每个行业的平均值填好了。

    #####################################################################

    def check_bbd_industry(self, indexstr, ustr):
        """bbd行业划分"""
        ret = None
        job_functions = indexstr['job_functions']
        job_title = indexstr['job_title']
        hangyelist = []
        if job_functions and len(job_functions.strip()):
            funclist = job_functions.split(u';')
            for i in funclist:
                for key in self.industry_hangye.keys():
                    if i in key:  # .split(u'/')
                        hangyelist.append(self.industry_hangye[key])
        elif job_title and len(job_title.strip()):
            funclist = job_title.split(';')
            for i in funclist:
                for key in self.industry_hangye.keys():
                    if i == key:  # .split(u'/')
                        hangyelist.append(self.industry_hangye[key])
        hangyelist = list(set(hangyelist))  # 去重
        if not hangyelist:
            hangyelist = [u'其他']
        ustrlist = ustr.split(';')

        if set(hangyelist) != (set(ustrlist)):
            ret = u'不正常,我的是 --%s--' % (';'.join(hangyelist))
        return ret

    def check_bbd_recruit_num(self, indexstr, ustr):
        """bbd招聘人数"""
        ret = None
        recruit_numbers = indexstr['recruit_numbers']
        if recruit_numbers and len(recruit_numbers):
            if re.compile(u'^\d+$').match(recruit_numbers):
                if ustr != recruit_numbers:
                    ret = u'纯数字直接赋值'
            elif re.compile(u'^\d{1,}.?人$').match(recruit_numbers):
                sub = re.compile(u'[^\d]').sub('', recruit_numbers)
                if ustr != sub:
                    ret = u'xx 人取值'
            elif re.compile(u'^\d{1,}-\d{1,}.?人$').match(recruit_numbers):
                max = recruit_numbers.split(u'-')[1]
                sub = re.compile(u'[^\d]').sub('', max)
                if ustr != sub:
                    ret = u'xx-xx 人取大值'
            elif recruit_numbers in (u'若干', u'人数不限', u''):
                if ustr != u'10':
                    ret = u'原始数据为若干或者不限的，未填充10'
        return ret

    def check_bbd_salary(self, indexstr, ustr):
        """bbd职位薪资"""
        ret = None
        salary = indexstr[u'salary']
        match = re.compile(u'^(\d+)-(\d+)$').match(salary)
        salaryslist = []
        if match:
            # groups = re.compile(u'(\d{1,})-(\d{1,})').match(salary)
            tmp = int(match.group(1)) + int(match.group(2))
            tmp /= 2
            if ustr != unicode(tmp):
                ret = u'没有是平均值呢'
        elif salary in (u'面议', u'空', u'未提供', None, u''):
            bbd_industry = indexstr[u'bbd_industry']
            location = indexstr[u'location'].split('-')[0]
            location = location.split(';')[0]#######################只有一个地区
            bbd_industrys = bbd_industry.split(u';')
            locations = location.split(u';')

            for location in locations:
                for bbd_industry in bbd_industrys:
                    lc = self.all_city.get(location, {})
                    ind = lc.has_key(bbd_industry)
                    if ind:  # 正常的地址和行业
                        salary = lc.get(bbd_industry, '')
                        if salary:  # 行业都匹配上了，均值一定在
                            salaryslist.append(salary)
                        else:
                            ret = u'两个都能匹配到的怎么没有均值呢' + location + bbd_industry
                            return ret  # 直接返回
                    elif lc and not ind:  # 找到了地区没找到行业，不处理
                        pass
                    elif not lc and bbd_industry in self.all_hangyes:  # 没有地区，有行业，填均值
                        salaryslist.append(self.averages[bbd_industry])
            # data = ustr.split(';')
            mydata = u';'.join([unicode(x) for x in salaryslist])
            if ustr != mydata:
                ret = u'我的解析和君哥的不一样我的解析是%s' % (mydata)
        return ret

    def check_pubdate_doublet(self, indexstr, ustr):
        """发布时间(排重)"""
        ret = None
        pubdate = indexstr[u'pubdate']
        bbd_dotime = indexstr[u'bbd_dotime']  # 2015年3月
        if pubdate and len(pubdate.strip()):
            tmp = pubdate[0:8]
            if ustr != tmp:
                ret = u'没有跟pubdate年月相同%s' % tmp
        else:
            tmp = bbd_dotime[0:8]
            if ustr != tmp:
                ret = u'没有跟bbd_dotime年月相同%s' % tmp
        if not re.compile(u'^\d{4}年\d{2}月$').match(ustr):
            ret = u'没有满足年月格式'
        return ret


#####################################################################


if __name__ == '__main__':
    #
    import json

    a = {"bbd_xgxx_id": "", "underling_numbers": "", "bbd_version": "2.0", "company_nature": "", "bbd_qyxx_branch": "[]", "service_year": "1-3年",
         "bbd_table": "recruit", "bbd_dotime": "2015年09月12日", "reportto": "", "bbd_source": "", "jobfair_location": "", "postcode": "", "bbd_industry": "其他",
         "bbd_salary": "7649", "majors_required": "", "bbd_params": "", "language_required": "", "responserate": "", "jobfair_time": "", "bbd_html": "",
         "validdate": "",
         "job_descriptions": "Job;Scope:;·;Install,;modify,;maintain,;and;upgrade;complex;equipment;in;accordance;with;maintenance;and;service;agreements;and;technical;specifications.;·;Perform;periodic;and;preventive;and;corrective;maintenance;on;customer;installations;to;ensure;that;equipment;continuous;to;perform;reliably.;·;Plan/assign/manage;field;labour;hours;to;maximize;profitability;and;productivity;without;compromising;safety;or;quality.;·;Coach;and;mentor;less;experienced;technicians,;check;the;quality;of;their;work,;and;help;them;diagnose;and;solve;problems.;·;Take;as;leader;in;safety;work;practices;on;site.;·;Maintain;accurate;service;records,;provide;documents;and;reports;for;monthly;safety;meetings.;·;Ensure;24hr;response;is;available;and;negotiate;other;agreeable;actions;with;customers.;·;Maintain;the;customer;relationship;and;collect;business;information.;·;Other;duties;assigned;by;supervisor/manager.;Requirement:;·;College;or;above,;mechanic;or;electric;background.;·;Above;3;years;industrial;maintenance;working;experience.;·;Good;communication;skills.;·;Excellent;documents;handle;skill.;·;Good;English;skills;is;preferred.;·;Team;work;spirit,;responsible;and;able;to;work;under;pressure.;工作职责：;·;根据维保服务协议和技术规范对设备进行安装、维修保养及升级；;·;执行定期的、预防性的客户设备维修保养，确保设备运行良好；;·;确保24小时响应，与客户协商其他相关工作活动；;·;处理好客户关系，收集与起重机相关业务信息；;·;执行公司要求的安全规则，服从现场管理；;·;主管安排的其他工作。;要求：;·;大专毕业，主修电气或机械专业；;·;两年以上设备安装和维护经验，有起重机安装和维护保养经验优先；;·;熟悉电气原理和线路，有一定的变频器和PLC基础；;·;有电工证和特种设备操作许可证的优先。;·;团队精神，动手能力强。;工作地址：;海南;洋浦经济开发区;查看职位地图",
         "recruit_numbers": "2", "contact_information": "", "source": "zhilian", "bbd_customer_name": "bbd_dp_parse_user", "company_name": "科尼起重机设备（上海）有限公司",
         "bbd_type": "recruit", "department": "", "job_title": "Service Engineer;Technician服务工程师;技师", "bbd_xgxx_date": "2015年09月01日", "page_content": "",
         "bbd_qyxx_company": "[\"科尼起重机设备（上海）有限公司\"]", "delivery_time": "", "bbd_uptime": "1.547406844E9", "website_address": "", "pubdate_doublet": "2015年09月",
         "bbd_recruit_num": "2", "pubdate": "2015年09月01日", "md5": "cbf88699555a158de6224ce14795d4b0", "salary": "面议", "view_rate": "",
         "job_functions": "售前;售后技术支持工程师", "benefits": "五险一金;年底双薪;绩效奖金;加班补助;带薪年假;补充医疗保险;定期体检;高温补贴", "job_nature": "全职", "company_introduction": "",
         "agerequired": "", "industry": "", "e_mail": "", "bbd_seed": "", "location": "洋浦市;洋浦经济开发区", "enscale": "", "salary_system": "",
         "education_required": "大专", "sex_required": "", "_id": "http://jobs.zhaopin.com/000548212252000.htm?ssidkey=y&ss=201&ff=03|_|2015-09-12",
         "bbd_url": "http://jobs.zhaopin.com/000548212252000.htm?ssidkey=y&ss=201&ff=03"}
    rt = recruit()
    print rt.check_bbd_industry(a, u'制造业')
    print rt.check_bbd_salary(a, "xxx")
    pass
