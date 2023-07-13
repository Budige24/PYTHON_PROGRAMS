# ---------------------Dictionaries (its an data type)-------------------
student = {'name': "Sruthi", 'DOB': 24 - 10 - 2000, 'location': "karimnagar", }
# print(student['name'])

# ------------------Get-----------------------------------
a = {1: "vamshi", 2: "sandeep", 3: "manasa"}
# print(a.get(1))

# ------------------keys----------------------------------
# print(a.keys())

# ------------------------values--------------------------
b = {1: "sruthi", 2: "shiva", 3: "ranjith"}
# print(b.values())

# ----------------------items-----------------------------
c = {1: "ramu", 2: "manasa", 3: "riyan", 4: "mikky"}
# print(c.items())

# ---------------------Update-----------------------------
d = {1: "sravan", 2: "madusudhan",}
d.update({3:"Ruchitha"})
# print(d)

for i,j in {1: "ramu", 2: "manasa", 3: "riyan", 4: "mikky"}.items():
    print(i,j)