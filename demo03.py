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

# import pymysql

# db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
# cur = db.cursor()
# cur.execute("select * from t_class;")
# res = cur.fetchall()
# print(res)


class  girlfriend():    #类的首字母必须大写
    def __init__(self):
        self.sex = "性别:女"
        self.high = "身高:170cm"
        self.weight = "体重:55kg"
        self.hair = "发型:大波浪"
        self.age = "年龄:18岁"
    def art(self,num):
        if num == 1:
            print("才艺:胸口碎大石")
        if num == 2:
            print("才艺:单手开法拉利")
        if num == 3:
            print("才艺:跳舞")
    def cooking(self):
        print("厨艺:精通八大菜系")
    def work(self):
        print("职业:是个小富婆")
zhangqi = girlfriend()   #类实例化
zhangqi.art(1)
zhangqi.cooking()
zhangqi.work()
print(zhangqi.sex)
print(zhangqi.high)
print(zhangqi.weight)
print(zhangqi.hair)
print(zhangqi.age)