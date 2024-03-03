#!/usr/bin/env python3

class Person:
    def __init__(self,  name):
        self.name = name
guido = Person("Guido")
jython = Person("Jython")

print(f"{guido.name} and {jython.name} are friends.")

