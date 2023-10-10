student={"name":"thanveer","course":"django","is placed":True,"salary":24000}

for k in student.keys(): # to print keys
    print(k)

for v in student.values(): # to print values
    print(v)

for k,v in student.items(): # to print both key and values
    print(k,v)

print(student.get("name")) # to get the value of the selected key

student.pop("name") # to remove selected key and value
print(student)