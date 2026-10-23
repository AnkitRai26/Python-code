Data Type

1.Interger
2.String
3.Float
4.Boolean
5.None

Interger is positive, negative and zero (25,-25,0)
String is single quote, double quote and triple quote ('', "", '" "') usually perfer to use doublw quotes

Float is decimal value (3.99, 2.4, 9.0)
Boolean is True and False (capital T and F is important)
None is not single type value storge.



--------------Keywords----------
Keywords are reserved words in python.

and, else, in, return, as,expect, is, True, False, 

The list of keywords are : 
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 
'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
'try', 'while', 'with', 'yield']

Category	Keywords
Value Keywords       True, False, None

Operator Keywords	  and, or, not, is, in

Control Flow Keywords {if, else, elif, for, while, break, 
                      ,continue, pass, try, except, finally, raise, assert}

Function and Class	   def, return, lambda, yield, class

Context Management	   with, as

Import and Module	   import, from

Scope and Namespace	    global, nonlocal

Async Programming	    async, await

--------Types of Operators-------

An Operator is a symbol that performs a certain operation between operands.
1.Arithematics operators (+,-,*,/,**,%)
2.Relational/Comparison Operators(==,!=,>,<,>=,<=)
3.Assignment Operators(=,+=,-=,*=,/=,%=,**=)
4.Logical Operators(not, and, or)


--------Type Conversion-------

These are two types of conversion
1.Implicit Conversion
2.Explicit Conversion (Type Casting)

Implicit Type Conversion
Python automatically changes one data type to another during runtime when safe
to do so, typically to prevent data loss during arithmetic operations

Integer to Float: Adding an int and a float results in a float

num_int = 10     # int
num_flt = 5.5    # float
result = num_int + num_flt
print(result)    # Output: 15.5
print(type(result)) # Output: <class 'float'>


Boolean to Integer: True evaluates to 1 and False evaluates to 0 in arithmetic operations.

result = True + 4 
print(result)    # Output: 5


Explicit Type Conversion (Type Casting)


You use manual functions to explicitly cast a value when Python cannot do it automatically,
such as changing a string into a number.

Primitive Type Functions

int(x): Converts x to an integer, truncating decimals or parsing numeric strings.
float(x): Converts x to a floating-point decimal number
str(x): Converts x into its string representation.
bool(x): Converts x to a boolean (True or False), where empty items or 0 evaluate to False

# Converting string to integer
age_str = "25"
age_int = int(age_str)

# Truncating a float
pi_int = int(3.14)  # Results in 3

Collection Type Functions
list(x): Converts an iterable (like a tuple or string) into a mutable list.
tuple(x): Converts an iterable into an immutable tuple
set(x): Converts an iterable into a collection of unique items, stripping duplicates.
dict(x): Converts a sequence of key-value tuples into a dictionary.

# Remove duplicate numbers using a set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = list(set(numbers))  # Results in [1, 2, 3, 4]


Potential Errors
If you try to explicitly convert a value that does not match the target format (e.g., text letters to an integer), Python will throw a ValueError.
# This raises: ValueError: invalid literal for int() with base 10: 'hello'
number = int("hello") 


To handle this cleanly, you can implement a standard try-except guard block.


