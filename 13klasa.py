lista=[1,2,3,4,5]

with open ('lista.txt', 'w') as file:
    file.write(str(lista))

with open ('lista.txt', 'r') as file:
    odczyt =file.read()
    lista_odczytane= eval(odczyt)
    print(odczyt)
    print(type(odczyt))

    print(lista_odczytane)
    print(type(lista_odczytane))

#pickle - serializacja i deserializacja obiektow

import pickle
lista2=[1,2,3,4,5]
with open('lista2.pkl', 'wb') as f:
    pickle.dump(lista2, f)
#zapisalo nam do pliku w postaci bajtowej


with open ('lista2.pkl', 'rb') as fh:
    odczyt2 =pickle.load(fh)
    print(odczyt2)
    print(type(odczyt2))


import ast


with open ('lista3.txt', 'w') as file:
    file.write(str(lista))

with open ('lista3.txt', 'r') as file:
    odczyt3 =file.read()
    lista_odczytane=ast.literal_eval(odczyt3)
    print(odczyt3)
    print(type(odczyt3))

    print(lista_odczytane)
    print(type(lista_odczytane))