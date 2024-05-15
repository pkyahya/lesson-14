def outer_function(x):
    def inner_function(y):
        return x + y
    
    def inner_function2(z):
        return x + z
    return inner_function, inner_function2

    

var_1, var_2 = outer_function(10)
print(var_1(5))
print(var_2(20))
print(var_1(3))