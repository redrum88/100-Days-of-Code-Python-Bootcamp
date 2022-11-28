# import math
#
#
# def add(*args):
#     result = math.fsum(args)
#     return result
#
#
# total = add(1, 2, 3)
# print(total)

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=2, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Audi")
print(my_car.make)