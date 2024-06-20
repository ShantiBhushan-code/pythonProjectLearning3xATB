my_List =[12,11,13,"shanti",1.2,True]
print(my_List)

#indexing
print(my_List[0])

#changing an element
my_List[3] = "bhushan"
print(my_List)
#append
my_List.append(100)
print(my_List)
#extend
my_List.extend([101,102])
print(my_List)
#insert
my_List.insert(1, "Awaken")
print(my_List)

#copy list
my_copy_list = my_List.copy()
print(my_copy_list)

my_copy_list[1]= 2
my_copy_list[4] =8
my_copy_list[6] = 10
print(my_copy_list)

my_copy_list.sort()
print(my_copy_list)

my_copy_list.remove(1.2)
print(my_copy_list)
#pop
my_copy_list.pop(3)
print(my_copy_list)
#reverse
my_copy_list.reverse()
print(my_copy_list)
#clear
my_List.clear()
print(my_List)
