# DailyTasks

=============DATE : 24th Jan==============
1. Data type : Python sets the variable type based on the value that is assigned to it. Unlike more riggers languages, Python will change the variable type if the variable       value is set to another value.
  var = 123 # This will create a number integer assignment
  var = 'john' # the `var` variable is now a string type.
2. Types of data type : 

  a. Numbers
      Most of the time Python will do variable conversion automatically. You can also use Python conversion functions (int(), long(), float(), complex()) to convert data from         one type to another. In addition, the type function returns information about how your data is stored within a variable.
      
      print(type(message))  # This will return a string
      print(type(n))  # This will return an integer
      print(type(pi))  # This will return a float
      
      Eg.
      message = "Good morning"
      num = 85
      pi = 3.14159
     
  b. String : String is a list of characters represented within single/double/triple quotes . Strings are immuable . 
      Strings can be accessed as a whole string, or a substring of the complete variable using brackets ‘[]’
      var1 = 'Hello World!'
      print var1[0]   # `H`
      print var1[1:5] #'ello `
  
  c. List : A list can contain a series of values. List variables are declared by using brackets [ ] following the variable name.
      A = [ ] # This is a blank list variable
      B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
      C = [2, 4, 'john'] # lists can contain different variable types.
      length = len(B)  => 3
      
  d. Tuple
      Tuples are a group of values like a list and are manipulated in similar ways.
      
  e. Dictionary 
      Dictionaries in Python are lists of Key:Value pairs.
      
3. Single line comment[#] , multiline comment ['''' '''/ """ """]
4. Docstring : Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.
    It’s specified in source code that is used, like a comment, to document a specific segment of code.
    
    def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    return None
  
    print("Using __doc__:")
    print(my_function.__doc__)
    
    => Using __doc__:
      Demonstrates triple double quotes
      docstrings and does nothing really.
      
      
=============DATE : 25th Jan==============

1. compiler vs interpreter : Compliers and interpreters are programs that help convert the **high level language** (Source Code) into **machine codes** to be understood by the    computers. Compiler scans the entire program and translates the **whole of it into machine code at once**. An interpreter takes very less time to analyze the source code        line by line.
2. python 2 and python 3 : Python 3 is more in-demand and includes a typing system. Python 2 is outdated and uses an older syntax
--------------------------------------------
      [Division operator]
      print 7 / 5
      print -7 / 5	
      Output in Python 2.x
      1
      -2
      Output in Python 3.x :
      1.4
      -1.4
      -------------------------------------------
      [print function]
      print 'Hello, Geeks'      # Python 3.x doesn't support 
      print('Hope You like these facts')
      ---------------------------------------------
      [__future__ module:]
      This is basically not a difference between the two versions, but a useful thing to mention here. The idea of the __future__ module is to help migrate to Python 3.x. 
      If we are planning to have Python 3.x support in our 2.x code, we can use _future_ imports in our code.
      from __future__ import division 
      print 7 / 5   => 1.4
      print -7 / 5  =>-1.4
---------------------------------------------
3. study in detail about print function
      print(object(s), sep=separator, end=end, file=file, flush=flush)
      
      Parameter	Description
      1. object(s)	      ----> Any object, and as many as you like. Will be converted to string before printed
          print("Hello", "how are you?")   => Hello how are you?
          x = ("apple", "banana", "cherry")
          print(x)  => ('apple', 'banana', 'cherry')
          # sample python objects
              list = [1,2,3]
              tuple = ("A","B")
              string = "Geeksforgeeks"

              # printing the objects
              print(list,tuple,string)  => [1, 2, 3] ('A', 'B') Geeksforgeeks
      2. sep='separator'	----> Optional. Specify how to separate the objects, if there is more than one. Default is ' '
          print("Hello", "how are you?", sep="---") => Hello---how are you?
      3. end='end'	      ----> Optional. Specify what to print at the end. Default is '\n' (line feed)
            # sample python objects
            list = [1,2,3]
            tuple = ("A","B")
            string = "Geeksforgeeks"
            # printing the objects
            print(list,tuple,string, end="<<..>>")   => [1, 2, 3] ('A', 'B') Geeksforgeeks<<..>>
            
      4. file	Optional. ----> An object with a write method. Default is sys.stdout
            # open and read the file
            my_file = open("geeksforgeeks.txt","r")
            # print the contentts of the file
            print(my_file.read())
            
      5. flush	Optional. ----> A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

4. study in detail about input function
      In Python, we use input() function to take input from the user. Whatever you enter as input, the input function converts it into a string. If you enter an integer value         still input() function convert it into a string.
      string = input()
      print(string)  => geeksforgeeks
        # Taking input from the user
        name = input("Enter your name")
        # Output
        print("Hello", name)
        => Enter your name:ankit rai
        Hello ankit rai
        
        # Taking input from the user as integer
        num = int(input("Enter a number:"))
        add = num + 1
        # Output
        print(add)
        Enter a number:15
        16

        # Taking input from the user as float
        num =float(input("Enter number "))
        add = num + 1
        # output
        print(add)
        => Enter number 5
        6.0

        # Taking input from the user as list
        li =list(input("Enter number "))
        # output
        print(li)
        Enter number 12345
        ['1', '2', '3', '4', '5']

        # Taking input from the user as tuple
        num =tuple(input("Enter number "))
        # output
        print(num)
        =>Enter number 123
        ('1', '2', '3')
        
=============DATE : 25th Jan==============       
Data type conversion (int to float,bool,string)

[Implicit Type Conversion]
a=5     -> int
b=1.0  -> float
c=a//b
c=5.0  -> float 
--------------------------------

[Explicit Type Conversion]

Converting Numbers to String

a = 10
 
 Converting number to string
s = str(a)
print(s)
print(type(s))

10
<class 'str'>
-----------------------------------
# Converting String to Number

s = '50'
 
# Converting to int
n = int(s)
print(n)
print(type(n))
 
# Converting to float
f = float(s)
print(f)
print(type(f))

=>50
<class 'int'>
50.0
<class 'float'>

# Floating Point to Integer

f = 10.0
 
# Converting to integer
n = int(f)
print(n)
print(type(n))

10
<class 'int'>


# Integer to Floating Point
n = 10
 
# Converting to float
f = float(n)
print(f)
print(type(f))

10.0
<class 'float'>

# Type conversion between Tuple and List

# Python program to demonstrate
# type conversion between list
# and tuples
 
t = (1, 2, 3, 4)
l = [5, 6, 7, 8]
 
# Converting to tuple
T = tuple(l)
print(T)
print(type(T))
 
# Converting to list
L = list(t)
print(L)
print(type(L))

(5, 6, 7, 8)
<class 'tuple'>
[1, 2, 3, 4]
<class 'list'>



