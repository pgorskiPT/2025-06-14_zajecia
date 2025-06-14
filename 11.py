class MyClass:
    counter =0

    @classmethod
    def increment_counter(cls):
        cls.counter +=1
        return cls.counter


print(MyClass.increment_counter())
print(MyClass.increment_counter())
print(MyClass.increment_counter())
c=MyClass()
print(c.counter)

print(c.increment_counter())
c.counter=0
print(c.counter)
c.increment_counter()
print(c.counter)
print(MyClass.counter)

c2=MyClass()
print(c2.increment_counter())


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko =nazwa_pelna.split()


osoba1=Osoba("Jan","Kowalski")
print(osoba1.imie, osoba1.nazwisko)
imie,nazwisko ="Jan Kowalski".split()
print(imie, ":", nazwisko)


osoba2=Osoba("Zenon","Nowak")
print(osoba2.imie, osoba2.nazwisko)


print("Przemek: Górski".split(":"))