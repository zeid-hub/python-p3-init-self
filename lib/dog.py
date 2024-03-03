#!/usr/bin/env python3

class Dog:
    def  __init__(self, name, breed = "Mutt"):    #The breed will  be set to Mutt if not provided.
        self.name = name
        self.breed = breed
fido = Dog("Fido", "Dalmatian")  #The breed will be set  to Dalmatian(the argument passed) for Fido.

print(f"{fido.name} is a {type(fido).__name__} and the breed is of a  {fido.breed}.")