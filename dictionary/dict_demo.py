mobile={"name":"iphone11pro","brand":"apple","price":45000,"color":"white"}
print(mobile["brand"])
print(mobile["name"])
print(mobile["price"])
print(mobile["color"])

mobile["storage"]="256gb"
print(mobile)

if "offer" in mobile:
    print("exist")
else:
    print("not exist")

if "offer" in mobile:
    mobile["offer"]+=50
else:
    mobile["offer"]=50
print(mobile)