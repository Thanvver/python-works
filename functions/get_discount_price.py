def get_discount_price(actual_price,discount):
    selling_price=actual_price-(actual_price*discount/100)
    return selling_price
print(get_discount_price(50,20))