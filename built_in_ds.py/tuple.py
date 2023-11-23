# tuple is basically read only list
from array import array
point = (1, 3)+(2, 4)*3
print(point)
point1 = tuple([1, 2, 3])
x, y, z = point1
print(point1)
print(x)
print(y)
print(z)
if 3 in point1:
    print("exist")


# swapping two variable
x = 10
y = 11

x, y = y, x  # x,y=(y,x),   x,y = 10,11
print("x", x)
print("y", y)


# array
# from array import array
# use array when working with large amount of dataset
numbers = array("i", [1, 2, 3])
