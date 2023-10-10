text="carrot"

text_count={}

for ch in text:
    if ch in text_count:
        text_count[ch]+=1
    else:
        text_count[ch]=1
        
print(text_count)