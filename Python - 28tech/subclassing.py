class person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
class student(person):
    def __init__(self, name, birth, grade):
        person.__init__(self, name, birth) # cách 1
        # super().__init__(self, name, birth) cách 2
        self.grade = grade
    def __str__(self):
        return f"{self.name} {self.birth} {self.grade:.2f}"
    
if __name__ == "__main__":
    s = student("John", 1990, 3.5)
    print(s)  # John 1990 3.50