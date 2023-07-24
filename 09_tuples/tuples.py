# -------------tuple (same like list with out methods)----------------------
a = ("mango", "apple", "vamshikrishna", "sruthi", 4, 24)
print(a)

# ---------------we can perform min, max and sum can be performed-----------
b = (1, 2, 3, 4, 5, 6, 7, 8)
print(min(b))
print(max(b))
print(sum(b))
print(len(b))

# ------------------Concatenation (adding of two tuples)--------------------
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)

# ------------repeating of tuple --------------------------------------------
name = ("Sruthi", "Vamshikrishna")
print(name * 4)

# --------------iteration (arranging a data ina list)------------------------
fullName = ("Sruthi", "Vamshikrishna")
for i in fullName:
    print(i)

# --------------Membership (to find the element present in data)-------------
firstname = ("Sruthi")
print("S" in firstname)
print("M" in firstname)
