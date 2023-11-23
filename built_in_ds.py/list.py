from collections import deque
letters = ['a', 'b', 'c']
matrix = [[2, 1], [3, 5]]  # two dimentional list
zeros = [0]*5
combined = zeros + letters
print(combined)
numbers = list(range(20))
chars = list("hello world")
print(chars)


# accessing list
letter = ['a', 'b', 'c', 'd']
print(letter[::2])  # ['a','c']
print(letter[::-1])  # ['d','c','b','a']

# unpacking list
first, second, *last = letter
print(first, second, last)
f, *s, l = letter
print(f, s, l)

# looping over list
for index, l in enumerate(letter):
    print(index, l)

# adding or removing items
# add
alphabets = ['a', 'b', 'c']
alphabets.append('d')
alphabets.insert(0, 'A')
print(alphabets)

# remove
alphabets.pop(0)
print(alphabets.index('d'))
print(alphabets.count('d'))
alphabets.remove('d')
print(alphabets)
del alphabets[1:]
alphabets.clear()
print(alphabets)


# sorting list
numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))  # it doesn't change the original list
print(numbers)

items = [
    ('product1', 9),
    ('product0', 10),
    ('product2', 8)
]
items.sort()
print(items)


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)
# uses of lambda function
items.sort(key=lambda item: item[1])
print(items)

# map function
price = []
# for item in items:
#     price.append(item[1])
# print(price)

prices = list(map(lambda item: item[1], items))  # map
prices = [item[1] for item in items]  # using list comprehension
print(prices)

# filter function
# filtered = list(filter(lambda item: item[1] > 8, items))
filtered = [item for item in items if item[1] > 8]  # using list comprehension
print(filtered)

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40]
print(list(zip("abcd", list1, list2)))

# stack
# append, pop

# queue
# from collections import deque
listing = deque([])
listing.append(1)
listing.append(2)
listing.append(3)
val = listing.popleft()
print(val)
if not listing:
    print("empty")
