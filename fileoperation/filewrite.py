fw=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\write.txt","w")
fw.write("hello there")

fw=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\year.txt","w")

for y in range(1800,2025):
    fw.write(str(y)+"\n")

# read from years.txt
# write leapyears into leapyear.txt
# write nonleapyer into nonlpyr.txt

