# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import re
from common import public


class tddkgs():
    """土地市场-地块公示"""
    need_check_ziduan = [
        u'company_name'
    ]

    def check_company_name(self, indexstr, ustr):
        ret = None
        needparse = [u'受让单位',
                     u'受让人',
                     u'竞得人：',
                     u'用地单位：',
                     u'竞得者为',
                     u'使用人：',
                     u'土地使用者：',
                     u'拟受让人：',
                     u'申请人：',
                     u'竞得人/受让人',
                     u'受让人：',
                     u'竞得单位']

        main = indexstr['main']  # 公司概况
        company_list = []
        try:
            for test in needparse:
                startpos = 0
                while True:
                    b = re.compile(u'[ ;；。:：、\t\n\r]{1,}' + test + u'[ ;；。:：、\t\n\r]{0,}').search(main, pos=startpos)
                    if b:
                        index = b.span()[1]
                        c = re.compile(u'[ \n\r\t;；。:：]{1,}').search(main, pos=index)
                        if c:
                            endindex = c.span()[1]
                        else:
                            break
                        # endindex = main.index(' ', index)
                        company = main[index:endindex]
                        company = company.strip().strip(u';；。：:、')
                        company = company.replace('(', u'（').replace(')', u'）').replace('，', ',')
                        company_list.append(company)
                        startpos = endindex
                    else:
                        break

        except Exception as e:
            ret = u'获取公司名称出错main:' + main
        company_list = list(set(company_list))

        if ustr == '':
            if company_list:
                ret = u"不相等我的是:-%s-" % (';'.join(company_list))
        elif set(ustr.split(';')) != set(company_list):
            ret = u"不相等我的是:-%s-" % (';'.join(company_list))
        return ret


