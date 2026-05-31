class Car:

    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
       self.__speed += 5

    def brake(self):
        self.__speed -= 5 
