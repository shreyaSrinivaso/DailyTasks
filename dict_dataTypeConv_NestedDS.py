#Task2
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
#Extract
#science
print(a[4][3][9:]) 
#computer
print(a[4][3][:8])

#output:
# science
# Computer
#-----------------------------------------------------------
#Task3
a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
#Extract
#666
print(a[4][4])
#201
print(a[4][3][0])
#102
print(a[4][1])
#999
print(a[4][3][2])
#777
print(a[4][5])
#output
# 666
# 201
# 102
# [999]
# 777
#-----------------------------------------------------------
#Task4:
a = [2,3,"python","hello",4,5,0]  
#Extract
#ll
print(a[3][2:4])
#thon
print(a[2][2:])
# output
# ll
# thon
#-----------------------------------------------------------
#Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

#Output Prediction 

print(Li1[5][0])
print(Li1[5][6])
print(Li1[5][-2])
print(Li1[5][7])
print(Li1[6])
print(Li1[5][5][1])
print(Li1[-2][-1])
print(Li1[-2][2:4])
# output
# 11
# 6666
# 6666
# 7777
# 7777
# 222
# 7777
# [33, 44]
#-----------------------------------------------------------
#Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

#py
print(a[1][3][:2])
#ello
print(a[2][10][1:])
#en
print(a[2][40][3:5])
#zoo
print(a[40][1][:3])
#Bot
print(a[40][2][:3])
# output
# py
# ello
# en
# zoo
# Bot
#-----------------------------------------------------------
#Task 7
#Covert below two lists in to a dictionary

a=[1,2,3,4,5]
b=["python","cpp","c","java","php"]

#print(dict(zip(key,value))
dict1=dict(zip(a,b))
print(dict1)
# output
# {1: 'python', 2: 'cpp', 3: 'c', 4: 'java', 5: 'php'}
#-----------------------------------------------------------
#Task8:
#Convert below set in to a list
a={5,4,3,6,2,7,1}
li=list(a)
print(li)
# output
# [1, 2, 3, 4, 5, 6, 7]
#-----------------------------------------------------------
#Task9:
#Remove duplicates from below list
a=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
rem=list(set(a))
print(rem)
# output
# [1, 2, 3, 4, 5, 6, 7]
#-----------------------------------------------------------
#Task10:
#Convert below one to tuple
a=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
tu1=tuple(a)
print(tu1)
print(type(tu1))
# output
# (5, 4, 3, 6, 2, 7, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 5)
# <class 'tuple'>