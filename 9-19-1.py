"""
# 查看变量类型
A = 10
print(type(A))
B = "小明"
print(type(B))
# 怎一个爽字了得，根本不用可考虑类型的取值范围
C = 450000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(type(C))
print(type(2**32))
print(type(2**64))
print(C)
"""
"""
# python之间不同的数据类型如何进行计算
# 在python中只要是数字型变量就可以直接计算，
# 无论是什么类型的数字，也无论是哪种类型的算术 运算都可以
# bool类型的数字在参与运算的时候，如果保存的是true那就是1
# 否则的话，也就是false就当作0来运算
A = 10
B = 20.5
C = True
print(A+B+C)
"""
"""
# 字符串相拼接
B = "晨辉"
A= "董"
print(A+B)
# 使用乘号可以重复的拼接字符串
print(A*10)
# 除了上述的两种的字符串和数字的相关的操作之外，其他的字符串和数字的操作
# 都会是错误的
print(A+"10+20")
"""
"""
# 用户和操作系统进行交互，提醒用户输入内容
# input函数实现从键盘输入语句
# input函数得到的类型都是str（字符串类型的）
password = input("请输入银行密码：")
print("密码错误")
"""
"""
# 类型转换函数
# 将字符串类型转换成int和float类型
print(int("123"))
print(float("152.3"))
"""
"""
# 实现买苹果的案例
price_str = input("请输入苹果的价格：")
weight = input("请输入苹果的重量：")
# money = weight * price_str直接这样输出是错误的，因为我说过，input默认都是str类型，
# 在字符串的操作里面除了我之前提到的两个操作之外其他的操作都是非法的
# 所用应该先进行str到int的转换
print(int(price_str)*int(weight))
"""
"""
# 上面的代码使用了太多的变量，现在我们来做一个简化（但是尼玛这叫转换吗？眼睛都花了）
print((int(input("请输入苹果的单价：")))*int(int(input("请输入苹果的重量："))))
"""
"""
# 变量的格式化输出
price = float(input("请输入单价："))
weigh = float(input("请输入重量："))
# 单纯的我以为这样就可以输出了，和C语言一样，万万没想到，吉多这大佬脑回路够清晰的
# print("苹果单价是%f元/斤，购买了%f斤，需要支付%f元",price,weigh,price*weigh)

# 原来要这样写，不禁感叹大佬就是脑回路清晰
print("苹果单价是%.2f元/斤，购买了%.2f斤，需要支付%.2f元"% (price, weigh, price*weigh))
"""
"""
# 定义一个小数，scale，输出数据比例是10.00%
scale = 0.1
print("数据的比例是%.2f%%" % (scale*100))
"""
"""
# 通过下面的命令查看python中的关键字
import keyword
print(keyword.kwlist)
"""
"""
# 判断语句
age = int(input("请输入你的年龄"))   # 这里要先记得把输入的str类型转换成int类型
if age < 18:
    print("你太小了不能进网吧嗨皮")
else:
    print("你可以开始嗨皮了")
"""
"""
# 逻辑运算演练
# 下面进行的是多次判断是否年龄合适
# 注意这里使用的不是else if 而是elif
age = int(input("请输入你的年龄"))
if age <18:   #if语句这里的（）是可以加也是可以不加的
    print("不允许进入网吧，你年龄太小了")
elif age <50:
    print("欢迎进入网吧嗨皮")
else:
    print("你年纪太大了容易嗨死，请不要进入网吧")
"""
"""
# if的嵌套
# 火车站安检
print("请问你是否打算回家？\n"
      "1.不回家\n"
      "2.回家")
chose_1 = int(input())
if chose_1 == 1:
    print("不回家你选个毛线，滚！！！")
else:
    print("这位爷，这边走")
    print("请选择你是否准备购买车票？\n"
        "1.没钱不买\n"
        "2.乞讨车费")
    chose_2 = int(input())
    if chose_2 == 1:
        print("没钱回个屁，赶紧滚！！！")
    else:
        print("来你先进门，检查一下有没有危险品")
        print("有没有带刀?\n"
            "1.没有带\n"
            "2.带刀了")
        chose_3 = int(input())
        if chose_3 == 1:
            print("好孩子，你可以上车回家了")
        else:
            print("你先过来，先扇你一巴掌，谁让你带刀了，教育半小时")
            print("带了多大的刀?\n"
              "1.小于20cm\n"
              "2.大于20cm")
            chose_4 = int(input())
            if chose_4 == 1:
                print("算了，刀也不长，赶紧滚上车")
            else:
                print("你带了20m的大砍刀你还想回家，憨批。赶紧滚下车")
"""










