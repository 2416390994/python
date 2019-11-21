# a = 20
# a = a // 3
# print(a)
# i = 0
# while i < 5:
#     print(123)
# 在默认情况下，print在输出完毕之后会默认在最后一行增加一个换行
# 如果不想让其输出换行，，就可以使用，end = ""来控制不让其输出换行
# i = 1
# while i <= 10:
#     j = 1     # 每一次循环执行完毕之后都必须使，j = 1重新开始来进行j的计数
#     while j <= i:
#         print("*", end="")
#         j = j + 1
#     print("")   # 这一步只是为了单纯的使语句输出一个换行，因为就算是空语句python也会默认输出一个换行
#     i = i + 1
# i = 1
# while i <= 10:
#     print("*"*i)
#     i = i + 1
# #
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d" % (j, i, i*j), end="\t")
#         j += 1
#     print("")
#     i += 1
# name_TOM = {"姓名": "小明",
#             "年龄": 50,
#             "身高": 1.5}
# print(type(name_TOM))
# print(name_TOM)  # 输出顺序往往和我们的定义顺序不一样，因为人家本身内部就不关心排序顺序
# # 取值
# print(name_TOM["姓名"])
# # 修改
# # 修改的时候如果key不存在就会新增键值对，也就是说key不存在的话就类似于增加
# name_TOM["姓名"] = "小红"
# print(name_TOM["姓名"])
# 使用循环遍历字典
# 一般应用中很少会对字典进行遍历
# name_TOM = {"姓名": "小明",
#             "年龄": 50,
#             "身高": 1.5}
# for k in name_TOM:  # k是每次循环遍历的时候的键值
#     print("%s   %s" % (k, name_TOM[k]))
# # 将多个字典放在一个列表中，再进行遍历
# card_list = [
#     {"姓名": "小刚",
#      "年龄": "20",
#      "身高": "1.85"},
#     {"姓名": "小雷",
#      "年龄": "28",
#      "身高": "1.55"},
# ]
# for into_card in card_list:
#     print(into_card)
# 按文本要求输出字符串
# poem = ["登鹳雀楼",
#         "王之涣",
#         "白日依山尽",
#         "黄河入海流",
#         "欲穷千里目",
#         "更上一层楼"]
# for c in poem:
#     print(c)
# for c in poem:
#         print("|%s|" % c.center(10))
# 1.拆分字符串
# hello = "\n\thello \tworld \rpig \ndog \tapple \nphone\n"
# # 首先将字符串中的所用的空白字符去掉，
# # 然后再使用“ ”作为分隔符拼接成一个完整的字符串
# hello2 = hello.split()  # 如果这里不指定去除什么分隔符的话，那么就会将所有的分隔符都去除掉
# print(hello2)
# hello3 = hello.split(" ")  # 指定空格的话那么就只能够将" "这种分隔符去掉
# print(hello3)
# # 2.合并字符串
# hello4 = " ".join(hello2)  # 这里将已经去除掉分隔符的字符串拿过来直接进行拼接
# # 这里指的就是拿空格拼接，当然你还可以指定其他的字符
# print(hello4)
# # 上面的这些操作的应用场景是在从网络上抓下的数据，进行处理
# # 因为不同的协议可能规定的协议结尾标识符不一样有的是\r\n，
# # 然后抓下来的数据就很不清晰，这样就可以使打印的数据很清晰

# 完整的for循环语法
# for num in [1, 2, 3, 4, 5, 6]:
#     print(num)
#     if num == 2:
#         break
#     # 只有for循环完毕，才会执行下面的语法不然就不会执行
#     # 使用break退出的话就不会执行else
#     else:
#         print("遍历完毕")
# print("我是院长")
# 在python中的引用和地址
# 使用#查看变量的地址
# a = 1
# print(id(a))
# print(id(1))
# b = a
# print(id(b))
# a = 2
# print(id(a))
# print(id(2))
# del(a)
# hash((1,2,3))
# 在函数内部对于用参数传进来的可变类型和不可变类型
# 进行赋值运算符的修改能否影响到外界的变量呢？
# def test(num, list_1):
#     num = 10  # 不可变类型
#     list_1 = [1, 2, 3]  # 可变类型
#     # 这里只要一旦进行了= 操作就相当于在内存中重新规划了一块内存，将形参的标签放在了新申请的空间上面
#     # 这个时候在赋值操作下面再进行所谓的方法进行修改也是无法改变外部的全局变量的
#     print(num)
#     print(list_1)
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
# def test(num, list_1):
#     num = 10  # 不可变类型
#     print(num)
#     list_1.append(10)  # 使用下标也无法修改列表中的值
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





