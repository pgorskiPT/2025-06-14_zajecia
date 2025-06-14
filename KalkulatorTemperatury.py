class KalkulatorTemperatur:
    @staticmethod
    def c_to_f(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5 / 9


print(KalkulatorTemperatur.c_to_f(30.0))
print(KalkulatorTemperatur.f_to_c(86.0))

#dodane testy
assert  86.0 == KalkulatorTemperatur.c_to_f(30.0)
assert  100.0 == KalkulatorTemperatur.f_to_c(212.0)

