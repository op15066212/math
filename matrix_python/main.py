from functools import lru_cache

# 导入自定义模块中的类和函数
from C import Complex  # 复数类
from F import Fraction  # 分数类
from M import M  # 矩阵类
from Mpro import Mpro  # 矩阵处理类
from Poly import Poly  # 多项式类
from PolyF import PolyF  # 带分数的多项式类


@lru_cache(maxsize=None)  # 使用LRU缓存，maxsize=None表示无限缓存
def fact(n: int) -> int:
    """
    计算n的阶乘。
    数学公式: n! = n * (n-1) * (n-2) * ... * 1
    """
    return A(n, n)


@lru_cache(maxsize=None)
def A(n: int, m: int) -> int:
    """
    计算排列数A(n, m)，即从n个元素中取出m个元素的排列数。
    数学公式: A(n, m) = n! / (n-m)!
    """
    if n == 0 or m == 0 or n == 1:
        return 1
    if m == 1:
        return n
    k = m // 2
    v1 = A(n, k)
    v2 = A(n - k, m - k)
    return v1 * v2


@lru_cache(maxsize=None)
def C(n: int, m: int) -> int:
    """
    计算组合数C(n, m)，即从n个元素中取出m个元素的组合数。
    数学公式: C(n, m) = n! / (m! * (n-m)!)
    """
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


@lru_cache(maxsize=None)
def H(n: int) -> int:
    """
    计算卡特兰数H(n)。
    数学公式: H(n) = C(2n, n) / (n + 1)
    """
    return C(2 * n, n) // (n + 1)


@lru_cache(maxsize=None)
def B(n: int) -> Fraction:
    """
    计算第n个伯努利数B(n)。
    数学公式: B(n) = sum((-1)^i * C(n, i) * i^(n-1)) / (2^n - 1)
    """
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


@lru_cache(maxsize=None)
def Z(n: int) -> Fraction:
    """
    计算Z(n)，与伯努利数相关的函数。
    数学公式: Z(n) = B(n+1) * (2^(n+1) - 1) / (n + 1)
    """
    res = B(n + 1) * ((2 ** (n + 1)) - 1) // (n + 1)
    return res


@lru_cache(maxsize=None)
def zeta1(n: int) -> Fraction:
    """
    计算黎曼ζ函数在负整数点的值。
    数学公式: ζ(-n) = Z(n) / (1 - 2^(n+1))
    """
    if n == 0:
        return Fraction(-1, 2)
    res = Z(n)
    res //= Fraction(1) - (2 ** (n + 1))
    return res


