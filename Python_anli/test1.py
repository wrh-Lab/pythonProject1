# 首先定义一个小车价格的类
class Car:
    price = 100000

    def __init__(self, c):
        self.color = c


car1 = Car("Red")   #引用类，并将其进行实例化
car2= Car("Blue")
print(car1.color+car2.color)#输出实例化

Car.price=11000000  #修改类属性
print(Car.price)
Car.name="QQ"  #添加类的属性，通常这种添加的方法是对类内部直接进行修改
car1.price=12   #这就是另一种修改类属性的方法，不过这种修改方式是对对象名进行修改，
# 就像是对类名的映射进行修改一样，对类本身的属性不产生影响
print(car1.price)
print(Car.name ,Car.price)  #对于同时打印类里面的属性，两者之间不能使用“+”符号进行连接

car1.color="Yellow"  #修改实例属性
print(car1.color)

def setSpeed(self,s):
    self.speed=s

    print("第二次更改")
import types
car1.setSpeed=types.MethodType(setSpeed,car1) #动态为成员添加成员方法
x=car1.setSpeed(50)
print(x)