# ----------multilevel inheritance-------------------------------------------
# ----(same as single level inheritance but will be a Grandfather class)----
# --
class Grandfather():  # Base class
    def Output_Grandfather(self):
        print("iam grandfather class")


class parent(Grandfather):  # Intermediate class
    def Output_parent(self):
        print("iam a parent class")


class child(parent):    # Derived class
    def Output_child(self):
        print("iam a child class")


obj = child()
obj.Output_Grandfather()
obj.Output_parent()
obj.Output_child()
