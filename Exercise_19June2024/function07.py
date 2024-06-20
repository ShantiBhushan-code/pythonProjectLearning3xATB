def outer_fun() :
    a= 20
    print(a)
    def inner_fun() :
        #a= 30
        print(a)

    inner_fun()

outer_fun()