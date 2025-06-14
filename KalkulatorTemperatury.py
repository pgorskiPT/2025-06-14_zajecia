class KalkulatorTemperatur:
    @staticmethod
    def c_na_f(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def f_na_c(f):
        return (f - 32) * 5 / 9



c = 100
f = KalkulatorTemperatur.c_na_f(c)
print(f"{c} C = {f:.2f} F")

f = 212
c = KalkulatorTemperatur.f_na_c(f)
print(f"{f} F = {c:.2f} C")
