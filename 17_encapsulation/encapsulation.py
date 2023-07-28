# ---------------------------------encapsulation--------------------------------
# ---wrapping of variables methods in a single unit is called encapsulation-----
# ------access modifiers (public, private, protected)---------------------------
# --------------------------------(Private__)-----------------------------------
# --------------------------------(Protected_)----------------------------------

class school():
    def __init__(self, a, b):
        self.__a = a  # Private (two underscores __)
        self._b = b  # Protected (single underscore _)


class BiologyClass(school):
    def Output(self):
        print(self._b)  # Protected can be accessed in every class who has inherited it
    #  print(self.__a)  # Private cannot be accessed outside its class


obj = BiologyClass("Sampath", "vamshiKrishna")  #
obj.Output()
