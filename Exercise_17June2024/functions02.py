# *args
def sum(a, b, c):
    return a + b + c


results = sum(1, 2, 3)
print(results)


def sum_three(a=2,b=3,c=4):
    return a + b + c


r = sum_three(1, 2)
print(r)
