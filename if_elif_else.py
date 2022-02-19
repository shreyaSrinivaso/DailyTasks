#Feb 15

#Task 1
#hackerrank Write a function : DONE

#Task 2
#hackerrank Python If-Else : DONE

#TASK 3:
#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number


n = int(input("enter a number : "))

if(n%3==0 and n%5==0):
    print("Fizzbuzz")
elif(n%5 == 0):
    print("Buzz")
elif(n%3==0):
    print("Fizz")
else:
    print("Invalid Number")
    
#output:
#enter a number : 3
#Fizz
#enter a number : 5
#Buzz
#enter a number : 15
#FizzBuzz
#enter a number : 32
#Invalid Number


#===============================================================

#TASK 4
#Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark
#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL
n = int(input("Enter your marks:"))

if(0<=n<=100):
    print("Valid num")
    if(n>=50):
        print("PASS")
        if(100>=n>=90):
            print("Grade = A")
        if(89>=n>=80):
            print("Grade = B")
        if(79>=n>=70):
            print("Grade = C")
        if(69>=n>=60):
            print("Grade = D")
        if(59>=n>=50):
            print("Grade = E")
    elif(49>=n>=0):
            print("FAIL!!!")
else:
    print("Invalid num !! Error: Enter num between (0 -100) ")
    
#output
#Enter your marks:455
#Invalid num !! Error: Enter num between (0 -100) 

#Enter your marks:56
#Valid num
#PASS
#Grade = E

#===================================================================

#TASK 5:
#collect three marks from user
#calculate mark1 + mark2 + mark3 / 100

#if calculate > 90 ===> Grade A
#if calculate > 75 ==> Grade B
#calculate > 50  ==> grade C
#Other wise ===> Grade D
    
M1=int(input("Enter Mark 1 : "))
M2=int(input("Enter Mark 2 : "))
M3=int(input("Enter Mark 3 : "))

totalMarks=M1+M2+M3

if(totalMarks>=90):
    print("GRADE: A")
elif(90>totalMarks>=75):
    print("GRADE: B")
elif(75>totalMarks>=50):
    print("GRADE: C")
else:
    print("GRADE D")
    
#OUTPUT:
#Enter Mark 1 : 40
#Enter Mark 2 : 50
#Enter Mark 3 : 6
#GRADE: A
#===================================================================

