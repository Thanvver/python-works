from re import*

text="aaabbaaac"

# pattern="a+" #one or more occurance of "a"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())


# pattern="a*" #zero or more occurance of "a"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

pattern="a{1,2}" #min,max
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())