def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Fraction:
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        self.simplify()

    def __str__(self):
        if self.y == 1:
            return f"{self.x}"
        else:
            return f"({self.x}/{self.y})"

    def ToIF(self):
        from IF import IF
        return IF(self)

    def simplify(self):
        if self.x == 0:
            self.y = 1
            return
        if self.y == 0:
            raise ValueError("分母不能为零")
        GCD = gcd(self.x, self.y)
        self.x //= GCD
        self.y //= GCD
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

    def __add__(self, rhs: any):
        if not isinstance(rhs, Fraction):
            rhs = Fraction(rhs)
        nx = (self.x * rhs.y) + \
             (rhs.x * self.y)
        ny = self.y * rhs.y
        res = Fraction(nx, ny)

        return res

    def __sub__(self, rhs: any):
        if not isinstance(rhs, Fraction):
            rhs = Fraction(rhs)
        nx = (self.x * rhs.y) - \
             (rhs.x * self.y)
        ny = self.y * rhs.y
        res = Fraction(nx, ny)

        return res

    def __mul__(self, rhs: any):
        if not isinstance(rhs, Fraction):
            rhs = Fraction(rhs)
        nx = self.x * rhs.x
        ny = self.y * rhs.y
        res = Fraction(nx, ny)
        return res

    def __pow__(self, power, modulo=None):
        n = power
        bas = Fraction(self.x, self.y)
        res = Fraction(1)
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    def __floordiv__(self, rhs: any):
        if not isinstance(rhs, Fraction):
            rhs = Fraction(rhs)
        nx = self.x * rhs.y
        ny = self.y * rhs.x
        res = Fraction(nx, ny)
        return res

    def __iadd__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        temp = self + other
        return temp

    def __isub__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        temp = self - other
        return temp

    def __imul__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        temp = self * other
        return temp

    def __ifloordiv__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        temp = self // other
        return temp

    def length(self):
        return self.x / self.y

    # =
    def __eq__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.x == other.x and self.y == other.y

    # <
    def __lt__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.length() < other.length()

    # >
    def __gt__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return other < self

    # >=
    def __ge__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return not self < other

    # <=
    def __le__(self, other: any):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return not other < self

    def __abs__(self):
        return Fraction(abs(self.x), abs(self.y))

    def __neg__(self):
        temp = Fraction(self.x, self.y)
        return Fraction(-1) * temp


if __name__ == "__main__":
    a = Fraction(3, 5)
    b = Fraction(5, 7)
    print((a + b))
    print((a - b))
    print((a * b))
    print((a // b))
    print(a ** 5)
    a = Fraction(7, 20) + 2
    b = Fraction(3, 4) + 4
    c = Fraction(1, 2) + 4
    d = Fraction(20, 100) + Fraction(1, 3)
    print(a // (b - c * d))
