# a = 10
# b = 5
# print(a + b)
#
# for i in range(10):
#     print(i)
#
# # 解包赋值
# a, b, c = (1, 2, 3)
# print(a, b, c)
#
# x, y, *z = (1, 2, 3, 4, 5,)
# print(x)
# print(y)
# print(z)
#
# x, y, *z = (1, 2, 3, 4, 5,)
# print('x =', x)
# print('y =', y)
# print('z =', z)
#
# a = 10
# b = 20
# print(a + b)
# c = a + b
#
# (2 + 2 == 1 + 3)
# print(2 + 2 == 1 + 3)
#
# z = 13
# print(z % 10)
#
# z = 1564982
# print(z % 10)
# z //= 10
# print(z)
#
# z = 1564982
# z %= 10
# print(z)
# z //= 10
# print(z)
#
# """
# 成绩评定： 0-59分  不及格  60-70  及格  71-80  良好   81-100  优秀
# 给定任意成绩，程序运行之后输出该成绩的级别
# """
# score_list = [10, 20, 30, 40, 88, 92, 73, 65]
# for score in score_list:
#     if (score < 60):
#         print('不及格')
#     elif (60 <= score <= 70):
#         print('及格')
#     elif (71 <= score <= 80):
#         print('良好')
#     elif (80 <= score <= 100):
#         print('优秀')
#     else:
#         print('请输入正确的成绩')
#
# s = 0
# for i in range(100):
#     s = s + i
# print(s)
#
# for i in range(0, 100, 2):
#     print(i)
#
# # 求出10*9*8...*1 d=的结果 10的阶乘  10！
# sum = 1
# for x in range(10, 0, -1):
#     sum *= x
#     print(sum)

# flag = True
# a = 44
# while flag:
#     b = int(input("请输入数字"))
#     if (b > a):
#
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         flag = False


# s = 1
# for i in range(100):
#     s = s + i
#     print(s)
#
#
# s = 1
# for i in range(0,):
#     s = s + i
#     print(s)
#
#
#
# a = 10
# b = 10


"""
成绩评定： 0-59分  不及格  60-70  及格  71-80  良好   81-100  优秀
给定任意成绩，程序运行之后输出该成绩的级别
"""
# score = 75
# if score <= 59 and score >= 0:
#     print("不及格")
# elif score <= 70 and score >= 60:
#     print('及格')
# elif score <= 80 and score >= 71:
#     print('良好')
# elif score <= 100 and score >= 81:
#     print('优秀')
# else:
#     print('成绩无效')

#
#
# for i in range(1,100):
#     if (i % 3  == 0):
#         # continue
#         print(i)


# for i in range(1,90):
#     if (i % 2 !=0):
#         print(i)


#定义一个求两个数商和余数的方法

#
# a = 10
# b = 2
# s = a // b
# y = a % b
# print(s,y)

# def sy(a,b):
#     print('商为',a // b,'余为',a % b)
#
# sy(9,3)
# sy(27,2)


# def sy(a,b):
#     if (b == 0):
#         print('除数不能为0')
#     else:
#         print('商为',a // b,'余为',a % b)
#
# sy(27,3)
# sy(27,0)



# def sy(a,b):
#     if (b == 0):
#         return None
#     else:
#         return (a // b,a % b)
# sy(27,3)
# sy(27,0)
# print(sy(27,2))

# re = sy(25,5)
# if re == None:
#     print('参数错误')
# else:
#     print('商为:', re[0],'余为:', re[1])


# re = sy(b=5,a=25)
# if re == None:
#     print(re)
#     print('参数错误')
# else:
#     print('商为:', re[0],'余为:', re[1])

# c = 1, 2, 3, 4,
# a,*b = (1, 2, 3, 4)
#
# print(b)


#
# class calculator():
#     a = None
#     b = None
#     res = None
#     def input(self,a,b):
#         self .a = a
#         self .b = b
#     def sum(self):
#         self.res =self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_res(self):
#         return self.res
#
# cal = calculator()
# cal.input(10,5)
# cal.sum()
# print(cal.get_res())
# cal.div()
# print(cal.get_res())


# class calculator():
#     res = None
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         self.res =self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_res(self):
#         print(self.res)
#
# c = calculator(10,5)
# c.sum()
# c.get_res()
# c.div()
# c.get_res()

# b = [1,5,6,8,2,7,5,8,4,4,9]
# len(b)
# print(len(b))







# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,"X",a,"=",a*b,end="\t")
#     print()
#

