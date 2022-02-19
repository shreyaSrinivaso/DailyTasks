# Write function to concatenate three strings
def concat_strings(x,y,z):
    return x+y+z

print(concat_strings("Hi!, ","My name is ","Shreya Srinivas"))

# Write a function multiply three different integers and return a int
def mul_3nos(x,y,z):
    return x*y*z


a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
c=int(input("Enter num 3: "))
print(mul_3nos(a,b,c))

# Write a function to return middle char of the string
def middleChar(x):
    mid=len(x)//2
    listString=list(x)
    return listString[mid]

print(middleChar("ABCDE"))

