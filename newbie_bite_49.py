GREETING = "Hello, {name}! You are {age} years old."


def create_greeting(name, age):
    return GREETING.format(name=name, age=age)
