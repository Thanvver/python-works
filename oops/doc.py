def swap_num(fn):

    def inner_fun(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun

@swap_num
def sub(n1,n2):
    return n1-n2

@swap_num
def div(n1,n2):
    return n1/n2

print(sub(5,10))