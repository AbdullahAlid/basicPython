# print("Hello World!")
# print("*"*10)
# print("Hello")

# primitive datatype
import math  # import math module
student_count = 7  # number
rating = 4.8  # number
is_attend = True  # boolean
course_name = "python programming"  # string

# string access
print(len(course_name))  # 18 len is a built in function
print(course_name[0])  # p
print(course_name[-1])  # g
print(course_name[0:3])  # pyt
print(course_name[0:])  # python programming
print(course_name[:3])  # pyt
print(course_name[:])  # python programming

# escape sequences
# \"
# \'
# \\
# \n
course_name = "python \nprogramming"
print(course_name)

# formatted string
first_name = " Abdullah"
last_name = "alid"
full_name = first_name+" "+last_name
print(full_name)
# any valid expression can be written inside {} in formatted string
full_name_using_formatted_string = f"{first_name} {last_name}"
print(full_name_using_formatted_string)


# some common string method
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.strip())
print(full_name.find("ali"))
print(full_name.replace("ali", "bali"))
print(full_name)
print("bali" in full_name)
print("bali" not in full_name)

# arithmatic operator
# +,-,*,/,//.**,%
# augmented assignment operator
# +=, -=, *=, /=, //=, **=, %=

# some common number method
print(round(2.5))
print(abs(-2.8))
print(math.ceil(2.2))


# type conversion
x = input("X :")
y = int(x) + 1

print(bool(-1))

# Falsy Values Includes:

# 1) Sequences and Collections:

# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ” “
# Empty ranges range(0)
# 2) Numbers: Zero of any numeric type.

# Integer: 0
# Float: 0.0
# Complex: 0j
# 3) Constants:

# None
# False

# everything beyond them are considered as truthy value
