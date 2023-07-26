# -------------------multiple inheritance ----------------------------
# ----can inherit multiple classes in a single class------------------
# --------this type of inheritance can only done in python -----------
# -------multiple base classes can be inherited in a derived class----
class Father():  # Base Class 1
    def Output_father(self):
        print("iam a father class")


class Mother():  # Base Class 2
    def Output_mother(self):
        print("iam a mother class")


class Child(Father, Mother):    # Derived class
    def Output_child(self):
        print("iam a child class")


obj = Child()
obj.Output_father()
obj.Output_mother()
obj.Output_child()