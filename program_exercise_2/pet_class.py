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

while True:
    my_pet = Pet()

    name = input(f"Enter your pet's name: ")
    animal_type = input(f"Enter your pet's type (Dog, Cat, Bird, etc.): ")
    age = int(input(f"Enter your pet's age: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    history.append(my_pet)

    another = input(f"Add another pet? (yes/no): ").lower()
    if another != "yes":
       break

print("=== PET HISTORY ===")
for i, pet in enumerate(history, start=1) 
print(f"Pet {i}")
print("Name:", pet.get_name())
print("Animal Type:", pet.get_animal_type())
print("Age:", pet.get_age())

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

history.append(my_pet)

another = input(f"Add another pet? (yes/no): ").lower()
if another != "yes":
   break