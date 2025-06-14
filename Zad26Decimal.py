from decimal import Decimal
print(type('0.1'))
x = Decimal("0.1")
y = Decimal("0.2")
z = x + y

print(y)
print(x)
print(z)


print(type(0.1))
u= Decimal(0.1)
print(u)

print(x==y)
print(x==x)

add=x+y
print(add)



#dzialaania z zaokragleneim mozna nie stosowac metod i


x = Decimal("1.3466")

# Zaokrąglenie do dwóch miejsc dziesiętnych w górę
rounded = x.quantize(Decimal("0.01"))
print(rounded)
rounded = x.quantize(Decimal("0.01"))

print(rounded)
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP

# Tworzenie obiektu Decimal
x = Decimal("2.3466")

# Zaokrąglenie do dwóch miejsc dziesiętnych w górę
rounded_up = x.quantize(Decimal("0.01"), rounding=ROUND_UP)

# Zaokrąglenie do dwóch miejsc dziesiętnych w dół
rounded_down = x.quantize(Decimal("0.01"), rounding=ROUND_DOWN)

# Zaokrąglenie do najbliższej wartości (standardowe zaokrąglanie)
rounded_half_up = x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(rounded_up)      # Wynik: 2.35
print(rounded_down)    # Wynik: 2.34
print(rounded_half_up) # Wynik: 2.35
