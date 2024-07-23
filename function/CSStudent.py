class CSStudent():
    stream = "cse"
    def __init__(self, roll):
        self.roll = roll
a = CSStudent(100)
b = CSStudent(200)

print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)