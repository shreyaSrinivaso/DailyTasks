#Empty tuples
t1=()
print(type(t1))
t1=tuple()
print(type(t1))

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)
#Find the common elements between two tuples

for i in t1:  #1
    for j in t2:
        if(i == j):
            print(i)

    
#Concatenate both tuples and remove duplicates from tuple    
t1=(1,4,5,6,7,8)
t2=(5,6,7,8,9)
t3=t1+t2
print(t3)
removeDups=print(set(t3))

#Find the index value of 9 (after concatenation)

t3=(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
index=print("index of 9 is",t3.index(9))


#output:
# <class 'tuple'>
# <class 'tuple'>
# 5
# 6
# 7
# 8
# (1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
# {1, 4, 5, 6, 7, 8, 9}
# index of 9 is 10