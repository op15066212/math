from C import Complex


class Poly:
    def __init__(self, coe=None):
        if coe is None:
            coe = [0]
        if not isinstance(coe, list):
            coe = [coe]
        if len(coe) > 0 and not isinstance(coe[0], Complex):
            temp = [Complex() for _ in range(len(coe))]
            for i in range(len(coe)):
                temp[i] = Complex(coe[i])
            coe = temp
        self.cof = coe
        self.clear()

    def __getitem__(self, key):
        return self.cof[key]

    def degree(self):
        i = len(self.cof) - 1
        while i > 0 and self[i].length() == 0:
            i -= 1
        return i

    def clear(self):
        m = self.degree() + 1
        while len(self.cof) > m:
            self.cof.pop()

    def evaluate(self, x):
        if not isinstance(x, Complex):
            x = Complex(x)
        res = Complex()
        for i in range(len(self.cof) - 1, -1, -1):
            res = res * x + self[i]
        return res

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        n = max(len(self.cof), len(other.cof))
        res = [Complex() for _ in range(n)]
        for i in range(n):
            a = self[i] if i < len(self.cof) else Complex()
            b = other[i] if i < len(other.cof) else Complex()
            res[i] = a + b
        return Poly(res)

    def __sub__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        n = max(len(self.cof), len(other.cof))
        res = [Complex() for _ in range(n)]
        for i in range(n):
            a = self[i] if i < len(self.cof) else Complex()
            b = other[i] if i < len(other.cof) else Complex()
            res[i] = a - b
        return Poly(res)

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        n = len(self.cof) + len(other.cof) - 1
        res = [Complex() for _ in range(n)]
        for i in range(len(self.cof)):
            for j in range(len(other.cof)):
                res[i + j] += self[i] * other[j]
        return Poly(res)

    def __imul__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        temp = self * other
        return temp

    def __iadd__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        temp = self + other
        return temp

    def __isub__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        temp = self - other
        return temp

    def __ifloordiv__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        temp = self // other
        return temp

    def __imod__(self, other):
        if not isinstance(other, Poly):
            other = Poly(other)
        temp = self % other
        return temp

    def __pow__(self, power, modulo=None):
        n = power
        bas = Poly(self.cof)
        res = Poly([1])
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    def __floordiv__(self, other):
        m = self.degree()
        n = other.degree()
        if m < n:
            return Poly()
        quotient = [Complex() for _ in range(m - n + 1)]
        remainder = self[:m + 1]
        for i in range(m - n, -1, -1):
            q = remainder[i + n] // other[n]
            quotient[i] = q
            for j in range(n + 1):
                remainder[i + j] -= q * other[j]
        return Poly(quotient)

    def __mod__(self, other):
        m = self.degree()
        n = other.degree()
        if m < n:
            return Poly(self.cof)
        quotient = [Complex() for _ in range(m - n + 1)]
        remainder = self[:m + 1]
        for i in range(m - n, -1, -1):
            q = remainder[i + n] // other[n]
            quotient[i] = q
            for j in range(n + 1):
                remainder[i + j] -= q * other[j]
        return Poly(remainder)

    def __neg__(self):
        temp = self.cof
        for i in range(len(self.cof)):
            temp[i] = -temp[i]
        return Poly(temp)

    def __str__(self):
        if self.degree() == 0:
            return str(self[0])
        arr = []
        for i in range(len(self.cof)):
            if len(self.cof) > 1 and self[i].length() == 0:
                continue
            if i == 0:
                arr.append([str(self[i]), ""])
            elif i == 1:
                if self[i] == 1:
                    arr.append(["", "x"])
                else:
                    arr.append([str(self[i]), "x"])
            else:
                if self[i] == 1:
                    arr.append(["", "x^" + str(i)])
                else:
                    arr.append([str(self[i]), "x^" + str(i)])
        sb = ""
        sb += "["
        for i in range(len(arr) - 1, -1, -1):
            if i == 0:
                sb += str(arr[i][0]) + str(arr[i][1])
            else:
                sb += str(arr[i][0]) + str(arr[i][1]) + " + "
        sb += "]"
        return sb


if __name__ == '__main__':
    a = Poly([1, 2])
    b = Poly([3, 4, 5])
    print(a)
    print(b)
    print()
    print(a + b)
    print(a - b)
    print(a * b)
    print()
    print(b // a)
    print(b % a)
    print(b // a * a + b % a)
