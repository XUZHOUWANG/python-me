import uuid,random,time,json,string
from datetime import datetime
print("------------- _______________")
f = open("tmp.txt",'w')
u=str(uuid.uuid4()).replace("-","")
for line in open("company.txt"):
    r =str(random.randint(100000,1000000))
    s = " INSERT INTO `member_apply_load` (`create_time`, `company_id`, `num`, `status`, `uid`, `business_id`, `update_time`, `expired`, `operate`)" + " VALUES " + " ('2018-11-22 14:03:49', "+line +", 5, 0, '"+ u +"','yy201811228314545636437" +r +"', NULL, 0, 'SUPER_ADMIN');"
    print(s)
    f.write(s)
f.close()





