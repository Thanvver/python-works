list1=[10,11,12,13,16]
list2=[12,13,14,20,21]
# out=[]

# for n1 in list1:
#     if n1 in list2:
#         print("common",n1)


# list1.sort()
# list2.sort()
# p1,p2=0,0

# while (p1<len(list1)and p2<len(list2)):
#     if list1[p1]==list2[p2]:
#         print("commom",list2[p2])
#         p2+=1
#     elif list1[p1]<list2[p2]:
#         p1+=1
#     else:
#         p2+=1

limit=int(input("enter length of list:"))

list=[]

for i in range(limit):
        element=int(input("enter a number:"))
        list.append(element)
print(list)
