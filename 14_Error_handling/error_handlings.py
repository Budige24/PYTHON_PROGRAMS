# --------------------ERROR Handling---------------------
a = 1
try:
    print(b)  # risky code
except:
    print("error")
else:
    print("no error")
finally:
    print("always")
