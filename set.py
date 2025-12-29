#homgeneous set
s1 = {'sasmit','samir','jack'}
print(s1)
print(type(s1))

#heterogeneous set
s2 = {'hello', True, 100 }
print(s2)
print(type(s2))

dup_set = {1,1,2,2,3,3,4,4,}
print(dup_set)


empty_set = set()
print(empty_set)
print(type(empty_set))  #{}creates a dictionary no a set

empty_set.add(4)
print(empty_set)
empty_set.update({1,2,3})
print(empty_set)

#remove in set
s = ({0,6,3,4,8,1,2,5})
s.remove(2)
print(s)

#discard in set
s.discard(4)
print(s)

#pop in set
removed = s.pop()
print("removed: ", removed)
print(s)



A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))

print(A|B) #union
print(A&B) #intersection
print(A-B) #difference
print(A^B) #symmetric difference

C = {1,2}
D = {1,2,3,4}

print(C.issubset(D))
print(D.issubset(C))
print(C.issubset({5,6}))

#frozen set
fs = frozenset({1,2,3})
print(fs[1])
fs = set()
fs.add(5)
print(fs)