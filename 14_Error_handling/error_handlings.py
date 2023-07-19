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

# ------------------Error handling ------------------------

c = "chintu"
try:
    print(c+22)
except TypeError:
    print("type error1")
except ValueError:
    print("value error2")
