# set is a unordered collection with no duplicate
numbers = [1, 1, 2, 3, 4]
first = set(numbers)  # [1,2,4,4]
second = {1, 5}
# Can add using add() method and can remove using remove() method

# important applications of set

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in second:
    print("exist")
