#!/usr/bin/python
#coding=utf8
import json
import urllib 
import urllib2
import os 


#host file: ./host. data fiel:./data_send
def post_data_from_file():
    fp=open('./host','r')
    host_content=fp.read()
    fp.close()
    content=eval(host_content)

    #make url
    ip=content['ip']
    port=content['port']
    path=content['path']
    url="http://"+ip+":"+port+path

    #read data info from file
    data="{'data':{'uid':'100001','token':'abcd1992ttft','status':'1','create_time':'2016-11-1418:20:10','user_info':{'source_id':'245678','product_type':'宜农贷','market_channel_lev1':'400客服','market_channel_lev2':'微信','market_channel_lev3':'微信农商贷','sale_depart':'上海营业部咨询团队','sale_manager_empid':'110220161101','sale_empid':'110220161101','name':'刘备','phone':'18512132095','email':'zhangfei@126.com','qq':'33522155','gender':'男','birth_date':'1992-5-16','identity_number':'130255199205165207','education':'博士','marital_status':'未婚','registered_addr':'浙江省新民市张家湾','living_addr':'北京市海淀区','city':'北京市','salary':'10000','company_type':'国企','company_name':'三国杀桌游有限公司','company_addr':'北京市海淀区','company_tele':'010-52689077','career_length':'36','working_department':'it事业部','job_title':'市场开拓总经理','yrd_discard_reason':'征信报告未通过','credit_card_line':'10000','quantity':'10','usage':'买房','loan_desc':'用来缴纳税','loan_due_time':'60','max_repayment':'20','has_car':'1','car_city':'北京市','car_buy_time':'2006-10-01','car_price':'20','has_estate':'0','has_estate_loan':'0','ext1':'test_value','ext2':'test_value','ip':'10.110.151.11','utm_source':'test_value','utm_campaign':'test_value','utm_media':'test_value','utm_content':'test_value','utm_keyword':'test_value','utm_term':'test_value','os':'mac','career_type':'employee','career_type_other':'test_value','business_license':'0','business_proof':'0','stock_over20':'0','bank_statement':'1','house_fund':'1','social_insurance':'1','job_contract':'1','salary_pay_type':'bycard','salary_by_card':'5000~10000','salary_by_cash':'0~3000','ecommerce_op':'0','ecommerce_platform':'taobao','operation_length':'test_value','lenders':'中国银行','is_estate_entire_pay':'2','is_estate_paid_off':'2','address_proof':'0','car_drive_miles':'100','career_start_date':'2006-10-01','car_model':'baoma001','car_province':'河北省','creator_id':'123456','credit_card_expire_status':'0','discard_reason_other':'reson1','ecommerce_type':'0','ecommert_type':'0','estate_province':'河北省','estate_built_date':'2006-10-01','estate_buy_date':'2006-10-01','estate_buy_price':'100','estate_city':'石家庄','estate_valuation':'100','feature':'feature','first_contact_type':'0','has_creditcard':'0','has_workplace_estate':'0','paid_moreThan_half':'0','is_car_entirePay':'0','is_car_mortgage_payOff':'0','is_loan_from_us':'0','is_nine_seats':'0','is_reLoan':'0','job_proof':'0','level':'1','loan_expire_status':'0','origin':'origin','origin_extrainfo':'0','ori_product_typeId':'111','other_ecommerce_Platform':'jd','other_lenders':'001','other_market_channel':'车贷','product_typeId':'002','row_data_id':'10','use_date':'2007-10-01','source_type_id':'1111','car_number':'88888888','market_channel_id':'111','province':'河北省'}}}"
   
    cmd = "curl -d "+ '''"'''+"data="+data +'''" "'''+url+'''"'''
    print cmd
    os.system(cmd)

if __name__=="__main__":
    post_data_from_file()
