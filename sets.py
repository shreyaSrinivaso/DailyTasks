#Create two empty sets
s={} #not possible 
print(type(s))
s1=set()
print(type(s1))
s2=set()
print(type(s2))

#update set1 with 7,8,9,1,2,3,4,5,0
set2={7,8,9,1,2,3,4,5,0}
s1.update(set2)
print(s1)

set3={4,5,6,0}
s2.update(set3)
print(s2)

#check whether set2 is subset of set1 or no ?

print(s2.issubset(s1))

#check whether both have common elements are no ?

common=s2.intersection(s1)
print(common)

#remove 8 from set 1 and set 2 ==> find the inferences

rem8=s1.remove(8)
print(s1)

# rem8=s2.remove(8)
# print(s2)


#discard 0 from set1 and set2 
rem0=s1.remove(0)
print(s1)
rem0=s2.remove(0)
print(s2)


#find collection of both sets ===> set1 and set2
s1={0, 1, 2, 3, 4, 5, 7, 8, 9}
s2={0, 4, 5, 6,11,18}
U=s1.union(s2)
print(U)

#output
# <class 'dict'>
# <class 'set'>
# <class 'set'>
# {0, 1, 2, 3, 4, 5, 7, 8, 9}
# {0, 4, 5, 6}
# False
# {0, 4, 5}
# {0, 1, 2, 3, 4, 5, 7, 9}
# {1, 2, 3, 4, 5, 7, 9}
# {4, 5, 6}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 18}