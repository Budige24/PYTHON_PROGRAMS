# ----------------File_handling------------------------
# _______________Read a file --------------------------
file = open('message.txt', mode='r')
print(file.read())
file.close()

# ------------------Write in a file (replace the text in file)------------------
file = open('message.txt', mode='w')
file.write('hello team')
file.close()

# --------append (add the text in the file to the existing data)----------------
file = open('message.txt', mode='a')
file.write('bye bye')
file.close()

# ------------------r+ (Read + Write)-------------------------------------------
file = open('message.txt', mode='r+')
print(file.read())
file.write("r+ mode")
file.close()
