def hello(func):
    def inner():
        print("Hello ")
        func()

    return inner


@hello
def name():
    print("Alice")


name()
