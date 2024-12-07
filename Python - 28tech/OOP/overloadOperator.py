class sophuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, other):
        tmp1 = self.thuc + other.thuc
        tmp2 = self.ao + other.ao
        return sophuc(tmp1, tmp2)
    def __sub__(self, other):
        tmp1 = self.thuc - other.thuc
        tmp2 = self.ao - other.ao
        return sophuc(tmp1, tmp2)
    def __eq__(self, value):
        return self.thuc == value.thuc and self.ao == value.ao
    def __str__(self):
        return f"{self.thuc} + {self.ao}j"
if __name__ == "__main__":
    s1 = sophuc(2, 3)
    s2 = sophuc(3, 1)
    s3 = s1 + s2
    s4 = s1 - s2
    print(s3)
    print(s4)
    print(s3 == s4)