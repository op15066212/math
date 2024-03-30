from Poly import Poly


def gcd(a, b):
    if b.degree() == 0 and b[0] == 0:
        return a
    else:
        return gcd(b, a % b)


class PolyF:
    def __init__(self, x=Poly(0), y=Poly(1)):
        if not isinstance(x, Poly):
            x = Poly(x)
        if not isinstance(y, Poly):
            y = Poly(y)
        self.x = x
        self.y = y
        self.simplify()

    def evaluate(self, n):
        return self.x.evaluate(n) // self.y.evaluate(n)

    def __str__(self):
        if self.y.degree() == 0 and self.y[0] == 1:
            return f"{self.x}"
        else:
            return f"{self.x} / {self.y}"

    def simplify(self):
        if self.x == 0:
            self.y = 1
            return
        if self.y == 0:
            raise ValueError("分母不能为零")
        GCD = gcd(self.x, self.y)
        self.x //= GCD
        self.y //= GCD
        if self.y[self.y.degree()] < 0:
            self.x = -self.x
            self.y = -self.y

    def __add__(self, rhs):
        if not isinstance(rhs, PolyF):
            rhs = PolyF(rhs)
        nx = (self.x * rhs.y) + \
             (rhs.x * self.y)
        ny = self.y * rhs.y
        res = PolyF(nx, ny)

        return res

    def __sub__(self, rhs):
        if not isinstance(rhs, PolyF):
            rhs = PolyF(rhs)
        nx = (self.x * rhs.y) - \
             (rhs.x * self.y)
        ny = self.y * rhs.y
        res = PolyF(nx, ny)

        return res

    def __mul__(self, rhs):
        if not isinstance(rhs, PolyF):
            rhs = PolyF(rhs)
        nx = self.x * rhs.x
        ny = self.y * rhs.y
        res = PolyF(nx, ny)
        return res

    def __pow__(self, power, modulo=None):
        n = power
        bas = PolyF(self.x, self.y)
        res = PolyF(1)
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    def __floordiv__(self, rhs):
        if not isinstance(rhs, PolyF):
            rhs = PolyF(rhs)
        nx = self.x * rhs.y
        ny = self.y * rhs.x
        res = PolyF(nx, ny)
        return res

    def __iadd__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        temp = self + other
        return temp

    def __isub__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        temp = self - other
        return temp

    def __imul__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        temp = self * other
        return temp

    def __ifloordiv__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        temp = self // other
        return temp

    def length(self):
        return self.x.evaluate(1) // self.y.evaluate(1)

    # =
    def __eq__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        return self.x == other.x and self.y == other.y

    # <
    def __lt__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        return self.length() < other.length()

    # >
    def __gt__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        return other < self

    # >=
    def __ge__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        return not self < other

    # <=
    def __le__(self, other):
        if not isinstance(other, PolyF):
            other = PolyF(other)
        return not other < self

    def __abs__(self):
        a = self.x
        b = self.y
        if a[a.degree()] < 0:
            a = -a
        if b[b.degree()] < 0:
            b = -b
        return PolyF(a, b)

    def __neg__(self):
        temp = PolyF(self.x, self.y)
        return PolyF(-1) * temp


if __name__ == "__main__":
    a = PolyF(3, 5)
    b = PolyF(5, 7)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a ** 5)
