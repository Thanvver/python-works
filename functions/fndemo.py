# def add(n1,n2):
#     res=n1+n2
#     return res
# print(add(40,50))


# def cube(n):
#     res=n**3
#     return res
# print(cube(3))

# def largest(n1,n2):
#     if n1>n2:
#         return n1
#     else:
#         return n2
# print(largest(20,30))


# def sub(n1,n2):
#     return n1-n2
# print(sub(2,3))

# def smart_sub(n1,n2):
#     if n1>n2:
#         return n1-n2
#     else:
#         return n2-n1
# print(smart_sub(4,5))
# print(smart_sub(5,4))

# def oddeven(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(oddeven(5))

def hcf(num1,num2):
    res=1
    sm_num=num1 if num1<num2 else num2
    for i in range(1,sm_num-1):
        if num1%i==0 and num2%i==0:
            res=i
    return res
print(hcf(18,24))
    
def lcm(num1,num2):
    gcd=hcf(num1,num2)
    res=(num1*num2)/gcd

    return res
print(lcm(18,24))

def least_common_multiple(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True
    while(flag):
        if max%n1==0 and max%n2==0:
            print(f"lcm of {n1},{n2} is {max}")
            break
        else:
            max+=1
least_common_multiple(30,25)

