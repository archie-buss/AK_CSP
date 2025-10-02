#AK 7th conditionals notes


#What do if statements do?
# telling the computer "if something happens, do this"
#What are boolean statements? 
# always a true or false
#What do else statements do?
 #doing the other output if the input isn't the if statement
#What kind of statement do you use if you have more than 2 needed outcomes?
 #elif
#What do each of the different symbols mean in conditionals?

#< : if its less than
#> :if its greater than
#<= : if it
#>= : if its greater than or equal to
#== : is a question
#!= : now equal too/not
#What are the 3 logical operators?
# and, or, not# And allow us to combime multiple conditions
#What are logical operators for?
# they tell the code if its true, not true, or else#
#What does a nested conditional statement do?
# ony happens inside another conditional

#homework = input("is your homework done?").#strip().capitalize()
#if homework == "no":
#   print("Then go do your homework!")
#else:
#   print("Yes you can go!")

#grade = 60

#if grade >= 90:
    #print(f"You have a {grade}%, you get an A!")
#elif grade >= 80:
    #print(f"You have a {grade}%, that is a B!")
#elif grade >= 70:
    #print(f"You have a {grade}%, that is a C!")

#else:
    #print:(f"You have a {grade}%, that is a D or lower.")

#name = input("what is your name?")

#if name == "Ms LaRose":#
    #print("you are the teacher!")
#elif name == "tia" or name == "ashley":
    #print("you are a TA")
#else:
    #print(f" hello, {name}, you are a student")


grade = 97

if grade >= 90:
    if grade > 100:
        print("Thats not possible you cheated!")
    print(f"You have a {grade}%, you get an A!")
elif grade >= 80:
    print(f"You have a {grade}%, that is a B!")
elif grade >= 70:
    print(f"You have a {grade}%, that is a C!")