
def greet():
    print("Hello")
    print("welcome")


greet()


def greet_with_name(f_name, l_name):
    print(f"Hello {f_name} {l_name}")
    print("welcome")


# here 2nd argument is keyword argument
greet_with_name("abdullah", l_name="alid")


def greet_name(f_name, l_name="alid"):
    print(f"Hello {f_name} {l_name}")
    print("welcome")


# here 2nd argument is  not required argument
greet_name("abdullah", "arin")


# *args
def prod(*numbers):
    result = 1
    for n in numbers:  # numbers is a tuple
        result *= n
    return result


print(prod(1, 2, 3, 4, 5))  # 120

# **args


def user_date(**users):
    for u in users:  # users is a dictionary
        print(u, users[u])


user_date(id=1, name="alid")

# debug practice


def prod_prac(*numbers):
    result = 1
    for n in numbers:  # numbers is a tuple
        result *= n
    return result


print(prod_prac(1, 2, 3, 4, 5))
