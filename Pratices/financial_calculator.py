# AK 7th budget calculator


income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent/mortgage: "))
utilities = float(input("What is your monthly utilities: "))
groceries = float(input("What is your monthly groceries: "))
transportation = float(input("What is your monthly transportation?"))
rent_percent = (rent / income) * 100
utilities_percent = (utilities / income) * 100
groceries_percent = (groceries / income) * 100
transportation_percent = (transportation / income) * 100
savings = income * 0.10
savings_percent = 10
total_expenses = rent + utilities + groceries + transportation + savings
leftover = income - total_expenses
print("Your rent is $", rent, "and that is", round(rent_percent), "% of your income.")
print("Your utilities are $", utilities, "and that is", round(utilities_percent), "% of your income.")
print("Your groceries are $", groceries, "and that is", round(groceries_percent), "% of your income.")
print("Your transportation is $", transportation, "and that is", round(transportation_percent), "% of your income.")
print("You should save $", savings, "a month, that is", savings_percent, "% of your income.")
print("You have $", leftover, "of spending money each month!")