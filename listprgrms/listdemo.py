# films=["vigathakumaran","marthandavarma","balan","nirmala"]
# print(films[0])

# for f in films:
#     print(f)

expenses=[12000,13000,14000,11000,25000,28000,21000]

#1.print march month expenses
#2.print all expenses
#3.print costly expense
#4.print expenses > than 16000

# 1.
# print(expenses[2])
# 2.
# for e in expenses:
#      print(e)
# 4.
for e in expenses:
     if e>16000:
      print(e) 

# 3.
# max_exp=0
# for e in expenses:
#      if e>max_exp:
#           max_exp=e
# print(max_exp)

# min_exp=expenses[0]
# for e in expenses:
#      if e<min_exp:
#           max_exp=e
# print(min_exp)

# max_exp=max(expenses)
# print(max_exp)

srt_exp=sorted(expenses,reverse=False)
print(srt_exp)
desc_exp=sorted(expenses,reverse=True)
print(desc_exp)
