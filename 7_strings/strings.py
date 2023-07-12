# ------------------single (for single string or sentence) '' -----------------------------
a = 'hello sruthi'
print(a)

# ------------------double (for single line with multiple sentences)""----------------------
b = "Hello, Sruthi!"
print(len(a))

# -----------------triple (used for multiple lines and multiple sentences) '""'-------------
c = '"hello sruthi ' \
    'how are you ' \
    'had your lunch ' \
    'when are you coming to hyderabad"'
print(c)

# -----------------------------------UPPER (upper case)-----------------------------------
NAME = "Sruthi Vamshikrishna"
print(NAME.upper())

# -----------------------------------lower (lower case)-----------------------------------
name = "SRUTHI VAMSHIKRISHNA"
print(NAME.lower())

# ----------------------------------Replace (to replace a word)---------------------------
fullname = "Sruthi Mahendher"
print(fullname.replace("Mahendher", "Vamshikrishna"))

# -----------------------Count (to know how many times a letter is present)--------------
applicant = "Sruthi Vamshikrishna"
print(applicant.count("i"))

# ----------------------Remove (to remove a word or a letter)----------------------------
Name = "Sruthi Mahender"
print(Name.removesuffix("Mahender"))
print(Name.removeprefix("Sruthi"))

# ----------------------Split (to change from string to list)----------------------------
_name = "Sruthi Mahender"
print(_name.split())

# ----------------------strip (to remove the empty space)--------------------------------
_fullname = "    Sruthi Mahender     "
print(_fullname)
print(len(_fullname))
print(_fullname.strip())
