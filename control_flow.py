# comparison operator
# >,<,==,>=,<=

# conditional statement
temperature = 23
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("it's good")
else:
    print("It's cold")
print("done")

# ternary operator
age = 12
message = "Eligible" if age >= 18 else "not eligible"
print(message)
# as ternary operator return value it can be use as expression
validity = f"He is {'Eligible' if age >= 18 else 'not eligible'} to consume alcohol"
print(validity)

# logical operator
# and, or, not are logical operator

# chaining comparision operator
age = 22
# if age>=18 and age<65:
if 18 <= age < 65:
    print("Eligible")
