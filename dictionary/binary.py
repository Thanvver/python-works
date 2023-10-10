# linear searching
# binary searching
# word count
# first recursive
# sort
# bubble sort
# quick sort
# merge sort
# dfs(depth first search)
# bfs(breadth first search)
# dijkstra algorithm

list=[12,14,16,18,20]
list.sort()
element=20
low=0
upp=len(list)-1
is_found=False

while(low<=upp):
    mid=(low+upp)//2

    if element==list[mid]:
        is_found=True
        break
    elif element<list[mid]:
        upp=mid-1
    elif element>list[mid]:
        low=mid+1
print(is_found)