# s1="python"
# s2="java"
# #output ===>jythonpava64hv
s1="python"
s2="java"
print(s2[0]+s1[1:6]+s1[0]+s2[1:]+str(len(s1))+str(len(s2))+s1[3]+s2[2])
#output ===> jythonpava64hv

#=============================================================================
# string1: maths
# string2: science
# output ===> sathsmcience57te
s1="maths"
s2="science"
print(s2[0]+s1[1:4]+s2[0]+s1[0]+s2[1:]+str(len(s1))+str(len(s2))+s1[2]+s2[3])
# output ===> sathsmcience57te


#=============================================================================
# Collect two strings from user

# string1: wikipedia
# string2: typescript

# output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
# (ord , chr)

s1="wikipedia"
s2="typescript"

mid1=str(s1[(len(s1)//2)])
mid2=str(s2[(len(s2)//2)])

print(ord(mid1))
print(ord(mid2))
print(ord(mid1)+ord(mid2))

#output:
#112
#99
#211

#=============================================================================
#collect one string from user:

#string: computer
#output: c6r

#string: mathematics
#output: m9s

string=input("Enter string:")
print(string[0]+str(len(string)-2)+string[-1])
# string: computer
# output: c6r
#output:
#Enter string: computer
#c6r