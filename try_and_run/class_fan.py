class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):
        self.__speed = Fan.SLOW
        self.__on = False
        self.__radius = 5
        self.__color = "blue"

    
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

    def display(self):
        print("Speed:", self.__speed)
        print("Radius:", self.__radius)
        print("Color:", self.__color)
        print("On:", self.__on)
        print()

fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

fan1.display()
fan2.display()