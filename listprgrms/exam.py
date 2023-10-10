# C,

text="AB CD AB CD AB"
words=text.split(" ")

wc={}

for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)

# B,

text="ABABC"

wc={}

for ch in text:
     if ch in wc:
         wc[ch]+=1
     else:
         wc[ch]=1

for k,v in wc.items():
     if v==1:
         print(k)



# D,

data=[
    
     {"id":100,"name":"python","price":350},
     {"id":101,"name":"java","price":450},
     {"id":102,"name":"django","price":1300},
     {"id":103,"name":"Html","price":1000},
     {"id":104,"name":"Bootstrap","price":300},
]
# a
booknames=[i.get("name") for i in data]
print(booknames)
# b
price=[i.get("price") for i in data if i.get("name")=="java"]
print(price)
# c
Html_data=[i for i in data if i.get("name")=="Html"][0]
print(Html_data)

Html_data["price"]=600
print(Html_data)


     
    
