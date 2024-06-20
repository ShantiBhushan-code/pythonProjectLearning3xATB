# lambda expression
def double(x):
    return x * 2


print(double(5))
# output: 10

# lambda expression
double = lambda x: x * 2
print(double(5))

# Lamda expression with multiple arguments
add = lambda x, y: x + y
print(add(3, 8))


# Lambda expression with multiple statements
def my_function(x):
    if x > 5:
        return x ** 2
    else:
        return x

    my_function(6)


# Lamda expression with multiple statement


function = lambda x: x ** 2 if x > 5 else x
r = function(3)
print(r)

# Even odd

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(5))
