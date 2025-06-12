#inherit class attributes
class car:
    def __init__(self, name, brand, color,):
        self.name = name
        self.brand = brand
        self.color = color

    def intro(self):
        return f"Your car is {self.name} {self.brand} color {self.color}"
    
class Motor(car):
    def __init__(self, name, brand, color):
        super().__init__(name, brand, color)

    def defIntro(self):
        return f"Your Motorcycle is {self.name} {self.brand} color {self.color}"

class Motor2(car):
    def __init__(self, name, brand, speed, color):
        super().__init__(name, brand, color)
        self.speed = speed
    
    def intro1(self):
        return f"Your Motorcycle is {self.name} {self.brand} max speed of {self.speed} color {self.color}"
    
#user input here

kotse = car( str(input("enter car model: ")), str(input("enter brand: ")), str(input("enter color: ")))
print(kotse.intro())

firstline = Motor( str(input("enter motor model: ")), str(input("enter brand: ")), str(input("enter speed: ")))
print(firstline.defIntro())

secondline = Motor2( str(input("enter motor model: ")), str(input("enter brand: ")), str(input("enter color: ")), str(input("enter speed: ")))
print(secondline.intro1())
