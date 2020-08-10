#判断
# a = 1
# b = 2
# if a > b:
#     print("a>b")
# else :
#     print("b更大")


# age = int(input("请输入你的年龄:"))
# if age > 60:
#     print("退休")
# elif age > 30:
#     print("好好上班")
# elif age > 20:
#     print ("找个好工作")
# else:
#     print("好好读书")

# chengjilist = {}
# studentllist = ["张三","李四","麻五","赵六","田七","王八","皮九"]
# a = 0
# while a < len(studentllist):
#     chengji = int(input("请输入"+studentllist[a]+"的成绩"))
#     chengjilist.update({studentllist[a] : chengji})
#     a = a+1
# chengjilist.update(万十 = "20")
# print(chengjilist)
# print(chengjilist["万十"])



# a = ["张三","李四","麻五","赵六","田七","王八","皮九"]
# for i in a:
#     print(i)


# for i in range(100):
#     print(i)


# for b in range(1,10):
#     for a in range(1,b+1):
#         print(a,"x",b,"=",a*b,end=" ")
#     print()

# a = 1
# while a <=9:
#     b = 1
#     while b <=a:
#         print(a,"x",b,"=",a*b,end=" ")
#         b = b+1
#     a = a+1
#     print()


#模拟红绿灯,30次红灯,35次绿灯,3次黄灯
while True:
    t = 30
    for h in range(30):
        print("红灯还有",t,"秒结束")
        t-=1
    t = 35
    for h in range(35):
        print("绿灯还有",t,"秒结束")
        t-=1
    t = 3
    for h in range(3):
        print("黄灯还有",t,"秒结束")
        t-=1


#实现一个注册功能
# userlist = []
# passwordlist = []
# userpassword = {}
# user = input("账号:")
# for i in user:
#     userlist.append(i)
# if userlist[0] in "qwertyuiopasdfghjklzxcvbnm" and 5<=len(userlist)<=8:
#     password = input("密码:")
#     for j in password:
#         passwordlist.append(j)
#     if 6<=len(passwordlist)<=12:
#         userpassword.update({user:password})
# else:
#     print("账号必须以小写字母开头且长度在5-8之间,密码长度在6-12之间")
# print(userpassword)


