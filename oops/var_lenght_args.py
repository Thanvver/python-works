def product(*args):
    res=1
    for n in args:
        res*=n
    print(res)

product(10,23,14)
product(2,3,4,5,6)


def greetings(**kwargs): #(kwargs-keyword arguments)
    print(f"hello {kwargs.get('msg')} app user {kwargs.get('user_name')}")
greetings(msg="good morning",user_name="geo")

def dispatch_order(**kwargs):
    print(f"hello user {kwargs.get('name')} you order {kwargs.get('code')} {kwargs.get('item')} is ready to {kwargs.get('status')}")
dispatch_order(item="ucb shirt",code="123bc",status="deliver",name="vijay")
