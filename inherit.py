class parent:
    def func1():
        print("this is parent class")


class child(parent):
    def func2():
        print("this is child class")

obj1=child
obj1.func1()
obj1.func2()               