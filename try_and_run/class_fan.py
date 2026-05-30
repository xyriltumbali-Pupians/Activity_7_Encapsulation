class Fan:
    
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self):

    def display(self):
        print("Speed:", self._speed)
        print("Radius:", self._radius)
        print("Color:", self._color)
        print("On:", self._on)
        print()