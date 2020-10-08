'''
class <classname>([base classes]):
    instance methods.
    class nethods
    static methods
'''

class Employee():
    count = 100;
    def __init__(self):
        self.count = 99;

    def display(self):
        print("count = {}".format(self.count));

    @classmethod
    def modifyCount(cls):
        cls.count += 100;

print("Employee.count", Employee.count);
e1 = Employee();
print(e1.__dict__);
Employee.modifyCount();
print(e1.__dict__);
e1.display();
print("Employee.count", Employee.count);
