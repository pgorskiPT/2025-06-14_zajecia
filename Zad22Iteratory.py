"""
 w Pythonie to obiekt, który pozwala na sekwencyjne przechodzenie przez
  elementy kolekcji (takiej jak lista, krotka, zbiór czy słownik).
  W uproszczeniu, iterator pozwala na "iterowanie" (przechodzenie)
  przez dane bez potrzeby znajomości ich wewnętrznej struktury.

Co to jest "iteracja"?
Iteracja oznacza proces przetwarzania elementów kolekcji w ustalonej kolejności.
W Pythonie, podczas iteracji, używamy takich konstrukcji jak:

Pętla for

Funkcja next()

Zrozumienie iteratorów
Iterator to obiekt, który:

Implementuje metodę __iter__() – która zwraca obiekt iteratora.

Implementuje metodę __next__() – która zwraca kolejny element w sekwencji.

Jeśli elementy się skończą, rzuca wyjątek StopIteration, sygnalizując koniec iteracji.
"""
from win32pdh import counter_status_error

lista = [1, 2, 3, 4]

# Tworzymy iterator
iterator = iter(lista)

print(iterator)
print(type(iterator))
# Wyciąganie kolejnych elementów za pomocą next()
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
#print(next(iterator))  # Zgłosi StopIteration
# znaczy ze itertor nie ma juz elementow do odczytania;
# to oznacza ze iterator zwraca elementy raz,
# jak widac lista sie skonczyla i iterator po jej przejscu skonczyl iteracje

for x in range(5):
    print(x, end="|")
print()

class Count:
    """

    """
    def __init__(self,low,high):
        self.current=low
        self.high=high
    def __iter__(self):
        return  self

    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            self.current+=1
            return self.current -1

print("----------------")
counter1=Count(1,6)
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))

print("-----------------")
while True:
    try:
        numer =next(counter)
        print(numer)
    except StopIteration:
        break
counter2=Count(1,5)
print(next(counter2))
print(next(counter2))
print(next(counter2))