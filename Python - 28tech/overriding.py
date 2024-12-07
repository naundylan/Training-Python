class person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    def show(self):
        return f"{self.name} {self.birth}"
class student(person):
    def __init__(self, name, birth, gpa):
        super().__init__(name, birth)
        self.gpa = gpa
    def show(self):
        return person.show(self) + ' ' + f"{self.gpa:.2f}"

if __name__ == "__main__":
    s = student("John", "1990", 3.5)
    print(s.show())