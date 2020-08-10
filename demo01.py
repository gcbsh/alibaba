# print(type("你好,hellow world"))
# print(type(2333333))
# print(type(True) ) #布尔类型
# print(type(()))    #元组
# print(type([])  ) #数组
# print(type({}) )  #字典
"""多行注释"""


# a = (input("请输入:"))
# b = (input("请输入:"))
# print("input获取的内容:",len(a+b))


#a = ("input获取的内容:",2>3,2222,(),[],{})
#print(a[2])  //打印标为2的字符,下标从0开始,-1从最后开始
# print(a.index(2222))  #查找字符串的下标,就近原则
# print(a.count(2222))  #统计元组内该字符的数量
# b=(a,"黄淮","O(∩_∩)O哈哈~")
# print(b[0][1])    #多元元组
# print(a[0:2])    #切片,去0到2的字符,左闭右开


# a = ["input获取的内容:",2>3,2222,(),[],{}]
# # a.append(333) #数组追加数据
# a.insert(2,111)   #数组插入数据
# b = a.pop(2)    #pop拿值
# a.extend(a)    #插入数组,与print(a+a)效果一样


# a = {"id":1,"name":"李四","age":51}
# a["sex"] = "男"  #没有则插入,有则修改
# a.update(学历 = "本科") #插入一条数据
# del a["学历"]     #删除一条数据
print(a)  #取值

# name = (input("请输入您的姓名:"))
# age = (input("请输入您的年龄:"))
# a = {"name":name,"age":age}
# print(a)