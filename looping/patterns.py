# for row in range(1,4):
#     for column in range(1,4):
#         print("#",end="\t")
#     print()


# for row in range(1,4):
#         for column in range(1,4):
#             print(row,end="\t")
#         print()

# for row in range(1,4):
#         for column in range(row):
#             print("#",end="\t")
#         print()


# for row in range(1,4):
#         for column in range(row):
#             print(column+1,end="\t")
#         print()


# for row in range(1,6):
#         for column in range(row):
#             val=column+1
#             if val%2==0:
#                   print("#",end="\t")
#             else:
#                   print(val,end="\t")
            
#         print()


# for row in range(4,0,-1):
#     for column in range(row):
#         print("#",end="\t")
#     print()


# for row in range(1,7):
#     for column in range(row):

#         print("#",end="\t")
#     print()

for row in range(1,7):
    for sp in range(7-row,1,-1):
         print(end=" ")
    for st in range(row):
         print("*",end=" ")
    print()
    
    







