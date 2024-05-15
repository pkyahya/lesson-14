def decorator(func):
    def wrapper():
        func()
        print("First after function execution")
        print("Second after function execution")
    return wrapper

def decorator_2(func):
    def wrapper():
        print("This is decorator 2 running")
        func()
    return wrapper

@decorator
def say_hello():
    print("Hello!")

@decorator_2
def say_goodbye():
    print("Goodbye!")

say_hello()
say_goodbye()