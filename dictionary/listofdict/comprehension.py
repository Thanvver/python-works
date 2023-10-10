list=[4,5,6,7,8,2,1]

cubes=[n**3 for n in list]
print(cubes)

evens=[n for n in list if n%2==0]

odds=[n for n in list if n%2!=0]

num_gtfive=[n for n in list if n>=5]

print(evens)
print(odds)
print(num_gtfive)