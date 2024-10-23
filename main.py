from abc import ABC
class Abs_class(ABC):
    def print(self,x):
        print("Passed value : ",x)
    def abs_method(self):
        print("This is an abstract class method")
class test_class(Abs_class):
    def abs_method(self):
        print("This is a child class method")
obj1=test_class()
obj1.abs_method()
obj1.print(10) 