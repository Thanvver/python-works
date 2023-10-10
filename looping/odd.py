# print all odd numbers within a given range(end)

#start=1
#end=int(input("enter ending number:"))
#while(start<=end):
#    print(start)
#    start+=2 

# another method

#while(start<=end):
 #   if(start%2!=0):
  #      print(start)
   # start+=1

#print all numbers which are divisble by 3 and 5 upto given range (start,end-user)

num1=int(input("enter first number:"))
num2=int(input("enter end number:"))

while(num1<=num2):
   if(num1%3==0 and num1%5==0):
      print(num1)
   num1+=1



