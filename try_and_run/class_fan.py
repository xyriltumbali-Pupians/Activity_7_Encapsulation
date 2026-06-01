class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        self.__oscillating = False
        self.__timer = 0

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            print("Invalid speed!")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive.")

    def set_color(self, color):
        self.__color = color

    def set_on(self, on):
        self.__on = on

    def set_oscillating(self, state):
        self.__oscillating = state

    def set_timer(self, minutes):
        if minutes >= 0:
            self.__timer = minutes
        else:
            print("Timer cannot be negative.")

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def is_on(self):
        return self.__on

    def get_timer(self):
        return self.__timer

    def is_oscillating(self):
        return self.__oscillating

    def toggle_power(self):
        self.__on = not self.__on

    def increase_speed(self):
        if self.__speed < Fan.FAST:
            self.__speed += 1

    def decrease_speed(self):
        if self.__speed > Fan.SLOW:
            self.__speed -= 1

    def get_speed_name(self):
        if self.__speed == Fan.SLOW:
            return "SLOW"
        elif self.__speed == Fan.MEDIUM:
            return "MEDIUM"
        elif self.__speed == Fan.FAST:
            return "FAST"

    def get_power_consumption(self):
        if not self.__on:
            return 0
        elif self.__speed == Fan.SLOW:
            return 20
        elif self.__speed == Fan.MEDIUM:
            return 35
        else:
            return 65

    def display(self):
        print("Speed:", self.get_speed_name())
        print("Radius:", self.__radius)
        print("Color:", self.__color)
        print("Power:", "ON" if self.__on else "OFF")
        print("Oscillating:", self.__oscillating)
        print("Timer:", self.__timer, "minutes")
        print("Power Consumption:", self.get_power_consumption(), "Watts")
        print()

    def __str__(self):
        return (
            f"Fan(Speed={self.get_speed_name()}, "
            f"Radius={self.__radius}, "
            f"Color={self.__color}, "
            f"Power={'ON' if self.__on else 'OFF'})"
        )


fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)
fan1.set_oscillating(True)
fan1.set_timer(60)

fan2 = Fan()
fan2.set_speed(Fan.MEDIUM)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

print("=== FAN 1 ===")
fan1.display()

print("=== FAN 2 ===")
fan2.display()

print("Increasing Fan 2 Speed...")
fan2.increase_speed()
fan2.toggle_power()

print("\n=== FAN 2 AFTER CHANGES ===")
fan2.display()

print(fan1)
print(fan2)