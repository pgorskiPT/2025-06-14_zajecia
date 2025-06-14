class MyNumber:
    def __init__(self,value):
        self.value=value



num1=MyNumber(5)
num2=MyNumber(15)

print(5<15)# True

#print (num1 <num2)
"""
Traceback (most recent call last):
  File "C:\Szkolenia\2025-05 BotCampPython\2025-06-14_zajecia\Zad23Klasy.py", line 12, in <module>
    print (num1 <num2)
TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
True
"""

print (num1.value <num2.value)#True
print (10 *"=")


class MyNumber2:
    def __init__(self,value):
        self.value=value
    #ta metoda wykona sie przy porownaniu
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other): # real signature unknown
        """ Return self==value. """
        return self.value == other.value
num3=MyNumber2(5)
num4=MyNumber2(15)

print(5<15)# True

print (num3 <num4)


print (num1 ==num3)

print (10 *"=")
