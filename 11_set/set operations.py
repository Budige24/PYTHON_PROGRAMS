# --------Set Union (to merge to sets)-----------------
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

# ------------Intersection (gives common elements)-------
set3 = {1, 2, 4, 24}
set4 = {4, 24, 30, 29}
print(set3.intersection(set4))

# ------------ issubset and issuperset ------------------
set5 = {123, 456, 789, 987, 543, 678}
set6 ={123, 456,789}
print(set5.issuperset(set6))
print(set6.issubset(set5))