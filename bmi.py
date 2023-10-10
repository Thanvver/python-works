# BMI
# body mass index
# bmi=(weight in kg)/height in meter square
weight_kg=int(input("enter weight in kg:"))
height_cm=int(input("enter height in cm:"))
#cm=>meter cm/100
height_m=height_cm/100
bmi=weight_kg//height_m**2
print("bmi is",bmi)
if(bmi<20):
        print("under weight")
elif(bmi<25):
        print("normal weight")
elif(bmi<30):
        print("pre obesity")
else:
        print("obesity")