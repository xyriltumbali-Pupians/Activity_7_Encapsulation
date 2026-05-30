class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):
        self.__speed = Fan.SLOW
        self.__on = False
        self.__raduis = 5      
        self.__color = "blue"

    def display(self):
        print("Speed:", self.__speed)
        print("Radius:", self.__radius)   
        print("Color:", self.__color)
        print("On:", self.__on)
        print()


fan1 = Fan()
fan1.display()