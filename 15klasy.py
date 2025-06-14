import pickle
from dataclasses import dataclass
from zad14 import Person


from dataclasses import  dataclass

# @dataclass
# class Person:
#     first_name:str
#     last_name:str
#     id: int


with open("dane.pickle" , "rb") as file:
    p=pickle.load(file)
print (p)