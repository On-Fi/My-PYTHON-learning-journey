# Lesson 04 by Dave Gray

#-------------------
# String data type
#-------------------

# literal assignment
first = "Oni"
last = "Fistik"

print(type(first)) # the type() function returns the type of an object | the output is <class 'str'>  'str' = string
print(type(first) == str) # == str is a Statment that means "the datatype is a string" | the output is a boolean in this case it is true 
print(isinstance(first, str)) # the isinstance() function returns True if a specified object is an instance of a specified object
print("")

# constructor function
pizza = str("Margherita") # the str() returns a string object

print(type(pizza)) # the type() returns the type of an object | the output is <class 'str'>  'str' = string
print(type(pizza) == str)  # == str is a Statment that means "the datatype is a string" | the output is a boolean in this case it is true 
print(isinstance(pizza, str)) # the isinstance() function returns True if a specified object is an instance of a specified object
print("")

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)
print("")

# Casting a number to a string
decade = str(1990) # the number 1990 is now a string thanks to the str() function 
print(type(decade)) # the output is <class 'str'>  'str' = string
print(decade) # the output 1990 is as a string

statement = "I like rap music of the " + decade + "s."
print(statement)
print("")

# Multiple lines
multiline = """ 
hey was geht?

alles gut bro!
                                  :]
"""
print(multiline)
print("")

# Escaping special characters
sentence = 'I\'m back baby! \t Hey\n\nWhere\'s my money :\/: '
print(sentence)
print("")

# String Methods
print(last)
print(last.lower()) # the lower method makes every character of a string to lower case
print(last.upper()) # the upper method makes every character of a string to upper case
print(last)

print(multiline.title()) # the title method makes every word in a string to proper case
print(multiline.replace("gut", "SUPER")) # the replace method replaces a part a string 
print(len(multiline)) # the len method counts every character of a string | the output is a number (in this case 69)
print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "°"))
print("Coffee".ljust(18, "-")+ "2€".rjust(2))
print("Donut".ljust(18, "-")+ "3€".rjust(2))
print("Muffin".ljust(18, "-")+ "3€".rjust(2))
print("°°°°°°°°°°°°°°°°°°°°")
print("")

# string index values
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])
print("")

# Some methods return boolean data
print(first.startswith("O"))
print(first.endswith("Z"))
print("")


#-------------------
# Boolean data type
#-------------------
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print("")


#-------------------
# Numeric data type
#-------------------


