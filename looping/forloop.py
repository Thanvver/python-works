#for i in range(1,10):
#    print(i)

#10 to 1
#for i in range(10,1,-1):
#    print(i)


low_limit=int(input("enter lower limit:"))
upp_limit=int(input("enter upper limit:"))

#for i in range(low_limit,upp_limit):
#    print(i)

#print all even numbers from this low_limit to upp_limit

for i in range(low_limit,upp_limit):
    if (i&2==0):
        print(i) 

# 10 15 cde 11 ab 13 14 fgh


