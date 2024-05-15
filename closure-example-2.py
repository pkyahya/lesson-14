def counter():
    count = 0
    def increment():
        nonlocal count
        print("count is "+ str(count))
        count += 1
        return count
    
    return increment

# create two counter instances
counter1 = counter()
counter2 = counter()

print(counter1())
print(counter1())
print(counter1())

print(counter2())