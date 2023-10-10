f=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\data.txt","r")
# for line in f:
#     print(line)

words=[line.rstrip("\n") for line in f]
print(words)