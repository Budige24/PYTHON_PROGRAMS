# ----------------------polymorphism-----------------------------------
# ---for a single method we can give data in multiple forms -----------


class polymorphism():
    def add(self, a, b):
        print(a + b)


obj = polymorphism()
obj.add(1, 2)
obj.add("Sruthi", "_Vamshikrishna")
obj.add((24, 4), (30, 21))
obj.add([1, 2], [3, 4])
