year=int(input("enter a year:"))
if year %100==0 and year %400==0:
    print("leap year")
elif year %100!=0 and year %4==0:
    print("leap year")

else:
    print("not leap year")

    # case1
    # if year is century year that must be divicible by 400

    #case2
    # if year is not a century that must be / 4