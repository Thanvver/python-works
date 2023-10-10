# name="THanveer"
# print(name.casefold()) #upper to lower case
# print(name.capitalize()) #first letter captial only
# print(name.count("e")) #count specific alphabet
# print(name.index("r")) #position of alphabet
# print(name.strip("T")) #remove first alphabet
# print(name.rstrip("r")) #remove right side first alphabet
# print(name.isalpha()) #alpabet=true or else false,no space allowed
# print(name.isalnum()) #both alphabet and number=true or else false,no space and special characters allowed
# print(name.isdigit()) #digit=true orelse false,no space allowed

name="python is a programming language"
words=name.split(" ")
for w in words:
    print(w)

