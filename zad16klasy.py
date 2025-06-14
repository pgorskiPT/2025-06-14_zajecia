"""
Stworzyc slownik, zapisac slownik do pliki i odczytac z pliku za pomoca pickle,
odczytac wartosc klucza ze slownika.
"""
import pickle

my_dict = {
    'name': 'Przemek',
    'surname': 'Kowalski',
    'age': 48,
    'city': 'Piotrków Trybunalski'
}
print(type(my_dict))
print(my_dict)
print(10 * "=")

with open('slownik.pickle', 'wb') as file:
    pickle.dump(my_dict, file)

with open('slownik.pickle', 'rb') as file:
    loaded_dict = pickle.load(file)

print("Odczytany słownik:", loaded_dict)

print(loaded_dict['name'])


