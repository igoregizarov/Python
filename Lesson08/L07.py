class Complex_number:
    def __init__(self, numb=1 + 2j):
        self.numb = numb

    def __add__(self, other):
        return Complex_number(self.numb + other.numb)

    def __mul__(self, other):
        return Complex_number(self.numb * other.numb)

    def __str__(self):
        return f'{self.numb}'


m1 = Complex_number()
m2 = Complex_number()
print(m1 + m2)
print(m1 * m2)


