text="python is a programming language"

vowels=("a","e","i","o","u")

word=text.split(" ")

for w in word:
    if w.casefold().startswith(vowels):
        print(w)