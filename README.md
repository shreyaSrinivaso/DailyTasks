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
=================================================================================================================
