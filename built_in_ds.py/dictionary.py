# collection of key value pair
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])

print(point.get('a', 0))
del point["x"]
print(point)
for a in point:
    print(a, point[a])
for key, value in point.items():
    print(key, value)

# dictionary comprehension
# value = {}
# for x in range(5):
#     value[x] = x*2
value = {x: x*2 for x in range(5)}
print(value)

# generator expression take less memory, used only for iteration, can't hold values

# unpacking operator
