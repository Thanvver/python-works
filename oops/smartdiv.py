def swap_num(fn):

    def inner_fun(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun

def smart_div(fn):

    def wrapper(n1,n2):
        if n2==0:
            print("division not possible by zero")
            return
        return fn(n1,n2)
    return wrapper

@swap_num
@smart_div
def div(n1,n2):
    return n1/n2
print(div(5,10))

