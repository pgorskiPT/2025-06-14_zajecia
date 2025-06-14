# z zadania 18 modyfikujemy odniesienia

class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code=err_code



class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code =100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code =200)


class MyValidator:


    @staticmethod
    def is_int(value, name):
        if not isinstance(value,int):
            raise MyTypeError (f"{name}myst by integer")

    @staticmethod
    def not_zero(value, name):
        if value==0:
            raise MyValueError  (f"{name}connot by zero")


def my_function(x:int, y:int) -> float:
    MyValidator.is_int(x, "x")
    MyValidator.is_int(y, "y")
    MyValidator.not_zero(y, "y")

#
# def my_function(x:int, y:int) -> float:
#     if not isinstance(x,int):
#         raise MyTypeError("x myst by integer")
#     if not isinstance(y,int):
#         raise MyTypeError("y myst by integer")
#     if y==0:
#         raise MyValueError ('y connot by zero')

    return x / y

try:
    result = my_function(5,6)
except MyTypeError as e:
    print("Caught a MyTypeError")
    print("Error code:", e.err_code)

except MyValueError as e:
    print("Caught a MyValueError")
    print("Error code:",  e.err_code)
except Exception as e:
    print("Error", e)
else:
    print( f"Reuslt is : {result}")
finally:
    print ("End")