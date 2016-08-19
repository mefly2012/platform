# -*- coding: utf-8 -*-



import codecs

all_tables = {
    'ktgg': ['main'],
    'zgcpwsw': ['title', 'casecode'],
    #
    # # 'ktgg',
    # # 'cdfy_sfgk',
    # # 'newktgg',
    # # 'zyktgg',
    # # 'zgcpwsw',
    # # 'itslaw',
    # # 'qyxg_zgcpwsw',
    # # 'qyxg_wscpws',
    #
    'zhixing': ['pname', 'case_code'],
    'dishonesty': ['pname', 'case_code', 'exe_code'],
    'recruit': ['pubdate_doublet', 'company_name', 'job_functions', 'source'],
    'xgxx_shangbiao': ['applicant_name', 'application_no'],
    'shgy_zhaobjg': ['title'],
    'shgy_zhongbjg': ['title'],
    'rmfygg': ['notice_content', 'notice_time', 'notice_type'],
    'overseas_investment': ['certificate_no'],
    'qyxx_wanfang_zhuanli': ['application_code'],
    'tddy': ['landno', 'land_location', 'mortgage_right_name'],
    'tdzr': ['land_location', 'landno', 'original_usename'],
    'dcos': ['company_name', 'certificate_num'],
    'qyxx_enterpriseQualificationForeign': ['company_name', 'certificate_no', 'issue_date'],
    'qyxx_gcjljz': ['company_name', 'certificate_no'],
    'qyxx_jzsgxkz': ['company_name', 'certificate_no'],
    'qyxx_miit_jlzzdwmd': ['company_name', 'certificate_no'],
    'qyxx_food_prod_cert': ['company_name', 'certificate_no'],
    'qyxx_haiguanzongshu': ['company_name', 'customs_code'],
    'qyxx_gmpauth_prod_cert': ['company_name', 'certificate_no'],
    'qyxx_hzp_pro_prod_cert': ['company_name', 'certificate_no'],
    'qyxx_medi_jy_prod_cert': ['company_name', 'certificate_no'],
    'qyxx_medi_pro_prod_cert': ['company_name', 'certificate_no'],
    'qyxx_industrial_production_permit': ['company_name', 'certificate_no'],
    'qyxx_nyscqyzzcx': ['company_name', 'validdate'],
    'qyxx_tk': ['company_name', 'certificate_no'],
    'qyxx_ck': ['company_name', 'certificate_no'],
    'xzcf': ['name', 'public_date', 'punish_code'],
    'rjzzq': ['copyright_nationality', 'regnum', 'regdate'],
    'qyxx_finance_xkz': ['company_name', 'issue_date', 'id_serial_num'],
    'qylogo': ['company_full_name'],
    'ssgs_zjzx': ['_id'],
    'simutong': ['financing_side', 'invest_side', 'invest_time'],
    'tddkgs': ['title', 'main'],
    'shgy_tdcr': ['project_name', 'project_location', 'electron_supervise'],
    'qyxx_zhuanli': ['application_code', 'reg_effect_date'],
    'zhuanli_zhuanyi': ['application_code', 'reg_effect_date'],
    'zpzzq': ['copyright_owner', 'regnum'],
    'zuzhijigoudm': ['jgdm', 'jgmc'],

    # 'sfpm_taobao':['title','auctioneer','disposal_unit'],
    # 'domain_name_website_info':['organizer_name','site_certificate_no','domain_name']
}

tablename='SIMUTONG'

if __name__ == '__main__':
    # fok = codecs.open(tablename+'_mysql', 'r', encoding='utf-8')
    # fdup = codecs.open(tablename+'_dup', 'r', encoding='utf-8')
    #
    # foks=fok.read()
    # for i in fdup.readlines():
    #     if i.strip() not in foks:
    #         print i
    #         break
    #
    # fdup.seek(0)
    # all_list=[]
    #
    # for i in fdup.readlines():
    #     all_list.append(i.strip())
    # print len(all_list)
    # print len(set(all_list))

    a=1
    b=0
    try:
        a/b
    except Exception as e:
        print str(e)

