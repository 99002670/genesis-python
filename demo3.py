class Number():
    def __init__(self, n):
        self.n = n;

    def display(self):
        print("N=", self.n);

    def __add__(self, other):
        self.n = self.n + other.n;


n1 = Number(10);
n2 = Number(20);
n1.display();
n1 + n2;    #n1.__add__(self,n2)
n1.display();
