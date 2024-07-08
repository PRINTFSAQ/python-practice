class grandfather:
    def func1():
        print("this is your grandfather ")

class father(grandfather):
    def func2():
        print("this is your father ")
class child(father):
    def func3():
        print("this you own child class")


obj=child
obj.func1()
obj.func2()
obj.func3()
       