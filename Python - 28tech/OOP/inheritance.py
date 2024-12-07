class person:
    def greet(self):
        print("Hello, my name is Quyen!")
class student (person):
    pass
if __name__ == "__main__":
    p = person()
    p.greet()
    s = student()
    s.greet()