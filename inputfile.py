quantity=int(input("enter the quantity = "))
print(quantity)

rate=int(input("rate ="))
print(rate)

basictotal=quantity*rate
print("basic total =",basictotal)

dis=(basictotal*10/100)
print("discount value = ",dis)

gstp=int(input("enter the gst percentage  = "))
gst=(basictotal*gstp/100)
print("applied  gst =",gst)


nettotal=basictotal+gst
print("the net total =",nettotal)