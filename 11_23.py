# class A:
#     def __init__(self):
#         self.__number = 200
#         self.number = 100
#     def __test(self):
#         print("私有方法")
#     def test(self):
#         print("公有方法")
#         # 在父类的内部可以调用自己的私有公有方法都可以
#         self.__test()
#         print(self.__number)
#         print(self.number)
# class B(A):
#         def __init__(self):
#             print("我是子类")
# b = B()
# b.
# # b.__test()

# class A:
#      def test(self):
#          pass
# class B(A):
#     def func(self):
#         pass
# class C(A):
#     def functest(self):
#         pass
# class D(B,C):
#     pass
# d =D()
# d.test()   # 这也就是C++中的菱形继承，钻石继承，C++中为了解决二义性引入的是虚继承，但是在python中没有让用户解决，而是解释器自己解决了菱形继承的二义性
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def game(self):
#         print("蹦蹦跳的玩耍")
# class GodDog(Dog):
#     def __init__(self,name):
#         self.name = name
#     def game(self):
#         print("飞上天去玩耍")
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def game(self,dog):
#         print("%s和%s玩耍" % (self.name,dog.name))
#         dog.game()
#
# dog = Dog("旺财")
# xiaoming = Person("小明")
# xiaoming.game(dog)
# dog1 = GodDog("飞天旺财")
# xiaoming = Person("小明")
# xiaoming.game(dog1)

# class Tool(object):
#     count = 0
#     def __init__(self):
#         Tool.count += 1   # 有这句话可以看出（Tool.count）是类的属性，因为是通过类名去调用的，而不是对象的self
#
# a = Tool()
# b = Tool()
# print(Tool.count,end="")
# class Tool:
#     count = 0
#     @classmethod
#     def show_tool_count(cls):
#         print("现在拥有的工具数量是%d" % Tool.count)
#
#     def __init__(self,name):
#         self.name = name
#         print("创建对象成功,它的名字是%s" % self.name)
#         Tool.count += 1
#
#     # def __del__(self):
#     #     print("%s" % self.name)
#
# tool1 = Tool("斧头")
# tool2 = Tool("砍刀")
# tool3 = Tool("棍子")
# Tool.show_tool_count()
# class Dog:
#     @staticmethod   # 表示你写的函数将会是一个静态的方法
#     def run():  # 因为不需要调用对象的属性，所以就不需要传递self
#         print("小狗要跑")
#
# Dog.run()  # 可以不用定义对象直接在类外访问静态方法
# class Game:
# #     top_score = 0
# #     @staticmethod
# #     def show_help():
# #         print("不要让僵尸进入你的房间")
# #
# #     @classmethod
# #     def show_top_score(cls):
# #         print("历史最高分时%s" % Game.top_score)
# #
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def start_game(self):
# #         print("%s,请开始你的游戏" % self.name)
# #
# # Game.show_help()
# # Game.show_top_score()
# # game = Game("🔅")
# # game.start_game()















