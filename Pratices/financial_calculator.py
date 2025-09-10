# AK 7th budget calculator


income = float(input("what isyour monthly income:\n"))
rent = float(input("what is your monthly rent:\n"))
utilities = float(input("what is your monthly utilities:\n"))
groceries = float(input("what is your monthly groceries:\n"))
transportation = float(input("what is your monthly transportation cost:\n"))
rent_percent = (rent / income) * 100
utilities_percent = (utilities / income) * 100
groceries_percent = (groceries / income) * 100
transportation_percent = (transportation / income) * 100
savings = income * 0.10
savings_percent = 10
total_expenses = rent + utilities + groceries + transportation + savings
leftover = income - total_expenses
print("your rent is", rent, "and that is", round(rent_percent), "% ofyour income.")
print('your utilities are', utilities, "and that is", round(utilities_percent), "% of your income.")
print("your groceries are", groceries, "and that is", round(groceries_percent), "% of your income.")
print("your transportation cost is", transportation, "and that is", round(transportation_percent), "% of your income.")
print("you should save", savings, "am month, that is", savings_percent, "% of your income.")
print("you have", leftover, "of spending money each month.")