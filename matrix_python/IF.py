from F import Fraction


class IF:
    def __init__(self, f=None, p=None):
        if f is None:
            f = Fraction()
        if p is None:
            p = 0
        if not isinstance(f, Fraction):
            f = Fraction(f)
        if not isinstance(p, int):
            p = int(p)
        self.f = f
        self.p = p
        self.clear()

    def clear(self):
        i = int(self.f.length())
        self.p += i
        self.f = Fraction(self.f.x - self.f.y * i, self.f.y)

    def __add__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return IF(self.f + other.f, self.p + other.p)

    def __sub__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return IF(self.f - other.f, self.p - other.p)

    def __mul__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return IF(self.ToF() * other.ToF())

    def __pow__(self, power, modulo=None):
        n = power
        bas = IF(self.f, self.p)
        res = IF(Fraction(1))
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    def __floordiv__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return IF(self.ToF() // other.ToF())

    def __iadd__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        temp = self + other
        return temp

    def __isub__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        temp = self - other
        return temp

    def __imul__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        temp = self * other
        return temp

    def __ifloordiv__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        temp = self // other
        return temp

    def ToF(self):
        return self.f + self.p

    def inverse(self):
        q = self.ToF()
        q = Fraction(q.y, q.x)
        return IF(q)

    def length(self):
        return self.ToF().length()

    def __eq__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return self.f == other.f and self.p == other.p

    # <
    def __lt__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return self.length() < other.length()

    # >
    def __gt__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return other < self

    # >=
    def __ge__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return not self < other

    # <=
    def __le__(self, other: any):
        if not isinstance(other, IF):
            other = IF(other)
        return not other < self

    def LoopStructure1(self):
        n = self.f.x if self.f.x > 0 else -self.f.x
        m = self.f.y
        mp = {}
        i = 0
        while n > 0:
            mp[n] = i
            n *= 10
            if n <= 0:
                return []
            n %= m
            if n in mp:
                return [mp[n], len(mp) - 1]
            i += 1
        return []

    def LoopStructure2(self):
        loop = self.LoopStructure1()
        if (len(loop) == 0):
            return ""
        n = self.f.x if self.f.x > 0 else -self.f.x
        m = self.f.y
        mp = {}
        i = 0
        res = ""
        while n > 0:
            mp[n] = i
            n *= 10
            if n <= 0:
                return res
            if i >= loop[0] and i <= loop[1]:
                res += str(n // m)
            n %= m
            if n in mp:
                return res
            i += 1
        return res

    def __str__(self):
        if self.f == Fraction():
            return str(self.p)
        if self.p == 0:
            return str(self.f)
        return "[" + str(self.p) + " + " + str(self.f) + "]"

    def __neg__(self):
        return IF(self.f, self.p) * IF(-1)


if __name__ == "__main__":
    print(1324 / 19)
    a = IF(Fraction(1324, 19))
    print(a)
    print(a ** 2)
    print(a.LoopStructure1())
    print(a.LoopStructure2())
    a = IF(Fraction(7, 20), 2)
    b = IF(Fraction(3, 4), 4)
    c = IF(Fraction(1, 2), 4)
    d = IF(Fraction(20, 100)) + IF(Fraction(1, 3))
    print(a // (b - c * d))
