nr = input("enter a number:")
nr = int(nr)

if nr % 2 == 0:
    print(nr, "is Even")
else:
    print(nr, "is Odd")


# ---- PRINT NRS LESS THAN GIVEN ONE
nrs = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
less_than = input("Ref nr to compare:")
less_than = int(less_than)
for number in nrs:
    if number < less_than:
        print(number)
