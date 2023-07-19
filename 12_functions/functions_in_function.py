# -------------Nested-functions (functions in function)------------
def outer():
    print("this is outer function")

    def inner():
        print("this is inner function")

    inner()


outer()


# -------------import functions-----------------------------------
def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)
