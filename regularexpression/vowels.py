from re import*

text="goodmorning #sachin"
# pattern="[aeiou]"

# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

#consonants
pattern="[^aeiou\W\d]"

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())


