# AK 7th expressions notes

# What is an algorithm?
    # Answer 
name = input("hello, what is your name?")
print("hello", name)

#treyson has 12 apples, he has 5 friends that he wants to give apples to. How many apples does each friend get?
apples = 12
friends = 5
print("each friend gets", apples / friends, "apples")


# List steps in an algorithm
#1. variables(get needed info)
#2. do the equations(do the things)
#3. display results
# List ALL of the different mathematical operators (Give me the symbol and tell me what it does)
number_1 = int(input("tell me a number:\n"))
number_2 = float(input("tell me another number:\n"))
number_1 += number_2
print("addition(+):", number_1)
number_1 += number_2
print("subtraction(-):", number_1)
number_1 -= number_2
print("multiplitation(*):", number_1)
number_1 *= number_2
print("division(/):", round(number_1, 2)) #round(number to round, number of decimal places)
number_1 /= number_2
print("exponents(**):", number_1)
number_1 **= number_2
print("integer division:", number_1)
number_1 //= number_2
print("muldo(%):", number_1)
number_1 %= number_2
# List ALL of the different assignment operators (Give me the symbols and what it does)
#(+)means addition
#(-)means subtraction    
#(*)means multiplication
#(/)means division
#(//)means integer division
#(%)means modulo
#(**)means exponentiatioexonents
# Why are expressions so important in programming?
# Because we learn to use expressions for be able to create better code.
# Average age of 4 people

# integers in programming are whole numbers

# floats in programming are numbers with decimals

# mudlo = remainder of a division problem



person1 = 14
person2 = 13
person3 = 21
person4 = 10

total= person1 + person2 + person3 + person4
print("the total age of 4 people is", total)
average = total / 4
print("the average age of 4 people is", average)
