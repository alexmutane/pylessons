
# Calc year when one will turn 100 years old
from datetime import date
username = input("what's your name:")
userage = input("Tell me your age:")
userage = int(userage)
current_year = date.today().year
birthyear = current_year - userage
hundred_in = birthyear + 100

print(username, ", you was born in", birthyear,
      "and you'll turn 100 years old in:", hundred_in)
