from F import Fraction


class Complex:
    def __init__(self, real=None, imag=None):
        if real is None:
            real = Fraction()
        if imag is None:
            imag = Fraction()
        if isinstance(real, int):
            real = Fraction(real)
        if isinstance(imag, int):
            imag = Fraction(imag)
        self.real = real
        self.imag = imag

    # 加法运算符重载
    def __add__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    # 减法运算符重载
    def __sub__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    # 乘法运算符重载
    def __mul__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __pow__(self, power, modulo=None):
        n = power
        bas = Complex(self.real, self.imag)
        res = Complex(Fraction(1))
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    # 除法运算符重载
    def __floordiv__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        denominator = other.real * other.real + other.imag * other.imag
        return Complex((self.real * other.real + self.imag * other.imag) // denominator,
                       (self.imag * other.real - self.real * other.imag) // denominator)

    def __iadd__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        temp = self + other
        return temp

    def __isub__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        temp = self - other
        return temp

    def __imul__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        temp = self * other
        return temp

    def __ifloordiv__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        temp = self // other
        return temp

    def __eq__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return self.real == other.real and self.imag == other.imag

    def length(self):
        a = self.real.length()
        b = self.imag.length()
        return (a * a + b * b) ** 0.5

    # <
    def __lt__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return self.length() < other.length()

    # >
    def __gt__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return other < self

    # >=
    def __ge__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return not self < other

    # <=
    def __le__(self, other: any):
        if not isinstance(other, Complex):
            other = Complex(other)
        return not other < self

    # 转换为字符串
    def __str__(self):
        if self.imag == Fraction(0):
            return str(self.real)
        elif self.real == Fraction(0):
            return str(self.imag)
        elif self.imag == Fraction(1):
            return f"{self.real} + i"
        elif self.imag == Fraction(-1):
            return f"{self.real} - i"
        elif self.imag < Fraction(0):
            return f"{self.real} - {self.imag * Fraction(-1)}i"
        else:
            return f"{self.real} + {self.imag}i"

    def __abs__(self):
        if self.real > Fraction():
            return Complex(self.real, self.imag)
        return Complex(-self.real, -self.imag)

    def __neg__(self):
        temp = Complex(self.real, self.imag)
        return Complex(-1) * temp


if __name__ == "__main__":
    a = Complex(Fraction(1, 2), Fraction(3, 4))
    b = Complex(Fraction(3, 4), Fraction(1, 2))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
