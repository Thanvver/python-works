st1={10,20,30}
st2={30,20,50}
# st=set()-can defined this way too


# duplicates not allowed
# indexing not supported
# can be updated

# add()-method
# st1.add(40)
# print(st1)

# union()-method
# union_set=st1.union(st2)
# print(union_set)

#intersection()-method
# int_method=st1.intersection(st2)
# print(int_method)

#difference()-method
# diff_method=st1.difference(st2)
# print(diff_method)

# remove()-method
# st1.remove(20)
# print(st1)

#discard()-method(same as remove method but wont return error if try to remove an object not in set)
# st2.discard(50)
# print(st2)

#pop()-method(remove a random object)
# st1.pop()
# st2.pop()
# print(st1)
# print(st2)

# symmetric difference()-method
sym_diff=st1.symmetric_difference(st2)
print(sym_diff)