# for loop
# we can only loop over iterable object
# for number in range(3):
#     print("attempt", (number+1)*".")

# for else
for number in range(1, 4):
    print("attempt", number*".")
    if number == 3:
        break
else:
    print("Attempt 3 times but failed")

# nested loop
for x in range(3):
    for y in range(4):
        print(f"({x},{y})")

number = 100
# While loop
while number > 0:
    print(number)
    number //= 2

# Another example of while loop
while True:
    command = input(">")
    if command.lower() == "quit":
        break
