#定义方法
# def checkname(user,password):
#     if user[0] in "qwertyuiopasdfghjklzxcvbnm" and 5<=len(user)<=8:
#         if 6<=len(password)<=12:
#                 print({user:password})
#         else:
#             print("密码长度在6-12之间")
#     else:
#         print("账号必须以小写字母开头且长度在5-8之间")
# checkname("k12345",str(123456))

import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
cur = db.cursor()
cur.execute("select * from t_class;")
res = cur.fetchall()
print(res)