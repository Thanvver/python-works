f_read=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\year.txt")
l_write=open("C:\\Users\\thanveer\\OneDrive\\Desktop\\luminar\\fileoperation\\leapyear.txt","w")

# for year in f_read:
#     year=int(year)

#     if(year %100==0) and (year %400==0):
#         l_write.write(str(year)+"\n")
#     elif(year %100!=0) and (year%4==0):
#         l_write.write(str(year)+"\n")

[l_write.write(str(year)+"\n") for year in f_read if int(year.rstrip("\n"))%4==0]