per=int(input("enter the percentage = "))

if(per<34):
    print("the candidate is fail")

    if(per>35 and per<50):
        print("candidate is passed")

elif(per>=50 and per<60):
    print("second class")


elif(per>=60 and per<70):
    print("first class")

elif(per>=70 and per<100):
    print("distinction")

else:
    print("not valid")