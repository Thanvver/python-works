# linear searching


list=[12,14,16,18,20]

element=16

i=0
stop=len(list)
is_found=False

while(i<stop):
    cur_value=list[i]
    if cur_value==element:
        is_found=True
        break
    i+=1
print(is_found)

