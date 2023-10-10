text="race"
out="care"

if (sorted(text)==sorted(out)):
    print("anagram")
else:
    print("not anagram")

#q1."malayalam" palindrome or not

text="thanveer"
count=len(text)-1
p_str=""
for i in range(count,-1,-1):
    p_str+=text[i]
print("palindrome" if text==p_str else "not palindrome")

