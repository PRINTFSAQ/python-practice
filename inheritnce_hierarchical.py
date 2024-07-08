class parent:
    def func1():
        print("this is parent classs ")


class son1(parent):
    def func2():
        print("this is son1 ")

class son2(parent):
    def func3():
        print("this son 2")
class son3(parent):
    def func4():
        print("this is son 3")


obj=son1
obj.func1()
obj.func2()


obj1=son2
obj1.func1()
obj1.func3()

obj2=son3
obj2.func1()
obj2.func4()