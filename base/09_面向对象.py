class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        # 哪一个对象调用该方法,self就指向该对象
        print("The cat's name is %s" % self.name)
        print("The cat like eat fish")

    @staticmethod
    def drink():
        print("The cat need drink water")

    def __del__(self):
        print("The cat is dead")


tom = Cat("Tom")
tom.name = "Tom"  # 给对象增加属性(不推荐)
tom.drink()
tom.eat()
print("%x" % id(tom))  # %x会将数字以16进制输出
print(dir(tom))  # python内置函数dir(),可以查看变量的所有方法和属性


"""
对象的内置方法:
  __init__方法:构造函数
  __del__方法:析构函数,在对象销毁时调用
  __str__方法:类似toString()方法,返回对象的描述信息
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return "我是%s,我的体重是%.2fkg" % (self.name, self.weight)


person = Person("小明", 50)
person.run()
print(person)


"""
被使用的类应该先开发
"""


class HouseItem:
    """
    家具类,家具名称,占地面积
    """
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s,占地面积为:%.2f" % (self.name, self.area)


class House:
    """
    房子类,户型,面积,家具列表,剩余面积
    """
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("这间房子为%s户型,占地面积为%.2f平方米,家具有%s,剩余面积为%.2f平方米"
                % (self.house_type,
                   self.area,
                   self.item_list,
                   self.free_area))

    def add_item(self, item):
        if item.area > self.free_area:
            print("%s的面积过大." % item.name)
            return
        self.item_list.append(item.name)
        self.free_area = self.free_area - item.area


house = House("别墅", 100)
desk = HouseItem("桌子", 2.0)
bed = HouseItem("床", 3.0)
house.add_item(desk)
house.add_item(bed)
print(house)
# 385

"""
ak案例
"""


class Gun:
    def __init__(self, mode, bullet_count):
        self.mode = mode
        self.bullet_count = bullet_count

    def shoot(self):
        if self.bullet_count <= 0:
            print("The Gun Have No Bullet")
            return
        self.bullet_count -= 1

    def add_bullet(self):
        self.bullet_count += 1

    def __str__(self):
        return "The Gun's Mode is %s" % self.mode


class Solder:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("The Solder Have Not Gun")
            return
        self.gun.shoot()
        print("The Solder %s Have Fired!" % self.name)


ak47 = Gun("ak47", 2)
three = Solder("More Three", None)
three.fire()
three.fire()
three.fire()
