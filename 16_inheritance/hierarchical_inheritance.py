# -------------------hierarchical inheritance -----------------------
# ---in hierarchical inheritance there will be one
# parent class and multiple child classes---------------------------
class father():  # Base class
    def Output_father(self):
        print("iam a father class")


class child1(father):   # Derived class1
    def Output_child1(self):
        print("iam child class1")


class child2(father):   # Derived class2
    def Output_child2(self):
        print("iam child class2")


obj = child1()
obj.Output_child1()
obj.Output_father()
obj = child2()
obj.Output_child2()
obj.Output_father()
