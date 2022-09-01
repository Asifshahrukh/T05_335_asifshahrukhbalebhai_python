# Introduction
# 1. What is python?
# Python is a general purpose, high level, interpreted, object-oriented programming language used for a
# wide variety of applications.

# 2. What are the features of python?
# * Python is easy and simple to learn and code
# * Python is Interpreted
#   It is known as interpreted language because Python interprets the code line by line, which means the source code of
#   python program is converted intp bytecode that is then executed by python virtual machine.
# * It is free and accessible.
# * It is portable which means the code written in python can be moved to other system like windows, linux, MacOS
# * It has a broad and extensive library.
# * It is dynamically typed language which means in other languages we have to give data type while assinging a value
#     to the variable but in python we dont have to define a variable with any data type.


# 3. Advantages and disadvantages of Python?
#  Advantages of Python
#  * It is very easy to learn and code.
#  * It has an extensive and broad library.
#  *  Python is a very productive language. The simple nature of Python helps the developers to concentrate on solving
#     the issues in it.
#  * Its has a vast and an extensive library.

#  Disadvantages of Python
#  * Because of its elementary programming language, users faces difficulty in working with other programming languages.
#  * It is a time-consuming language. It has a low execution speed.
#  * There are many issues with the design of the language which gets displayed only during run time.
#  * It is not suited for memory extensive programs and mobile applications.

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


#  Variable
# 1. What is a variable?
#    Variable is a name which is used to refer memory location of value. Variable is known as identifier and it holds
#    the value. In python we don't need to specify the type of variable like int, float because python is a type infer
#    language and smart enough to get the variable type.
#    for eg in java we use int a = 10 but in python we write simply a = 10.


#  2. What is Type casting?
# Type Casting is the method to convert the variable data type into a certain data type in order to the operation
# required to be performed by users.
#  There are two type of typecasting
#  * implicit typecasting
#  In this,  methods, Python converts data type into another data type automatically.
# eg: a to int
# a = 7
# print(type(a))
#  output will come as <class 'int'>
#  * explicit typecasting
#   In this method, Python need user involvement to convert the variable data type into certain data type in order to
#   the operation required.
# int variable
# a = 5
#
# typecast to float
# n = float(a)
#
# print(n)
# print(type(n))
#  output will come as <float 5.0>

#  3. what are tokens?
#  A token is the smallest individual unit in python program.all statements and instructions in a
#  program are built with tokens.
#  types of tokens
#  * Keywords:
#  They are reserved words and has specific meaning in a language and they cannot be used as ordinary identifiers.
#  eg class, break, continue, pass
#  * Identifiers:
# An identifier is a variable name.A Python identifier is a name used to identify a variable,
# function name,
# class name,
# module name or
# other object name.
# An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters,
# underscores and digits (0 to 9)
#  * Literals
#  In computer science, a literal is a notation for representing a fixed value in source code.
# name = “Madhu”   --- String literal
# age = 10  ---integer literal
# sal = 123.45 – float literal
# age = 10+20
#  * Operators
#  Operators are special symbols in Python that carry out arithmetic or logical computation.The value that the operator
#  operates on is called the operand
# >>>2+3
# 5
# 	Here + is an operator which is performing arithmetic computation.
# 	2 and 3 are the operands and
#   5 is the output of the operation.
#  * Constants:
#   A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers
#   that hold information which cannot be changed later.
#  for eg:  pi = 3.14 here pi is constant.

# 4. What is memory management in python?
#  Memory management in Python involves a private heap containing all Python objects and data structures.
#  The management of this private heap is ensured internally by the Python memory manager.

# 5. What is garbage collection and how does it work?
#  Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space.
#  The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.

#  IDE shotrcuts

#        Shortcuts:                                               Actions:
#       double shift                                        searches everywhere
#                                                        Quickly find any file, class, action, symbol, tool windows,or
#                                                        pycharm, in your project, and in the current Git repository.

#       ctrl+shift+A                                     Find action
#                                                        Find a command and execute.

#       Alt+enter                                         Show context actions
#                                                         Quick fixes for highlighted error and warnings.

#        F2                                               navigate between code issues

#       shift+F2                                          Jump to the next or previous  highlighted errors.


#  Operators:
# 1. What is an operator?
# Operators are used to perform operations on variables and values.
#  types of operators are:

# * Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations.
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y

# * Assignment operators
#  Assignment operators are used to assign values to variables
# =	    x = 5	  x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3

# * Comparison operators
# Comparison operators are used to compare two values
# ==	  Equal	                    x == y
# !=	Not equal	                x != y
# >	    Greater than	            x > y
# <	    Less than	                x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	    x <= y

# * Logical operators
# Logical operators are used to combine conditional statements
#  and 	       Returns True if both statements are true	                           x < 5 and  x < 10
# or	       Returns True if one of the statements is true	                   x < 5 or x < 4
# not	       Reverse the result, returns False if the result is true	not       (x < 5 and x < 10)

# * Identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location
# is 	       Returns True if both variables are the same object	             x is y
# is not	   Returns True if both variables are not the same object	         x is not y

# * Membership operators
# Membership operators are used to test if a sequence is presented in an object
# in 	            Returns True if a sequence with the specified value is present in the object	      x in y
# not in	        Returns True if a sequence with the specified value is not present in the object	  x not in y

#  Data Types:
# what are data types?
# classification of single type of data.
#  A) 1.NUMBERS ---> python supports four different data types, they are int,float,complex
#       eg int = 12
#          float =  5.7
#          complex = 5a + 7i
#
#     2.STRING ---> strings are amongst the most popular type in python.we can create them simply enclosing characters
#     in quotes. python treats single quotes the same as double quotes.
#            a = 'hello world'
#              print(a)
#     3. BOOLEAN ---> Boolean is a built-in logical data type that is mainly used for checking whether the logic of an
#     expression or comparison is true or not

#  KEYWORDS:
#  They are reserve words and has specific meaning in python language and they cannot be used as ordinary identifiers.
#   Keywords          Description
# =============   ==================
#   and	--->   A logical operator
#   as	--->  To create an alias
#  assert	--->  For debugging
#  break	--->  To break out of a loop
#  class	--->  To define a class
#  continue ---> To continue to the next iteration of a loop
#   def	 ---> To define a function
#   del	---> To delete an object
#  elif	---> Used in conditional statements, same as else if
#  else	---> Used in conditional statements
#  except	---> Used with exceptions, what to do when an exception occurs
# False	---> Boolean value, result of comparison operations
# finally	---> Used with exceptions, a block of code that will be executed no matter
#              if there is an exception or not
# for    --->  To create a for loop
# from   --->  To import specific parts of a module
# global --->  To declare a global variable
# if	---> To make a conditional statement