# Double in existing list
list1 = [1, 6, 3, 10, 5]
new_list = []
print("My original list is :", list1)
for x in list1:
    print(x)
    new_list.append(x * 2)

print("New list is :", new_list)


# using Map() function:
# Take each item from list
# Execute function it
# return same number of items in list
list2 = [1, 6, 3, 10, 5]
print("My original list is :", list2)

def double(x):
    return x*2

double_list = list(map(double,list2))
print("New list is :", double_list)
