print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
  print("You are tall enough to ride the rollercoaster!")
  age = float(input("How old are you? \n"))
  if age <= 12:
    print("Please pay 5€")
  elif age <=18:
    print("Please pay 7€")
  else:
    print("Please pay 12€")
else:
  print("You can't ride! ;(")


# < Less than
# > Greater than
# <= less than or equal to
# >= Greater than or equal to
# == Equal to
# != Not equal to

# modulo: gives the amount of decimal points a number has. it is used with the percentage sign
# Which number do you want to check?
#number = int(input())

# If the number can be divided by 2 with 0 remainder.
#if number % 2 == 0:
 # print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
#else:
 # print("This is an odd number.")
