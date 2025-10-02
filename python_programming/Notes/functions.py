# AK 7th functions notes


#def welcome():
    #name = input("what is your name? ")
    #print(f"Hello " + {name})


#print("This is not in my function")
#welcome()




#What a function is
# Is a pre-built funtion that performs a specific task

#Why we use functions
# so then we don't have to keep writing the same code over and over again

#How to write a function in Python
def roll(mod):
    return random.randint(2, 18) + mod
print("Here are your stats!")
print(f"Strength: {roll(0)}\nDexarity: {roll(1)}\nIntelligence: {roll(1)}\nCharisma: {roll(0)}")

strength = roll(0)
dexarity = roll(1)
intelligence = roll(1)
charisma = roll(0)

#What parameters and arguments are
# parameters: variable that only exists in the function
# argument: is the value that you give it
#How to use parameters and arguments in python


#What return statements are
return random.randint(2, 18) + mod
#what you wnat to end the function
#How to use return statements in a program
return random.randint(2, 18) + mod


#print()

#def add(number, number_two):
#    number += number_two
   #print(number)

#add(80)
#add(3)
#add(9)
#add(11)
#add(num_one)

import random

def roll(mod):
    return random.randint(2, 18) + mod
print("Here are your stats!")
print(f"Strength: {roll(0)}\nDexarity: {roll(1)}\nIntelligence: {roll(1)}\nCharisma: {roll(0)}")

strength = roll(0)
dexarity = roll(1)
intelligence = roll(1)
charisma = roll(0)
