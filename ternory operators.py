#num=10

#normal;

#if num>0:
#print("+ve")
#else:
#print("-ve")

#ternory;

#result="+ve" if num>0 else"-ve"
#print(result)

#odd even

#result="even" if num%2==0 else"odd"
#print(result)

#num1=10
#um2=20

#result=num1 if num1>num2 else num2
#print(result)

#num=int(input("enter a number:"))

#result=num+1 if num>5 else num-1
#print(result)

#n1=int(input("enter a number1:"))
#n2=int(input("enter a number2:"))

#result=n1-n2 if n1>n2 else n2-n1
#print(result)

#num=int(input("enter a number:"))

#result="+ve" if num>0 else"-ve" if num<0 else"zero"
#print(result)

num=int(input("enter a number:"))

result=num+1 if num>5 else num-1 if num<5 else 5
print(result)