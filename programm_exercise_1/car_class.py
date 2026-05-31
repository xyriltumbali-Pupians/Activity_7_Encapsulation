class Car:

    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5 

    def get_speed(self):
        return self.__speed

car = Car(2024, "Toyota")
    
print("Accelerating:")
for i in range(5):
    car.accelerate()
    print("Current speed:", car.get_speed())

print("\nBraking:")
for i in range(5):
    car.brake()
    print("Current speed:", car.get_speed())
