# Lesson 03 by Dave Gray

fristname = "Onur"
lastname = "Fistikci"

print("Onur" + "Fistikci") # output  = OnurFistikci
print("Onur " + "Fistikci") # output  = Onur Fistikci
print(fristname + lastname) # output = OnurFistikci
print(fristname + " " + lastname) # output = Onur Fistikci
print(fristname + "       " + lastname) # output = Onur       Fistikci
print("")

# Arithmetic Operators Part 01 = + - * /
age = 30
print(age + 5) # output = 35
print(age - 5) # output = 25
print(age * 5) # output = 150
print(age / 5) # output = 6.0
print(round(age / 5)) # output = 6
print("")

# Arithmetic Operators Part 02 = Expone­nti­ation ** , Floor division // and Modulus %
number = 10
print(number ** 5) # output = 100000 because "**"" means number * number * number * number * number
print(number // 4) # output = 2 because "//" means 5 / x = 10 
print(number % 5)  # output = 0 because "%" means number module 5 
print("")

# Python Comparison Operators
# Equal                        x == y
# Not equal                    x != y
# Greater than                 x > y
# Less than                    x < y
# Greater than or equal to     x >= y
# Less than or equal to        x <= y

# Boolean Values
print(5 == 8) # output = False because "5 is equal to 8" is false
print(5 != 8) # output = True because "5 is NOT equal to 8" is true
print(5 < 8) # output = True because "5 is less than 8" is true
print(5 > 8) # output = False because "5 is greater than 8" is false
print(5 >= 8) # output = False because "5 is Greater than or equal to 8" is false
print(5 <= 8) # output = True because "5 is Less than or equal to  8" is true
print("")

# If Statment
meaningIf = 24

if meaningIf > 10:
 print('That`s True')
else:
 print('Nope that`s not true')

if meaningIf < 10:
 print('That`s True')
else:
 print('Nope that`s not true')
print("")

# Ternary Operator
meaningTernary = 42
print('That`s Right') if meaningTernary > 10 else print('Nope that`s not right')
print('That`s Right') if meaningTernary < 24 else print('Nope that`s not right')