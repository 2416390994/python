"""
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
"""
"""
在python字典是除了列表以外最灵活的一种数据类型
列表一般用来存储有序的数据类型，字典用来存储无序的数据类型
上面所说的有序和无序指的是，就类似于数组和哈希表，我们关心数组中的元素顺序
但是我们只关心哈希表中根据key可以拿到哪些数据
name_TOM = {"姓名": "小明",
            "年龄": 50,
            "身高": 1.5}
print(type(name_TOM))
print(name_TOM)  # 输出顺序往往和我们的定义顺序不一样，因为人家本身内部就不关心排序顺序

# 取值
print(name_TOM["姓名"])
# 修改
# 修改的时候如果key不存在就会新增键值对，也就是说key不存在的话就类似于增加
name_TOM["姓名"] = "小红"
print(name_TOM["姓名"])
# 删除
name_TOM.pop("姓名")
print(name_TOM)
# 删除某一个元素
del name_TOM["身高"]
# 删除整个字典
del name_TOM
# 1.统计键值对的数量
print(len(name_TOM))
# 2.合并字典
temp_dict = {1: "姓名",
             2: "年龄",
             3: "身高"}
name_TOM.update(temp_dict)
# 注意在使用合并键值对操作的时候，如果需要合并的字典和原字典键值重名的话，就会覆盖原字典
print(name_TOM)
# 拷贝一个字典
name_TOM2 = name_TOM.copy()
print(name_TOM2)
# 打印所有的键值
print(name_TOM2.keys())
# 清空字典
name_TOM.clear()
print(name_TOM)
"""
"""
# 使用循环遍历字典
# 一般应用中很少会对字典进行遍历
name_TOM = {"姓名": "小明",
            "年龄": 50,
            "身高": 1.5}
for k in name_TOM:  # k是每次循环遍历的时候的键值
    print("%s   %s" % (k, name_TOM[k]))
# 将多个字典放在一个列表中，再进行遍历
card_list = [
    {"姓名": "小刚",
     "年龄": "20",
     "身高": "1.85"},
    {"姓名": "小雷",
     "年龄": "28",
     "身高": "1.55"},
]
for into_card in card_list:
    print(into_card)
"""
"""
# 定义一个字符串变量
# 在python中不仅可以使用" "（双引号）来定义字符串变量
# 而且还可以使用' '（单引号）来定义字符串变量
str1 = "hello world"
# 对于想要输出的字符串中间有" "的时候，外面可以使用' '
str3 = "我的外号是\"大西瓜\""   # 但是这个太不美观了
str2 = '我的外号是"大西瓜"'
print(str1)
print(str2)
print(str3)
for c in str2:
    print(c)
# 1.统计字符串的长度
print(len(str2))
# 2.统计一个小字符串在大字符串中出现的次数
str4 = "hello hello hello"
print(str4.count("llo"))
# 3.某一子子字符串出现的位置,子字符串出现的第一个字符索引的位置
print(str4.index("llo"))
"""
"""
# 字符串的常见操作
# 1.判断是不是空白字符
space_str = "   "
print(space_str.isspace()) # 判断一个字符串是不是只有空格
# 转义字符也属于空白字符

# 2.判断一个字符串是不是只包含数字
num_str = "1\u00b3一千零一"
# \u00b3指的就是上标
print(num_str)
print(num_str.isdecimal())  # 只能判断阿拉伯数字
print(num_str.isdigit())    # 不仅可以判断阿拉伯数字还可以判断unicode
print(num_str.isnumeric())  # 除了能判断上面的那种还可以判断汉字的数字
# 1>三个方法都不能判断小数
# 2>unicode 字符串
# 3>中文数字
"""
"""
hello_str = "hello hello"
# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))
# 2.判断是否已指定的字符串结尾
print(hello_str.endswith("hello"))
# 3.查找指定的字符串
# 同样也是返回索引值，那么和index的不同点在哪呢？
# index在查找字符串中不存在的字符串会报错返回吗，而find没有找到就会返回-1
print(hello_str.find("llo"))
# 4.替换字符串
# 值得说一下的是replace替换完成之后并不是更改原有字符串里面的内容，
# 而是返回一个新的字符串，如果想保存返回的字符串就要使用一个新的字符串变量来接收
# 就好比下面这两个，一个是直接打印替换后的，一个是打印原有的
print(hello_str.replace("hello", "pig"))
print(hello_str)
"""
"""
# 按文本牙要求输出字符串
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for c in poem:
    print(c)
for c in poem:
        print("|%s|" % c.center(10))
"""
"""
# 1.拆分字符串
hello = "\n\thello \tworld \rpig \ndog \tapple \nphone\n"
# 首先将字符串中的所用的空白字符去掉，
# 然后再使用“ ”作为分隔符拼接成一个完整的字符串
hello2 = hello.split()  # 如果这里不指定去除什么分隔符的话，那么就会将所有的分隔符都去除掉
print(hello2)
hello3 = hello.split(" ")  # 指定空格的话那么就只能够将" "这种分隔符去掉
print(hello3)
# 2.合并字符串
hello4 = " ".join(hello2)  # 这里将已经去除掉分隔符的字符串拿过来直接进行拼接
print(hello4)
# 上面的这些操作的应用场景是在从网络上抓下的数据，进行处理
# 因为不同的协议可能规定的协议结尾标识符不一样有的是\r\n，
# 然后抓下来的数据就很不清晰，这样就可以使打印的数据很清晰
"""
"""
# 字符串的切片
num_str = "123456789"
# 1.截取2-5之间的数字
new_num_str = num_str[1:5]
print(new_num_str)
# 2.截取2-末尾的字符串
new2_num_str = num_str[1:]
print(new2_num_str)
# 3.从开始位置截取到5的位置
new3_num_str = num_str[:5]  # 或者[0:5]也可以
print(new3_num_str)
# 4.截取完整的字符串
new4_num_str = num_str[:]
print(num_str)
# 5.从开始位置每个一个字符截取字符串
new5_num_str = num_str[0::2]  # 步长为2意思就是2个切一下
print(new5_num_str)  # 在哪个位置切片就取那个位置后面的元素
# 6.从索引1开始每隔一个取一个
new6_num_str = num_str[1::2]
print(new6_num_str)
# 截取2-末尾-1的字符
new7_num_str = num_str[1:-1]
print(new7_num_str)
# 截取字符串末尾的两个字符
new8_num_str = num_str[-2::]
print(new8_num_str)
# 通过切片获取字符串的逆序
new9_num_str = num_str[::-1]
print(new9_num_str)
"""
"""
# 返回的是True或者False
print("s" > "4")
# 值得注意的是两个字典之间是不可以比较大小的，其它类型都是可以的
"""
"""
# 对列表和元组进行切片
num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num2 = num1[1::2]
print(num2)
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num4 = num3[1::2]
print(num4)
# 不能对字典进行切片
"""
""""
# 完整的for循环语法
for num in [1, 2, 3, 4, 5, 6]:
    print(num)
    if num == 2:
        break
    # 只有for循环完毕，才会执行下面的语法不然就不会执行
    # 使用break退出的话就不会执行else
else:
    print("遍历完毕")
print("我是院长")
"""
"""
name_list = [{"姓名": "瘪三", "年龄": 20},
             {"姓名": "翔子", "年龄": 60},
             {"姓名": "犊子", "年龄": 40},
             {"姓名": "牛根", "年龄": 50}]
find_name = input("请输入你要查找的人的名字：")
for temp_name in name_list:
    if temp_name["姓名"] == find_name:
        print("找到了%s,%s在字典中，他的年龄是%d" % (find_name, find_name, temp_name["年龄"]))
        break
else:
    print("没找到%s,%s不在字典中" % (find_name, find_name))
"""
