"""
# 完成石头剪刀布的游戏，主要是为了进行随机数生成的学习
# 使用import导入工具包，应该将导入的语句放到文件的开头
# 因为这样方便下面的代码使用我们所导入的工具包
import random
player = int(input("请出拳：1.石头2.剪刀3.布"))
computer = random.randint(1,3)
print("电脑选择的是%d" % computer)
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
"""
"""
# while 循环的基本语法
i = 0
while i < 5:
    print("我饿了")
    i = i + 1

# 失败，死循环
i = 0
while i < 5:
    print("我饿了")
    ++i
"""
"""
sum = 0
i = 2
while i <= 100:
    sum += i
    i = i + 2
print(sum)
"""
"""
i = 0
while i < 10:
    i = i + 1
    print("我好快乐")
    if i == 3:
        print("我走了")
        continue
"""
# i = 1
# while i<10:
#     print("*"*i)
#     i = i+1
#
#
# # 在默认情况下，print在输出完毕之后会默认在最后一行增加一个换行
# # 如果不想让其输出换行，，就可以使用，end = ""来控制不让其输出换行
# i = 1
# while i <= 10:
#     j = 1     # 每一次循环执行完毕之后都必须使，j = 1重新开始来进行j的计数
#     while j <= i:
#         print("*", end="")
#         j = j + 1
#     print("")   # 这一步只是为了单纯的使语句输出一个换行，因为就算是空语句python也会默认输出一个换行
#     i = i + 1


# # 在一个函数的开头，如果不是顶行，居然需要两个空行，不然就会有白色的波浪线，python代码风格真恶的好严格
# def multiple_table():
#     """
#     可以使用这个专门的格式来个函数增加注释
#     并且这样还可以在调用函数的时候，让光标停留在需要调用函数的上方
#     并且ctrl + Q（大小写无区分）查看函数具体信息
#     """
#     i = 1
#     while i <= 9:
#         j = 1
#         while j <= i:
#             print("\t%d * %d = %d" % (j, i, i*j), end="    ")
#             j += 1
#         print("")
#         i += 1
#
#
# # 函数调用，居然也需要两个空行
# multiple_table()
# # 函数的参数以及返回值
# def sum_2number(num1, num2):
#     return num2 + num1
#
#
# a = int(input())
# b = int(input())
# result = sum_2number(a, b)
# print(result)
# def print_line(num, time):
#     """打印分割线
#     :param num: 分割线所使用的字符
#     :param time: 需要打印的次数
#     """
#     print(num * time)
#
#
# A = input()
# B = int(input())
# print_line(A, B)
# 列表list，在其他的语言中又叫数组，但是使用恰里比其他语言方便很多
# name_list = ["张三", "李四", "王五"]
# print(name_list[0])

# list的常规操作演示
number_list = [8, 9, 7, 5, 6, 3, 1, 2, 4, 0]
# 查看元素
print(number_list[0])
# 查看索引对应的元素
print(number_list.index(5))
# 替换
number_list[2] = "你好"
# 增加
print(number_list)
number_list.append("晚上好")
number_list.insert(5, "python牛逼")  # 双引号输出会有单引号
print(number_list)
number_list2 = ['好秀', '这次我使用的是单引号', '我想看看单引号输出的话会不会有一个单引号']
# 试了一下无论如何都会有单引号，怎样可以取消单引号呢
number_list.extend(number_list2)
print(number_list)
# 删除
number_list.remove("你好")
print(number_list)
number_list.pop()  # 不止是可以弹出最后一个压入的元素，还可以直接填入索引删除指定的索引对应的元素
print(number_list)
# number_list.clear()
# print(number_list)
# del 是关键字delete的缩写
# del删除之后指的是将一个变量直接从内存中删除，将变量删除之后后续的代码将不能使用该变量
del number_list[2]
print(number_list)
print(number_list[2])
# 统计
print(len(number_list))
print(number_list.count(0))  # 查看0这个元素在数组中出现的次数
# remove删除的是当前列表出现的第一个所要删除的值

# 关于排序，我发现 ，单独的str可以排序，单独的数字可以排序，但是数字和字符合并之后就没有办法再进行排序
# 但是python允许在一个列表中同时出现字符和数字类型
number_list3 = [8, 9, 7, 5, 6, 3, 2, 14, 5]
number_list3.sort()
print(number_list3)
number_list4 = ["张三","王五","李四"]
number_list4.sort()
print(number_list4)
# number_list3.extend(number_list4)
print(number_list3)
number_list3.sort(reverse=True)
print(number_list3)
number_list4.reverse()
print(number_list4)