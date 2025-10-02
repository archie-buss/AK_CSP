#AK 7th old enough



age = int(input("Hi, what is your age?\n"))

if age >= 18:
    print(f"you are {age}, you can vote!")
elif age >= 16:
    print(f"you are {age}, you can drive!")
elif age >= 15:
    print(f"you are {age}, you can get your learns permit!")
elif age <= 15:
    print(f"you are {age}, you can go to school!")
else:
    print(f"you are {age}, your not old enough, go home!")