# source_word="chicken"
# target_word="hen"

# source_list=[]
# kangaroo_word=""

# for ch in source_word:
#     source_list.append(ch)

# for ch in target_word:
#     if ch in source_list:
#         source_list.remove(ch)
#         kangaroo_word+=ch
# print(kangaroo_word==target_word)

source_word="decreases"
target_word="dress"

wc={}

for ch in source_word:  
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1
    else:
        print("not kangaroo word")
        break 
