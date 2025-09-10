#AK 7th budget calculator

num_one = int(input ("tell me your monthly income:\n"))
num_two = int(input("tell me your rent:\n"))
num_three = int(input("tell me your utilities cost:\n"))|
num_four = int(input("tell me how much your groceries cost:\n"))|
num_five = int(input("tell me how much your transportation cost:\n"))|
10
11
income = num_one
12
expenses = num_two + num_three + num_four + num_five
13
print("Your income is:", income)
14
savings = income* .1
15
print("You should put this much of your income into savings:", savings)
16
spending = income-(expenses+savings)
17
print("you have this much spending money:", spending)
18
19
rent_ percent = (num_two/income)*100|
20
print("This percentage of your income goes to rent:", rent_percent)
211
utilities_percent = (num_three/income) *100
22
23
print("This percentage of your income goes to utilities:", round(utilities_percent,1))
24
groceries_percent = (num_four/income) *100|
25
26|
print("This percentage of your income goes to groceries:", round(groceries_percent))
27
transportation_percent = (num_five/income) *100
281
29
print("This percentage of your income goes to transportation:", round(transportation_percent))