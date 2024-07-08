class father:
    def func1():
        print("this is father")


class mother:
    def func2():
        print("this is mother class")

class child(father,mother):
    def mfunc():
        print ("this is inherited child class")                


obj=child
obj.func1()
obj.func2()
obj.mfunc()
