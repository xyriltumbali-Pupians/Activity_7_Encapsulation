class Pet:

    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
      self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

my_pet = Pet()

name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's type (Dog, Cat, Bird, etc.): ")
age = int(input("Enter your pet's age: "))

my_petset_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("\nPet Information")
print("Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())
