from functools import cache

from C import Complex
from F import Fraction
from M import M
from Mpro import Mpro
from Poly import Poly
from PolyF import PolyF


@cache
def fact(n: int) -> int:
    return A(n, n)


@cache
def A(n: int, m: int) -> int:
    if n == 0 or m == 0 or n == 1:
        return 1
    if m == 1:
        return n
    k = m // 2
    v1 = A(n, k)
    v2 = A(n - k, m - k)
    return v1 * v2


@cache
def C(n: int, m: int) -> int:
    if n == 0 or m == 0 or n == 1 or m == n:
        return 1
    if m == 1:
        return n
    if m > n - m:
        return C(n, n - m)
    k = m // 2
    v1 = C(n, k)
    v2 = C(m, k)
    v3 = C(n - k, m - k)
    return v1 * v3 // v2


@cache
def H(n: int) -> int:
    return C(2 * n, n) // (n + 1)


@cache
def B(n: int) -> Fraction:
    res = Fraction()
    for i in range(0, n):
        for j in range(n - i):
            v1 = Fraction(C(n, j))
            v2 = Fraction(i ** (n - 1))
            v3 = Fraction((-1) ** (i + 1))
            val = v1 * v2 * v3
            res += val
    p1 = Fraction(2 ** n)
    p2 = Fraction(2 ** n) - 1
    res *= Fraction(n) // p1 // p2
    return res


@cache
def Z(n: int) -> Fraction:
    res = B(n + 1) * ((2 ** (n + 1)) - 1) // (n + 1)
    return res


@cache
def zeta1(n: int) -> Fraction:
    if n == 0:
        return Fraction(-1, 2)
    res = Z(n)
    res //= Fraction(1) - (2 ** (n + 1))
    return res


