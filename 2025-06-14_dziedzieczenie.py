class A:
    def method (self):
        print("metoda z klasy A")



class B:
    def method (self):
        print("metoda z klasy B")


a=A()
a.method()

b=B()
b.method()


class C(A,B):
    """

    """
c=C()
c.method()

print(C.__mro__)