@lru_cache(maxsize=None)
def zeta2(n: int) -> Fraction:
    """
    计算黎曼ζ函数在偶数点的值。
    数学公式: ζ(2n) = (-1)^(n+1) * (2^(2n) * B(2n) * π^(2n)) / (2 * (2n)!)
    """
    res = B(n)
    p1 = Fraction((-1) ** (n // 2 + 1))
    p2 = Fraction(2 ** n, 2 * fact(n))
    res *= p1 * p2
    return res


@lru_cache(maxsize=None)
def zeta3(x: int, n: int, j: int) -> Fraction:
    """
    计算zeta3函数，涉及组合数和幂运算。
    数学公式: zeta3(x, n, j) = sum((-1)^k * C(n, k) * (x-k)^(n-j))
    """
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


@lru_cache(maxsize=None)
def powsum(n: int) -> PolyF:
    """
    计算幂和多项式S(n)，即1^k + 2^k + ... + n^k的生成函数。
    数学公式: S(n) = sum(k^i) for i in range(n+1)
    """
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


@lru_cache(maxsize=None)
def powmul(n: int) -> PolyF:
    """
    计算多项式的乘积展开式。
    数学公式: T(n) = product((x + i) for i in range(1, n+1))
    """
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


@lru_cache(maxsize=None)
def zeta1mulc(n: int) -> Fraction:
    """
    计算与黎曼ζ函数相关的系数。
    数学公式: T(n) = sum((-1)^j * C(n, j) * ζ(-j))
    """
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


@lru_cache(maxsize=None)
def inv_zeta1mulc(n: int) -> Complex:
    """
    计算与黎曼ζ函数相关的逆系数。
    数学公式: inv_T(n) = sum((-1)^j * C(n, j) * G(j))
    """
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


@lru_cache(maxsize=None)
def inv2_zeta1mulc(n: int):
    """
    计算与黎曼ζ函数相关的另一种逆系数。
    数学公式: inv2_T(n) = sum((-1)^j * C(n, j) * T(j))
    """
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


@lru_cache(maxsize=None)
def inv3_zeta1mulc(n: int):
    """
    计算与黎曼ζ函数相关的第三种逆系数。
    数学公式: inv3_T(n) = sum((-1)^j * C(n, j) * unlimited2(powmul(j)))
    """
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


@lru_cache(maxsize=None)
def G(n: int):
    """
    计算G(n)，与阶乘相关的复数函数。
    数学公式: G(n) = 1 / (2n + 1)!
    """
    return Complex(1) // fact(2 * n + 1)


@lru_cache(maxsize=None)
def F(n: int) -> Fraction:
    """
    计算F(n)，与n相关的分数函数。
    数学公式: F(n) = (-1)^n / (n + 1)
    """
    return Fraction((-1) ** n, n + 1)


@lru_cache(maxsize=None)
def unlimited(it: Poly) -> Complex:
    """
    计算多项式的极限值。
    数学公式: lim(S(n)) = sum(F(i) * it[i])
    """
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
    """
    计算带分数的多项式的极限值。
    数学公式: lim(S(n)) = unlimited(it.x) / unlimited(it.y)
    """
    return unlimited(it.x) // unlimited(it.y)


if __name__ == '__main__':
    # 打印前6个伯努利数
    for i in range(1, 7):
        print("第" + str(i) + "个伯努利数:", B(i))
    print()

    # 打印黎曼ζ函数在负整数点的值
    for i in range(7):
        print("黎曼函数自变量(" + str(-i) + "):", zeta1(i))
    print()

    # 打印黎曼ζ函数在偶数点的值
    for i in range(2, 10, 2):
        print("黎曼函数自变量(" + str(i) + "):", str(zeta2(i)) + " * (pi)^" + str(i))
    print()

    for i in range(7):
        print("S(" + str(i) + "):", powsum(i))
    print()

    for i in range(7):
        print("n = 无穷大 -> S(" + str(i) + "):", unlimited2(powsum(i)))
    print()

    for i in range(7):
        print("T(" + str(i) + "):", powmul(i))
    print()

    for i in range(7):
        print("n = 无穷大 -> T(" + str(i) + "):", unlimited2(powmul(i)))
    print()

    # 打印与黎曼ζ函数相关的系数T(n)
    print(
        "展开(x + 1)(x + 2) ... (x + n) -> [T(0) * x ^ n] + [T(1) * x ^ (n - 1)] + ... + [T(n) * x ^ 0] —> ")
    for i in range(1, 7):
        print("G(" + str(-i) + "):", zeta1mulc(i))
    print()

    for i in range(1, 7):
        print("G(" + str(2 * i) + "):", G(i))
    print()

    # 打印与黎曼ζ函数相关的逆系数
    for i in range(1, 7):
        print("反解G(" + str(i * 2) + "):", inv_zeta1mulc(i))
    print()

    # 打印与黎曼ζ函数相关的第二种逆系数
    for i in range(1, 7):
        print("反解G(" + str(-i) + "):", inv2_zeta1mulc(i))
    print()

    # 打印与黎曼ζ函数相关的第三种逆系数
    for i in range(1, 7):
        print("n = 无穷大 -> 反解T(" + str(i) + "):", inv3_zeta1mulc(i))
    print()

    # 打印多项式展开式
    P = Poly(1)
    for i in range(6):
        P *= Poly([i, 1])
    print(P)
    print()

    # 打印多项式展开式的系数T(n)在x=5时的值
    for i in range(1, 6):
        print("T(" + str(i) + "):", powmul(i).evaluate(5))
