arr=[5,2,5,3,2,5]

arr.sort()
duplicate_list=[]

for i in range(0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]
  
    if current==next:
        if current not in duplicate_list:
            duplicate_list.append(current)
print(duplicate_list)


