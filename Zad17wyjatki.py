# tak jak dziedziczmy po klasei i liscie
#tak mozemy tez dziedziczyc po wyjatku
# python 3 powstal aby wszystko bylo obiektem

class MyExepction(Exception):
    def __init__(self, message):
        super().__init__(message)


#raise ZeroDivisionError("Nie dziel przez zero")

#raise MyExepction("wyjactek od radka")
"""
Traceback (most recent call last):
  File "C:\Szkolenia\2025-05 BotCampPython\2025-06-14_zajecia\Zad17wyjatki.py", line 12, in <module>
    raise MyExepction("wyjactek od radka")
__main__.MyExepction: wyjactek od radka
"""


try:
    x = int(input("Podaj liczbę całkowitą dodatnią: "))
    if x <= 0:  # Liczba musi być większa od zera
        print("Liczba musi być większa od zera.")
        raise MyException("Liczba musi być dodatnia.")  # Rzucamy wyjątek

except ValueError:
    print("Wprowadzono nieprawidłową wartość. ")
except MyException as e:
    print(f"Błąd: {e}")

else:
    print(f"Podałeś liczbę dodatgnią: {x}")
finally:
    print("wprowadz kolejne dane")