class Circle:
    pi = 3.14;
    def __init__(self, radius):
        self.radius = radius
    def circumFerence(self):
        circum = 2*Circle.pi*self.radius
        print(f"Circum Ference Of Circle {circum}")
    
    def circleArea(self):
        return Circle.pi*self.radius*self.radius
    
    
circle = Circle(3.5)
circle.circumFerence()
print(f"Area Of Circle is {circle.circleArea()}")