# for i in range(1,10):
#     print(i)


# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,'X',a,'=',a*b,end='\t')
#     print()

# for a in range(9,0,-1):
#     for b in range(1,a+1):
#         print(b,'X',a,'=',a*b,end='\t')
#     print()




# a = [1, 5, 6, 99, 6, 4, 6, 48, 8, 33, 77, 85, 78, 3,2]
#
# #获取列表A的长度，并赋值给B
# q = len(a)
# #通过循环拿到每一次最大值得比对次数
# for w in range(q-1,0,-1):
# #通过循环拿到要比对的数的下标
#     for e in range(1,w):
# #获取列表前一位数和后一位数值进行比较
#         if a[e] > a[e+1]:
# # #如果满足if后面的条件要执行交换的操作
#             a[e],a[e+1] = a[e+1],a[e]
# #打印A排序后的值
# print(a)


# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,"x",a,"=",a*b,end="\t")
#
#     print()

#
# for a in range(9,0,-1):
#     for b in range(1,a+1):
#         print(b,"x",a,"=",a*b,end="\t")
#     print()


# a = [5, 8, 9, 3, 86, 56, 55, 49, 37, 22, 9, 7, 1, 69]
#
# e = len(a)#获取列表A的长度，并赋值给e
# for b in range(e-1,0,-1):
#     for c in range(0,b):
#         if a[c] > a[c+1]:
#            a[c],a[c+1] = a[c+1],a[c]
# print(a)


# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,"x",a,"=",a*b,end="\t")
#     print()


#a.用户输入1-7七个数字，分别代表周- .到周 日
# b.如果输入1~5，打印对应的“周."~“周五”， 如果输入的数字是6或7.打印输出“周末":
# c.如果输入0，退出循坏
# d.输入其他内容，提示:“输入有误，请重新输入!”


# t = True
# a=["一","二","三","四","五","六","末",]
# while t:
#     b =int(input("输入数字"))
#     if b > 0 and b < 8:
#         print("周",a[b-1])
#     elif b == 0:
#         break
#     else:
#         print("输入有误，请重新输入!")



# s="一二三四五六日"
# a = [1,2,3,4,5,6,7]
#
# while True:
#     c = eval(input("请输入数字："))
#     if c in a:
#         print("今天为星期{}".format(s[c-1]))
#         break
#     elif c>=8:
#         print("输入有误，请重新输入!")


#a.用户输入1-7七个数字，分别代表周- .到周 日
# b.如果输入1~5，打印对应的“周."~“周五”， 如果输入的数字是6或7.打印输出“周末":
# c.如果输入0，退出循坏
# d.输入其他内容，提示:“输入有误，请重新输入!”
# t = True
# # a =["周一","周二","周三","周四","周五","周六","周末"]
# # while t:
# #     b=int(input("输入数字"))#input()代表从控制台获取数据，（）里面输入的代表提示
# #     if b<8 and b > 0:
# #         print(a[b-1])
# #     elif b == 0:
# #         print("退出循坏")
# #         break
# #     else:
# #         print("输入有误，请重新输入!")


#a.用户输入1-7七个数字，分别代表周- .到周 日
# b.如果输入1~5，打印对应的“周."~“周五”， 如果输入的数字是6或7.打印输出“周末":
# c.如果输入0，退出循坏
# d.输入其他内容，提示:“输入有误，请重新输入!”
# t = True
# a = ["周一","周二","周三","周四","周五","周六","周日"]
# while t:
#     b = int(input("请输入数字"))#input()代表从控制台获取数据，（）里面输入的代表提示
#     if b<8 and b>0:
#         print(a[b-1])
#     elif b == 0:
#         print("退出循环")
#         break
#     else:
#         print("输入有误，请重新输入!")


class bbb():
    money = 1000
    house = 100
    __clothes = "衣服"

    def public_function(self):
      print("公有方法")
    def __private_function(self):
        print("私有方法")
# print(bbb.house)
# print(bbb.money)
# bbb().public_function()

# class son(bbb):
#     hobby = "花钱"
# print(son.hobby)
# print(son.money)
# print(son.house)
# son().public_function()


# if __name__ =='__main__':
#     name = '翠花'

#
# l = [1,2,3,4,5,6,7,8,55]
# s ={1,2,3,4,5,6,9,8,6,7}
# #字符串转列表
# print(list(abs(a))


# f = open("sss.txt",'w')
# f.write("good lucky")
# f.close()


