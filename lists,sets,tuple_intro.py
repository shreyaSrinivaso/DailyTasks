#Create an empty list (two ways)

li1=[]
li2=list()

#Concatenate with [5,6,7,8]
li3=[5,6,7,8]
print(li1+li3)

#add 8,9,1,5,6,7,8,1 elements to that list
print(li1+li3+[8,9,1,5,6,7,8,1])

#Find frequency of 8 (count)
li4=li1+li3+[8,9,1,5,6,7,8,1]
print(li4.count(8))
print("\n")
#find sum (List)
li1 = [5,6,7,8,1]
i=0
Sum=0
for i in [5,6,7,8,1]:
    Sum=Sum+i
print("sum is :{}".format(Sum))
print("\n")
#find mean (List)
mean=Sum/len(li1)
print("mean is :",mean)
print("\n")
#find median (List)
# Median is the middle value of a set of data. To determine the median 
#value in a sequence of numbers, the numbers must first be arranged in ascending order. 
# If there is an odd amount of numbers, the median value is the number 
#that is in the middle, with the same amount of numbers below and above.
# If there is an even amount of numbers in the list, the median is 
#the average of the two middle values.

li1 = [5,6,7,8,1,2,9]
li1.sort()
print("sorted list:",li1)
length=len(li1)
mid=length//2
mid1=mid-1

if(length%2 != 0):
    median=li1[mid]
    print("median of odd elements :{}".format(median))
else:
    median=(li1[mid]+li1[mid1])/2
    print("median of even elements :{}".format(median))
print("\n")    
#remove duplicates from list and give output in the format of tuple  
li1 = [1,2,3,1,3,2,4,5,6,5] 
sets=set(li1)
print("list:",li1)
print("list after removing duplicates",sets)
Tuple=tuple(sets)
print("Tuple format output:",Tuple,type(Tuple))

#output:
# [5, 6, 7, 8]
# [5, 6, 7, 8, 8, 9, 1, 5, 6, 7, 8, 1]
# 3


# sum is :27


# mean is : 5.4


# sorted list: [1, 2, 5, 6, 7, 8, 9]
# median of odd elements :6


# list: [1, 2, 3, 1, 3, 2, 4, 5, 6, 5]
# list after removing duplicates {1, 2, 3, 4, 5, 6}
# Tuple format output: (1, 2, 3, 4, 5, 6) <class 'tuple'>