@cache
def zeta2(n: int) -> Fraction:
    res = B(n)
    p1 = Fraction((-1) ** (n // 2 + 1))
    p2 = Fraction(2 ** n, 2 * fact(n))
    res *= p1 * p2
    return res


@cache
def zeta3(x: int, n: int, j: int) -> Fraction:
    if j < 1 or j > n:
        print("1 <= j <= n")
        return Fraction(-1)
    res = Fraction()
    for k in range(n + 1):
        v1 = C(n, k)
        v2 = (x - k) ** (n - j)
        v3 = (-1) ** k
        res += v1 * v2 * v3
    return res


@cache
def powsum(n: int) -> PolyF:
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(i + 1):
            m[i][j] = C(i + 1, j)
            if (i - j) % 2 == 1:
                m[i][j] = -m[i][j]
    p = [[PolyF()] for _ in range(n + 1)]
    for i in range(n + 1):
        temp = [0 for _ in range(i + 2)]
        temp[i + 1] = 1
        p[i][0] = PolyF(temp)
    a = Mpro(m)
    b = Mpro(p)
    t = a.inverse() * b
    return t[n][0]


@cache
def powmul(n: int) -> PolyF:
    if n == 0:
        return PolyF(1)
    a = [[PolyF() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i - j != 0:
                a[i][j] = powsum(i - j)
            else:
                a[i][j] = PolyF(i + 1)
            if j % 2 == 1:
                a[i][j] = -a[i][j]
    b = [[PolyF()] for _ in range(n)]
    for i in range(n):
        b[i][0] = powsum(i + 1)
    m = Mpro(a)
    p = Mpro(b)
    t = m.inverse() * p
    return t[n - 1][0]


@cache
def zeta1mulc(n: int) -> Fraction:
    a = [[Fraction() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i - j != 0:
                a[i][j] = zeta1(i - j)
            else:
                a[i][j] = Fraction(i + 1)
            if j % 2 == 1:
                a[i][j] = -a[i][j]
    b = [[Fraction()] for _ in range(n)]
    for i in range(n):
        b[i][0] = zeta1(i + 1)
    m = M(a)
    p = M(b)
    t = m.inverse() * p
    return t[n - 1][0]


@cache
def inv_zeta1mulc(n: int) -> Complex:
    if n == 1:
        return G(1)
    a = [[Complex() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i - j != 0:
                a[i][j] = inv_zeta1mulc(i - j)
            else:
                a[i][j] = Complex(i + 1)
            if j % 2 == 1:
                a[i][j] = -a[i][j]
    b = [[Complex()] for _ in range(n)]
    for i in range(n):
        b[i][0] = G(i + 1)
    m = M(a)
    p = M(b)
    t = m * p
    return t[n - 1][0]


@cache
def inv2_zeta1mulc(n: int):
    if n == 1:
        return zeta1mulc(1)
    a = [[Complex() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i - j != 0:
                a[i][j] = inv2_zeta1mulc(i - j)
            else:
                a[i][j] = Complex(i + 1)
            if j % 2 == 1:
                a[i][j] = -a[i][j]
    b = [[Fraction()] for _ in range(n)]
    for i in range(n):
        b[i][0] = zeta1mulc(i + 1)
    m = M(a)
    p = M(b)
    t = m * p
    return t[n - 1][0]


@cache
def inv3_zeta1mulc(n: int):
    if n == 1:
        return unlimited2(powmul(1))
    a = [[Complex() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if i - j != 0:
                a[i][j] = inv3_zeta1mulc(i - j)
            else:
                a[i][j] = Complex(i + 1)
            if j % 2 == 1:
                a[i][j] = -a[i][j]
    b = [[Complex()] for _ in range(n)]
    for i in range(n):
        b[i][0] = unlimited2(powmul(i + 1))
    m = M(a)
    p = M(b)
    t = m * p
    return t[n - 1][0]


@cache
def G(n: int):
    return Complex(1) // fact(2 * n + 1)


@cache
def F(n: int) -> Fraction:
    return Fraction((-1) ** n, n + 1)


@cache
def unlimited(it: Poly) -> Complex:
    if it.degree() == 0:
        return it[0]
    arr = []
    for i in range(len(it.cof)):
        arr.append([it[i], F(i)])
    sb = Complex()
    for i in range(len(arr) - 1, -1, -1):
        sb += arr[i][0] * arr[i][1]
    return sb


def unlimited2(it: PolyF) -> Complex:
    return unlimited(it.x) // unlimited((it.y))


if __name__ == '__main__':
    for i in range(1, 7):
        print("第" + str(i) + "个伯努利数:", B(i))
    print()
    for i in range(7):
        print("黎曼函数自变量(" + str(-i) + "):", zeta1(i))
    print()
    for i in range(2, 10, 2):
        print("黎曼函数自变量(" + str(i) + "):", str(zeta2(i)) + " * (pi)^" + str(i))
    print()
    for i in range(7):
        print("S(" + str(i) + "):", unlimited2(powsum(i)))
    print()
    for i in range(7):
        print("T(" + str(i) + "):", powmul(i))
    print()
    for i in range(7):
        print("T(" + str(i) + "):", unlimited2(powmul(i)))
    print()
    for i in range(1, 7):
        print("黎曼函数系数T(" + str(-i) + "):", zeta1mulc(i))
    print()
    for i in range(1, 7):
        print("黎曼函数自变量(" + str(i) + "):", inv_zeta1mulc(i))
    print()
    for i in range(1, 7):
        print("黎曼函数2自变量(" + str(i) + "):", inv2_zeta1mulc(i))
    print()
    for i in range(1, 7):
        print("黎曼函数3自变量(" + str(i) + "):", inv3_zeta1mulc(i))
    print()
    P = Poly(1)
    for i in range(11):
        P *= Poly([i, 1])
    print(P)
    print()
    for i in range(1, 7):
        print("T(" + str(i) + "):", powmul(i).evaluate(10))
    # for i in range(100, 107):
    #     for j in range(100, 107):
    #         for k in range(90, 97):
    #             print(zeta3(i, j, k), end=' ')
