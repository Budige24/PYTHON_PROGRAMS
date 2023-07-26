# -----------inheritance (using methods, properties a class in another class)-----
# -------------------single level inheritance ---------------------
class parant():
    def output(self):
        print("iam parent class")


class child(parant):
    def output_child(self):
        print("iam a child class")


obj = child()  # child class
obj.output_child()  # child method
obj.output()  # parent method
