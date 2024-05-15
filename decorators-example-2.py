def uppercase_decorator(func):
    def wrapper(text, text_2):
        result = func(text, text_2)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello(name, name_2):
    return f"Hello, {name}, {name_2}!"

print(say_hello("Alice", "Bob"))