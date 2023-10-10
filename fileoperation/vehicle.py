f=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\numbers.txt")

all_num=[line.rstrip("\n") for line in f]
print(all_num)

kerala_reg=[num for num in all_num if num.startswith("kl")]
print(kerala_reg)