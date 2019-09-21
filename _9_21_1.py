# # import keyword
# # print(keyword.kwlist)
# # print(len(keyword.kwlist))
# name_space = ["今天","天气","好","晴朗"]
# # 使用迭代遍历列表，便利的时候需要指定临时变量，类似于下面的my_name，
# # 遍历的时候就会把列表里面的元素保存在临时变量里面然后再依次打印出来
# for my_name in name_space:
#     print(my_name, end="")


# # 元组tuple，意思就是由多个元素组成的序列，与列表类似，但是元组里面的元素是不能修改的
# # 元组是使用（）定义的，但是列表是使用[ ] 来定义的
# info_tuple = ("小明", 18, 17.5)
# print(type(info_tuple))  # 查看定义的（）类型到底是什么类型的数据，打印发现真的是tuple类型
# print(info_tuple[0])  # 查看元组中的元素
# # 定义一个空的元组
# # 我们知道的元组在定义好之后是不允许被修改的，也就是说我们平时很少去定义空的元组，但是我们必须知道
# empty_tuple = ()
# # 怎样定义只有一个元素的元组
# # 当我们像下面这样定义一个元组的时候，其实我们定义的并不是一个元组，
# # 而是一个int类型的数据，那是因为python的解释器会自动把括号拿走，然后只剩下一个5，这样就会被认为定义了一个int类型的数据
# single_tuple1 = (5)
# # 真正想要定义只有一个元素的元组改怎么做呢？那就要在元组的唯一的一个元素后面跟上一个 ' ，'
# single_tuple2 = (5,)

# # 元组的自带操作
# tuple1 = (1, 2, 5, 6, 3, 4, 7, 8, 9, 0)
# print(tuple1.count(2))  # 查看某个元素在元组中出现的次数
# print(tuple1.index(0))  # 查看某个元素在元组里所对应的索引号

# # 在日常的工作中其实直接点元组的遍历其实并不多,因为元组中的数据类型都不一致
# tuple1 = (1, 2, 5, 6, 3, 4, 7, 8, 9, 0)
# for my_tuple in tuple1:
#     print(my_tuple,end="")

# # 使用元组来拼接一个新的字符串
# tuple4 = ("小明", 18, 1.75)
# print("我的名字叫%s,今年%d岁，我身高%.2f" % tuple4)
# info = "我的名字叫%s,今年%d岁，我身高%.2f" % tuple4
# print(info)
# # 元组与列表的相互转化
# list1 = [1, 2, 3, 4, 5, 6]
# tuple5 = ("你还好吗？",123)
# new_list = list(tuple5)
# print(type(new_list))   # 查看打印信息，元组已经被转换为列表
# new_tuple = tuple(list1)
# print(type(new_tuple))
import time, os
import webbrowser


Break_time = 1
i = 0
while i < Break_time:
    webbrowser.open("https://blog.csdn.net/weixin_43767691/article/details/100929709")
    webbrowser.open("https://blog.csdn.net/weixin_43767691/article/details/101054562")
    webbrowser.open("https://blog.csdn.net/weixin_43767691/article/details/101036129")
    webbrowser.open("https://blog.csdn.net/weixin_43767691/article/details/100882628")
    time.sleep(60)
    os.system("taskkill/IM Chrome.exe")



