text="abbccde"

# wc={}
# dup_list=[]

# for ch in text:
#     if ch in wc:
#         dup_list.append(ch)
#     else:
#         wc[ch]=1

# print(dup_list[1])

#another method


non_dup_list=[]
dup_list=[]

for ch in text:
    if ch in non_dup_list:
        dup_list.append(ch)
    else:
        non_dup_list.append(ch)

print(dup_list[1])