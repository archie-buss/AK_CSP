#AK 7th fizz buzz practice

x = 1

while x < 50:
    if x % 3 == 0:
        print(f"BUZZ")

    elif x % 5 == 0:
        print(f"FIZZ")
    else:
        print(f"{x}")
    x += 1