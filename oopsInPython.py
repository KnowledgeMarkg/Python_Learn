class Instructor:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def display(self):
        print(f"My Name is {self.name}")

instructor_1 = Instructor("Kausar", "Bangalore")
print(instructor_1.name +" : "+ instructor_1.address)
instructor_1.display();

instructor_2 = Instructor("Rozi", "Bihar")
print(instructor_2.name +" : "+ instructor_2.address)
