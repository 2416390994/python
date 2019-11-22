# 1
# class Cat:
#     def eat(self):
#         print("%s爱吃鱼"%self.name)
#     def drink(self):
#         print("小猫爱喝水")
#
# Tom = Cat()  # 定义对象的方式和C++不太一样
# # Tom.name = "汤姆"
# Tom.eat()
# Tom.name = "汤姆"
# class Cat:
#     def __init__(self,new_name):
#         print("这是一个初始化方法")
#         self.name = new_name
#     def eat(self):
#         print("%s爱吃鱼"%self.name)
    # def __str__(self):
    #     return '呦吼'

# Tom = Cat("汤姆")
# print(Tom)
# Tom.eat()
# big_cat = Cat("大懒猫")
# big_cat.eat()


# class Person:
#
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return "我是%s，我的体重是%.2f" % (self.name, self.weight)
#
#     def run(self):
#         print("%s爱跑步，跑步锻炼身体" % self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         print("%s爱吃东西" % self.name)
#         self.weight += 1
#
# xiaoming = Person("小明", 170)
# xiaoming.eat()
# print(xiaoming)
# xiaoming.run()
# print(xiaoming)
# xiaoming.eat()
# print(xiaoming)

# class Gun:
#     def __init__(self, model):
#         #设置枪的型号
#         self.model = model
#         # 设置枪独的初始子弹数量
#         self.bullet_count = 0
#
#     def add_bullet(self, count):
#         # 设置给枪添加的子弹数量
#         self.bullet_count = count
#
#     def shoot(self):
#         # 判断子弹数量是否为空
#         if self.bullet_count <= 0:
#             print("没有子弹了")
#             return
#
#         # 枪的子弹-1
#         self.bullet_count -= 1
#         # 开火
#         print("%s哒哒哒,还剩下%d子弹" % (self.model, self.bullet_count))
#
#
# class Soilder:
#     def __init__(self, name):
#         # 士兵姓名
#         self.name = name
#         # 新兵没有枪
#         self.gun = None


#
#     def fire(self):
#         # 判断士兵是否有枪
#         if self.gun == None:
#            print("%s,还没有枪..." % self.name)
#            return
#         # 高喊口号
#         print("冲压...[%s]" % self.name)
#         # 让枪装满子弹
#         if self.gun.bullet_count <=  0 :
#             self.gun.add_bullet(50)
#         # 让枪发射子弹
#         self.gun.shoot()
#
# # 定义一把枪
# ak47 = Gun("AK47")
# # 创建一个士兵
# xusanduo = Soilder("许三多")
# # 给士兵一把枪
# xusanduo.gun = ak47
# # 让枪开火
# xusanduo.fire()
# xusanduo.fire()
# xusanduo.fire()

# list1 = [1,2,3]
# list2 = [1,2,3]
# list3 = list1
# print(list1 == list2)
# print(list1 is list2)
# print(list1 is list3)

# class Women:
#
#     def __init__(self):
#         self.__age = 18
#         self.name = "小芳"
#
# xiaofang = Women()
# print(xiaofang.name)
# print(xiaofang.__age)  # 私有属性内外不能访问

# class Women:
#
#     def __init__(self):
#         self.__age = 18
#         self.name = "小芳"
#
#     def __printf(self):
#         print(self.name,end="")
#
# xiaofang = Women()
# print(xiaofang.name)
# # xiaofang.__printf()         # 通过这样的方法是不可以访问到私有方法的
# xiaofang._Women__printf()   # 但是通过这种方法就可以访问到，所以说python中是没有真正意义上的私有的
#                             #但是不推荐使用，因为既然方法给成了私有就有他自己的道理
class Animal:
    def run(self):
        print("跑")
    def drink(self):
        print("喝")
    def eat(self):
        print("吃")
    def sleep(self):
        print("睡")


class Dog(Animal):

    def jiao(self):
        print("叫")


class GodDog(Dog):

    def fly(self):
        print("飞")


xiaotianquan = GodDog()
xiaotianquan.eat()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.drink()
xiaotianquan.fly()
xiaotianquan.jiao()



















