text="abccdb"

wc={}

for ch in text:
    if ch in wc:
        print(ch,"is the recursive number")
        break
    else:
        wc[ch]=1

