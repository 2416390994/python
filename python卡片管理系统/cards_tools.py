# 记录所用的名片变量
card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V-1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部名片")
    print("3.搜索名片")
    print("*" * 50)


def new_card():
    # 提示用户输入
    print("-" * 10)
    print("新增名片")
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入Email：")
    # 给输入的信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 将字典添加入列表
    card_list.append(card_dict)
    # 提示用户添加成功
    print("添加成功")


def show_all():
    if len(card_list) == 0:
        print("当前还没有名片，请先进行添加名片操作！")
    else:
        print("-" * 10)
        print("显示所有名片")
        for name in ["姓名", "电话", "QQ", "邮箱"]:
            print(name, end="\t\t\t")
        print("")
        print("=" * 50)
        for card_dict in card_list:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))


def search_card():
    if len(card_list) == 0:
        print("当前名片系统为空，没有可供查询的名片！")
        return
    print("-" * 10)
    print("搜索名片")
    find_name = input("请输入想要查找的名片用户姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))
            print("=" * 50)
            print("")
            # TODO 针对找到的名片进行后续的操作，修改或者删除
            deal_card(card_dict)
            break
    else:
        print("当前名片管理系统不存在你所搜索的用户%s！" % find_name)


def deal_card(find_dict):
    action_str = input("请选择对用户%s进行的操作\t：1.修改 \t2.删除\t 0 返回上级菜单\t" % find_dict["name"])
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名(不改变输入空格)：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话(不改变输入空格)：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ(不改变输入空格)：")
        find_dict["email"] = input_card_info(find_dict["email"],"email(不改变输入空格)：")
        print("修改成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功！")


def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
