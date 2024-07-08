class employee:
    def details():
        name1=input("enter the name ")
        age1=int(input("enter the age "))
        name.append(name1)
        age.append(age1)


    def display():
        for i in range(len(name)):
             print("name = %s \n age = %d"%(name[i],age[i]))

name=[]
age=[]

e1=employee
e1.details()
e1.display()