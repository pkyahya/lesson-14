def myFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")


# Driver code
myFun(first='ReDI', mid='School', last='Python')