if __name__ == '__main__':
    td = tddkgs()
    a = {"bbd_xgxx_id": "", "bbd_version": "1.0", "retain2": "", "retain1": "", "bbd_table": "tddkgs", "bbd_dotime": "2016年04月02日", "bbd_source": "",
         "bbd_params": "", "uuid": "58026a76-f862-11e5-8fc9-0cc47a7ce9ea", "district": "靖西县", "title": "靖西县国土资源局国有建设用地使用权挂牌出让结果公告", "bbd_html": "",
         "bbd_customer_name": "bbd_dp_parse_user", "company_name": "广西润宇工贸集团有限公司", "bbd_type": "tddkgs",
         "main": u"靖西县国土资源局国有建设用地使用权挂牌出让结果公告\n\n\n  发布时间：2009年9月17日 16:01  \r\n\t\t\t\t\t\t\t\t\t\t行政区：广西壮族 > 百色市 > 靖西县\n\n\n\n\n\n\n\n\n\n\n\n \n \n靖西县国土资源局国有建设用地使用权挂牌出让\n \n结果公告\n \n经靖西县人民政府批准，靖西县国土资源局于2009年9月3日采用挂牌方式出让一宗国有建设用地使用权，现将结果公告如下：\n1、宗地位置：广西靖西县龙邦镇护龙村；\n2、土地面积：10.6906公顷；\n3、土地用途：工业用地；\n4、土地使用年限：50年；\n5、投资强度：440万元/公顷\n6、成交价：666万元\n7、受让人：广西润宇工贸集团有限公司。\n \n \n                                               靖西县国土资源局\n                                               二〇〇九年九月十一日",
         "bbd_qyxx_branch": "[]", "bbd_uptime": "1.143726844E9", "data_source": "土地使用", "key": "", "date": "2009年09月17日",
         "md5": "7d41d870a6de56d76b5d4956473e2203", "bbd_qyxx_company": "[\"广西润宇工贸集团有限公司\"]",
         "main_source_code": "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"contentItem\" height=\"100%\" id=\"Table2\" width=\"100%\">\n<tr height=\"30\">\n<td></td>\n</tr>\n<tr>\n<td align=\"center\" class=\"ContentTitle3\" height=\"30\"><span id=\"lblTitle\">靖西县国土资源局国有建设用地使用权挂牌出让结果公告</span></td>\n</tr>\n<tr height=\"30\">\n<td align=\"center\"><font face=\"宋体\">  </font><span id=\"lblCreateDate\">发布时间：2009年9月17日 16:01</span><font face=\"宋体\">  \r\n\t\t\t\t\t\t\t\t\t\t<span id=\"lblXzq\">行政区：广西壮族 &gt; 百色市 &gt; 靖西县</span></font></td>\n</tr>\n<tr>\n<td class=\"TileUnderLine1\"></td>\n</tr>\n<tr>\n<td height=\"30\"></td>\n</tr>\n<tr>\n<td align=\"center\" valign=\"top\">\n<table border=\"0\" cellpadding=\"2\" cellspacing=\"0\" width=\"90%\">\n<tr height=\"400\">\n<td id=\"tdContent\" valign=\"top\"><p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt\"><span lang=\"EN-US\" style=\"FONT-SIZE: 15pt; FONT-FAMILY: 宋体\"><o:p> </o:p></span></p>\n<p align=\"center\" class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"></span> </p>\n<p align=\"center\" class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"><font size=\"5\">靖西县国土资源局国有建设用地使用权挂牌出让</font></span></p>\n<p align=\"center\" class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"><font size=\"5\"></font></span> </p>\n<p align=\"center\" class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"><font size=\"5\">结果公告</font></span></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span lang=\"EN-US\"><o:p><font size=\"4\"> </font></o:p></span></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">经靖西县人民政府批准，靖西县国土资源局于</span><span lang=\"EN-US\">2009</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">年</span><span lang=\"EN-US\">9</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">月</span><span lang=\"EN-US\">3</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">日采用挂牌方式出让一宗国有建设用地使用权，现将结果公告如下：</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">1</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、宗地位置：广西靖西县龙邦镇护龙村；</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">2</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、土地面积：</span><span lang=\"EN-US\">10.6906</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">公顷；</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">3</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、土地用途：工业用地；</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">4</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、土地使用年限：</span><span lang=\"EN-US\">50</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">年；</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">5</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、投资强度：</span><span lang=\"EN-US\">440</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">万元</span><span lang=\"EN-US\">/</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">公顷</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">6</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、成交价：</span><span lang=\"EN-US\">666</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">万元</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><font size=\"4\"><span lang=\"EN-US\">7</span><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\">、受让人：广西润宇工贸集团有限公司。</span></font></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span lang=\"EN-US\"><o:p><font size=\"4\"> </font></o:p></span></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span lang=\"EN-US\"><o:p><font size=\"4\"> </font></o:p></span></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"><font size=\"4\">                                               靖西县国土资源局</font></span></p>\n<p class=\"MsoNormal\" style=\"MARGIN: 0cm 0cm 0pt; TEXT-INDENT: 21pt; mso-char-indent-count: 2.0\"><span style=\"FONT-FAMILY: 宋体; mso-ascii-font-family: 'Times New Roman'; mso-hansi-font-family: 'Times New Roman'\"><font size=\"4\">                                               二〇〇九年九月十一日</font></span></p></td>\n</tr>\n</table>\n</td>\n</tr>\n<tr>\n<td align=\"right\" class=\"gridHeader\" height=\"20\">\n<a class=\"link1\" id=\"lnkOldBul\"></a></td>\n</tr>\n<tr>\n<td align=\"center\" class=\"gridHeader\"><input class=\"HeadToolButton\" id=\"btnPrint\" language=\"javascript\" name=\"btnPrint\" onclick=\"return btnPrint_onclick()\" style=\"HEIGHT: 24px\" type=\"button\" value=\"打印\"/><input class=\"HeadToolButton\" id=\"btnClose\" language=\"javascript\" name=\"btnClose\" onclick=\"return btnClose_onclick()\" style=\"HEIGHT: 24px\" type=\"button\" value=\"关闭窗口\"/></td>\n</tr>\n<tr>\n<td class=\"gridHeader\" height=\"20\"></td>\n</tr>\n</table>",
         "url": "", "bbd_xgxx_date": "2009年09月17日", "bbd_seed": "", "rawdata": "",
         "_id": "http://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=4a611fc4-42b1-4231-ac26-8d25b002dc2b&recorderguid=b92e7c8a-690f-4391-a641-df3141b1d667&sitePath=,2009-09-17|_|土地使用",
         "bbd_url": "http://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=4a611fc4-42b1-4231-ac26-8d25b002dc2b&recorderguid=b92e7c8a-690f-4391-a641-df3141b1d667&sitePath="}
    b = td.check_company_name(a, u'广西润宇工贸集团有限公司')
    print b
