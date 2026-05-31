class Car:

    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.__speed = 0
        self.__max_speed = 120

    def accelerate(self):
        if self.__speed < self.__max_speed:
            self.__speed += 5

        else:
            self.__speed = self.__max_speed
       
    def brake(self):
        if self.__speed >= 5:
           self.__speed -= 5 
        else:
            self.__speed = 0

    def stop(self):
        self.__speed = 0        

    def get_speed(self):
        return self.__speed
    
    def show_info(self):
        return f"{self.year_model} {self.make} | Speed: {self.__speed} km/h"

car = Car(2026, "Toyota")

print(car.show_info())

print("\nAccelerating:")
for i in range(5):
    car.accelerate()
    print("Current speed:", car.get_speed())

print("\nBraking:")
for i in range(5):
    car.brake()
    print("Current speed:", car.get_speed())

print("\nFinal Info:")
print(car.show_info())