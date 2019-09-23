# # 在python中的引用和地址
# # 使用#查看变量的地址
# a = 1
# print(id(a))
# print(id(1))
# b = a
# print(id(b))
# a = 2
# print(id(a))
# print(id(2))

# 这里需要注意的是，python不同于其他编程语言，其他编程语言要定义一个变量就是
# int a,当a 这个变量存在的时候无法再发定义一个变量a,但是可以对a所指向的内存
# 里面的变量进行修改，但是在python中，定义变量就是a = 10，但是之后再使用
# a = 20的话实际上就是让a这个变量重新指向一个存着20的地址

# # 在python中函数传参实际上传递的是变量的引用
# def test(num):
#     print(id(num))
#     str = "hello"
#     print(id(str))
#     return str
#
#
# a = 10
# print(id(a))
# e = test(a)
# print(id(e))
"""
# # hash()是哈希函数，也是python给我们提供的一个函数
# # 给这个函数传入一个不仅可变类型的值它会根据内部算法，返回一个唯一的值
# print(hash(1))
# print(hash("hello"))
# c = hash((1, 2, 3, 4))
# print(c)
# # 但是不能给哈希函数传参的时候传递可变类型
# # 因为key的底层是使用的hash做的优化，所以key不能使用可变类型的变量
# # 每次我们输入一个key其实是底层优化为哈希换到的数字，这样查找更快速
"""
# num = 100
#
#
# def test1():
#     print(num)
#     global num  # 这里只能分布进行修改 global num = 5 这种是错误的语句
#     num = 5
#     print(num)
#
#
# test1()

# # 返回元组之后，假如要拿到元组里面的数据，可以使用下标的方式，当然也可以一次性定义多个变量来接收元组返回的信息
# def test():
#     return 12, 23  # 给返回的是一个元组，但是（）被省略了
#
#
# # 外部打印
# g_1, g_2 = test()
# print(g_1, g_2)
""""
# # 使用python专有的方法来交换两个变量
# a = 10
# b = 20
# a, b = (b, a)
# # 利用元组交换，将元组中第一个变量返回给外部接受的变量，
# # 将第二个变量返回给外部的第二个变量，之间使用逗号来间隔
# # 和接收返回值的道理差不多
# print(a, b)
"""
"""
# # 在函数内部对于用参数传进来的可变类型和不可变类型
# # 进行赋值运算符的修改能否影响到外界的变量呢？
# def test(num, list_1):
#     num = 10  # 不可变类型
#     print(num)
#     list_1.append(10)  # 使用下标也无法修改列表中的值
#     list_1[1] = 500  
#     print(list_1)
# 
# 
# # 关于函数运行时的说明
# # 在python中运行到函数的时候并不会直接进入而是，直接跳过，也不看也不咋的，
# # 直到运行的时候才会进入函数，与C/C++不同
# gl_num = 20
# gl_list_1 = [5, 6, 7]
# test(gl_num, gl_list_1)
# print(gl_num)
# print(gl_list_1)
"""
