

class Base:
    def __init__(self):
        self.i = 10;
        print("Base.display:", self.i);

class Derived(Base):
    def __init__(self):
        super().__init__();
    def display(self):
        print("B.display:", self.i);


d1 = Derived();
print(Derived.mro());

d1.display();
