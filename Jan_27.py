print("int to float,bool,string")
print("------------------------")
a=10

Float=float(a)
print(Float)
print("Float:",type(Float))

Bool=bool(a)
print(Bool)
print("Float:",type(Bool))

String = str(a)
print(String)
print("String:",type(String))

print("float to int,bool,string")
print("------------------------")
b=10.50

Int=int(b)
print(Int)
print("Int:",type(Int))

Bool=bool(b)
print(Bool)
print("Bool:",type(Bool))

String = str(b)
print(String)
print("String:",type(String))

print("bool to int,float,string")
print("------------------------")
c=True

Int=int(c)
print(Int)
print("Int:",type(Int))

Float=float(c)
print(Float)
print("Float:",type(Float))

String = str(c)
print(String)
print("String:",type(String))

print("string to int,float,bool")
print("------------------------")
d="Shreya"

# Int=int(d)
# print(Int)
# print("Int:",type(Int))   #ValueError: invalid literal for int() with base 10: 'Shreya'

# Float=float(d)
# print(Float)
# print("Float:",type(Float))  #ValueError: could not convert string to float: 'Shreya'

Bool = bool(d)
print(Bool)
print("String:",type(Bool))

print("The only conversion which is not possible is from *string to int* and *string to float* ")