# f = open("sss.txt",'w')
# f.write("good lucky")
# f.close()
# f = open("sss.txt",'r')
#
# # print(f.read(5))#按个数读取
# # print(f.readable())#判断这段文字是否可读
# # print(f.readline(11))#按个数读取内容
# print(f.readlines())#读取所有内容


#a = 'abcdefghijk'
# print(a[0])#下标
# print(a[-1])#取最后一位字符
# print(a[0:-2:2])#[开始下标：结束下标:-代表倒序+步长]
#print(a[::])#取所有的字符

# for a in range(1,10):
#     for b in range(1,a+1):
#         print("{}x{}={}".format(b,a,a*b),end="\t")
#     print()
# z = [1,2,53,5,9,4,6]
#
# z[0] = 25#根据下标修该下标对应的值
# print(z)
# z[1:3] = 25,30# 根据多个下标修多个下标对应的值
# print(z)

# a = [1,2,1,6,4,5,6,7,8]
# a.insert(0,"翠花")#在确定下标插入一个字符
# a.append("翠花1")#在列表后边追加一个元素
#
# print(a)
# a.pop(2)
# print(a)

# a.remove(1)
# a.clear()#全部清除
# print(a)

# d = {"name":"翠花","age":18,"sex":"女"}
# print(d )
# d.update({"sid":"上海浦东"})
# print(d)



# try:
# #     a = open("ccc.txt")
# #     print(a.read())
# #     a.close()
# # except:
# #     print("没找到文件")
# # print("操作完文件")

class CustomException(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value

        def __str__(self):
            return self.value


a = 0
try:
    if a == 0:
        print("a={} 触发异常".format(a) )
        raise CustomException
    print("a={} 未触发异常".format(a))
except CustomException as e:
    print(a)