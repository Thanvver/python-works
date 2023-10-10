celc=float(input("enter your body temparature: "))
faht=celc*(9/5)+32
print(faht)
if(faht>99):
    print("the person is having fever")
else:
    print("normal temparature")