import pickle;
'''
dumps - object to binary
loads - binary to object
dump  - object to binary but saves to file
load  - binary to object by loading from file
'''

class test():
    def __init__(self):
        self.i = 10;
        self.f = 12.345;
        self.b = True;
        self.s = "TEST DATA";

    def display(self):
        print("{}, {}, {}, {}".format(self.i, self.f, self.b, self.s));

# t1 = test();
# file = open("test.dat", "wb");
# pickle.dump(t1, file);
# file.close();

file = open("test.dat", "rb");
t2 = pickle.load(file);
print(type(t2));
t2.display();
