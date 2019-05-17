#coding=utf-8
import httplib
import json
param = {
'content':'亲爱的商家，即日起“青团社招聘版”app正式更名为“青团兼职商户版”，同时为提升招聘效果进行了功能大升级~为感谢一路支持，额外赠送您5个报名单，邀请好友入驻还有更多奖励，点此查收：e.qtshe.com',
'templateId':10000
}
headerdata = {"Content-type": "application/json"}
url="http://api.qtshe.com/smsCenter/cloudService/sms/send"
for line in open("phone.txt"):
    param['mobile']=line
    conn = httplib.HTTPConnection("10.1.24.88",8090)
    print(param)

  
