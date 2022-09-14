patient_name = "John Smith"
patient_age = 20
is_new = True
# print("Hello world")

#----- INPUTS
# take_name = input("Tell me your name ")
# print("name is ", 2022 - int(take_name))


# firstNumber = input('first number: ')
# secondNumber = input('second number: ')
# print('sum is', float(firstNumber) + float(secondNumber))

# print(patient_name.replace("John", "Jhonny"))
# print('ohy' in patient_name)


#------- OPERATORS
a = 5
a **= 3
# print(a)

# print(4 != 2)

isGood = True
# print(not isGood)

# -----------
# celcius = 12
# if celcius > 30:
#     print("Hot today!!!")
#     print("Drink a water")
# elif celcius > 20:
#     print('Nice day')
# else:
#     print("It's cold.")

# -------- IF STATEMENT
# weight = input("Insert weight: ")
# weight = float(weight)
# measure = input("measure. Type K for kg or L to lbs: ")
# measure = measure.lower()
# if measure == 'k':
#     print(weight, "Kg is equal to ", weight * 2.2046, "Lbs")
# elif measure == 'l':
#     print(weight, "Lbs is equal to ", weight / 2.2046, "Kg")
# else:
#     print("Cannot convert")

#------ WHILE
# i = 0
# while i < 10:
#     i += 1
#     print(i)

#----- LISTS
names = ['John', 'Bob', 'Mary', 'Smith']
names[3] = 'Rubem'
# print(names)
# print('from second to third', names[1:3])

names.append('Manis')
names.insert(2, 'Python')
names.remove('Bob')
# print(names, len(names))

# ----- FOR LOOP
# for item in names:
# print(item)

# ----
nrs = range(5, 20, 2)
print(nrs)
for nr in nrs:
    print(nr)

myConstList = ('edson', 'joao', 'paulo', 'fli')
myConstList.index('joao')
for item in myConstList:
    print(item)
