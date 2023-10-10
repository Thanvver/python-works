from re import *

text="abaabbaab"
pattern="aa"

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

# text="python @ 123"

# pattern="[a-z]"
# pattern="[A-Z]"
# pattern="[a-zA-Z]"
# pattern="[0-9]"
# pattern="[a-zA-Z0-9]"

# pattern="[^a-zA-Z0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="\d" #[0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="\D" #except[0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

# pattern="\w" #[a-zA-Z0-9]
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())

pattern="\W" #except[^a-zA-Z0-9]
matcher=finditer(pattern,text)
for m in matcher:
 print(m.start(),m.group())