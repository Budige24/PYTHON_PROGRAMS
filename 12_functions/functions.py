# --------------Functions (a block of code)----------------------
def func():  # function definition
    print("this is function")  # function body


func()  # function call


# ----------parameters in function -------------------------------
def func1(a, b, c):
    print("this is function", a, b, c)


func1(1, 2, 3)


# ---USE * to sent multiple arguments to a single parameter-------
def func1(*a):
    print("this is function", a)


func1(1, 2, 3)


# ----USE ** to sent multiple arguments to a single
# parameter and to view in a dictionary form ----------------------
def func1(**a):
    print("this is function", a)


func1(a=1, b=2, c=3)
