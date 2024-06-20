# No return type no parameter
from pip._internal.resolution.resolvelib.factory import C


def add():
    a = 90
    b = 30
    c = 40
    d = a + b + c
    print(d)


add()


# No return type with parameter


def sum(a, b, c):
    d = a + b + c
    print(d)


sum(1, 2, 3)

# return type with no parameter
def add():
    a = 10
    b = 20
    c = 30
    d = a + b + c
    return d


r = add()
print(r)

# return type with parameter


def sum(a, b, c):
    d = a + b + c
    return d

r = sum(1, 2, 3)
print(r)
