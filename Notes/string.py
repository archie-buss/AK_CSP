#AK 7th string notes

#What makes something a string?
# a collection of letters, numners, and symbols that are surrounded by quotation marks
#Why do we have strings?

#How do stupid proofing and sanitization relate to each other?
# by making sure things work right. basically step one of stupid proofing
# for example like removing all of the extra spaces, makinf sure that something IS capitalized or making it lowercase.
#What is debugging?
# fixing your program
#How do you debug the different types of errors?
# syntax error - by fixing your spelling, and puntuation
# logic error - when your code seems to work but the output is wrong
# runtime error - by fixing the part of the code that makes it crash
#Describe what each of the methods below does:
#find()to find a specific letter or word in a string
#concatenate ()add one or more strings together
#upper(to make all letters uppercase)
#lower(to make all letters lowercase)
#strip(to remove the spaces at the beginning and end of a string)

#" content "
#'content'
#they are the same

#examples
first_name = input("what is your first name?:\n").strip().title()
last_name = input("what is your last name?:\n").strip().title()
full_name = first_name + " " + last_name

sentence = 'The quick brown fox jumps over the lazy dog.'
print(sentence)


print("welcome to my program", full_name + "!")

sentence = ' The quick brown fox jumps over the lazy dog. '
print(sentence[20:25])

#len-finds how long ghe string is
print(len(sentence))
