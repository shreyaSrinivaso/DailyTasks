#==========================================================
#TASK 1:
#Using Range function  print multiples of 5 from 0 to 75
for i in range(0,76,5):
    print(i)

#Using Range function  print multiples of 8 from 0 to 72
for i in range(0,73,8):
    print(i)

#Using Range function  print multiples of 5 from 75 to 0
for i in reversed(range(0,76,5)):
    print(i)

#Using Range function  print multiples of 8 from 96 to 72
for i in reversed(range(72,97,8)):
    print(i)

#==========================================================
#TASK 2
# Get a dynamic list from user

numOfElements= int(input("Enter num of elements:"))
L1=[]

for i in range(numOfElements):
    L1.append(i)

print(L1)

#==========================================================
#TASK 3

# Get a dynamic dictionary from user
numOfElements= int(input("Enter num of elements:"))
D1={}

for i in range(numOfElements):
    D1[i]=[i]
print(D1)

#==========================================================
#TASK 4
# Get two integers from user
# print multiples of 8 between them

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

for i in range(a,b):
    if(i%8 == 0):
        print(i)

#output:
#Enter number 1:2
#Enter number 2:88
#8
#16
#24
#32
#40
#48
#56
#64
#72
#80
#==========================================================
#TASK 5
# Input:
# Li1 = [3,4,5,2,7,8,9,10]

# Output:
# Li_odd = [3,5,7,9]
# Li_even = [4,2,8,10]

#Li1 = [3,4,5,2,7,8,9,10]

L1 = [3,4,5,2,7,8,9,10]
L_odd = []
L_even = []
for i in L1:
    if i%2 == 0:
        L_even.append(i)
    else:
        L_odd.append(i)

print(L_even)
print(L_odd)

#OUTPUT:
# [4, 2, 8, 10]
# [3, 5, 7, 9]
#==========================================================
#TASK 6
# Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
# Output:
# neg_LI = [-1,-7,-3]
# pos_LI = []
# Zeros = []

# Numeber of postivie ele: 7
# Number nega: 3
# Number of zeros: 2
L1=[-1,-7,8,10,20,21,17,28,-3,0,0]
neg_LI=[]
pos_LI=[]
zero_LI=[]
for i in L1:
    if(i<0):
        neg_LI.append(i)
    elif(i>0):
        pos_LI.append(i)
    else:
        zero_LI.append(i)
print("negetive list: ",neg_LI)        
print("positive list: ",pos_LI)
print("neutral list: ",zero_LI)

print("No of negetive elements:",len(neg_LI))
print("No of positive elements:",len(pos_LI))
print("No of neutral elements:",len(zero_LI))

#output:
# negetive list:  [-1, -7, -3]
# positive list:  [8, 10, 20, 21, 17, 28]
# neutral list:  [0, 0]
# No of negetive elements: 3
# No of positive elements: 6
# No of neutral elements: 2

#==========================================================
#TASK 7
print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))

# Output:
# [0, 1, 2, 3, 4]
# [1, 2, 3, 4]
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [-5, -2, 1, 4]
# [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# [10, 8, 6, 4, 2]
