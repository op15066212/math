from copy import copy

from PolyF import PolyF


class Mpro:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            # 假设第一个参数是二维列表
            data = args[0]
            self.row = len(data)
            self.col = len(data[0])
            if self.row > 0 and self.col > 0 and not isinstance(data[0][0], PolyF):
                temp = [[PolyF() for _ in range(self.col)] for _ in range(self.row)]
                for i in range(self.row):
                    for j in range(self.col):
                        temp[i][j] = PolyF(data[i][j])
                data = temp
            self.data = data
        elif len(args) == 2 and all(isinstance(arg, int) for arg in args):
            # 假设有两个参数，且都是整数
            row, col = args
            self.row = row
            self.col = col
            self.data = [[PolyF(0) for _ in range(col)] for _ in range(row)]
        else:
            raise ValueError("Invalid arguments to M constructor")

    def __getitem__(self, key):
        if isinstance(key, tuple):
            # 如果key是元组，则直接返回对应的元素
            return self.data[key[0]][key[1]]
        else:
            # 否则返回一个可以再次被索引的行对象
            return self.data[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            # 如果key是元组，则设置对应元素的值
            self.data[key[0]][key[1]] = value
        else:
            # 如果不是元组，那么就是设置整行的值
            self.data[key] = value

    def __add__(self, B: any):
        if not isinstance(B, Mpro):
            B = Mpro(B)
        A = Mpro(self.data)
        if A.row != B.row or A.col != B.col:
            raise ValueError("row or col not unequal")
        n = A.row
        m = A.col
        C = Mpro(n, m)
        for i in range(n):
            for j in range(m):
                C[i][j] = A[i][j] + B[i][j]
        return C

    def __sub__(self, B: any):
        if not isinstance(B, Mpro):
            B = Mpro(B)
        A = Mpro(self.data)
        if A.row != B.row or A.col != B.col:
            raise ValueError("row or col not unequal")
        n = A.row
        m = A.col
        C = Mpro(n, m)
        for i in range(n):
            for j in range(m):
                C[i][j] = A[i][j] - B[i][j]
        return C

    def __mul__(self, B: any):
        if not isinstance(B, Mpro):
            B = Mpro(B)
        A = Mpro(self.data)
        if A.col != B.row:
            raise ValueError("can not multiply")
        n = A.row
        m = B.col
        l = A.col
        C = Mpro(n, m)
        for i in range(n):
            for j in range(m):
                sum = PolyF(0)
                for k in range(l):
                    sum += A[i][k] * B[k][j]
                C[i][j] = sum
        return C

    def __iadd__(self, other: any):
        if not isinstance(other, Mpro):
            other = Mpro(other)
        return self + other

    def __isub__(self, other: any):
        if not isinstance(other, Mpro):
            other = Mpro(other)
        return self - other

    def __imul__(self, other: any):
        if not isinstance(other, Mpro):
            other = Mpro(other)
        return self * other

    def __pow__(self, power, modulo=None):
        n = power
        bas = Mpro(self.data)
        res = self.eye(self.row)
        while n > 0:
            if n % 2 == 1:
                res *= bas
            bas *= bas
            n //= 2
        return res

    def __copy__(self):
        n = self.row
        m = self.col
        it = [[self.data[0][0] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                it[i][j] = self.data[i][j]
        return Mpro(it)

    def eye(self, n: int):
        E = Mpro(n, n)
        for i in range(n):
            E[i][i] = PolyF(1)
        return E

    def inverse(self):
        A = Mpro(self.data)
        if A.row != A.col:
            raise ValueError("can not inverse")
        n = A.row
        U = copy(A)
        E = self.eye(n)

        for r in range(n):
            mx = U[r][r]
            pivot = r
            for i in range(r + 1, n):
                if abs(U[i][r]) > abs(mx):
                    mx = U[i][r]
                    pivot = i
            if mx == PolyF(0):
                raise ValueError("can not inverse")
            if r != pivot:
                U[pivot], U[r] = U[r], U[pivot]
                E[pivot], E[r] = E[r], E[pivot]
            divisor = U[r][r]
            for c in range(n):
                U[r][c] //= divisor
                E[r][c] //= divisor
            for i in range(n):
                if i == r:
                    continue
                factor = U[i][r]
                for j in range(n):
                    U[i][j] -= factor * U[r][j]
                    E[i][j] -= factor * E[r][j]
        return E

    def solve(self):
        A = Mpro(self.data)
        n = A.row
        m = A.col

        U = copy(A)
        r = 0
        c = 0
        while r < n and c < m:
            mx = U[r][c]
            pivot = r
            for i in range(r + 1, n):
                if abs(U[i][c]) > abs(mx):
                    mx = U[i][c]
                    pivot = i
            if mx == PolyF(0):
                c += 1
                continue
            if r != pivot:
                U[pivot], U[r] = U[r], U[pivot]
            divisor = U[r][c]
            for i in range(m):
                U[r][i] //= divisor
            for i in range(n):
                if i == r:
                    continue
                factor = U[i][c]
                for j in range(m):
                    U[i][j] -= factor * U[r][j]
            r += 1
            c += 1
        return U

    def __str__(self):
        maxLen = 0
        for row in self.data:
            for col in row:
                maxLen = max(len(str(col)), maxLen)
        res = ""
        maxLen += 1
        for row in self.data:
            for col in row:
                res += "{:<{width}} ".format(str(col), width=maxLen)
            res += '\n'
        return res

    def __neg__(self):
        T = copy(self)
        for i in range(T.row):
            for j in range(T.col):
                T.data[i][j] = -T.data[i][j]
        return T


if __name__ == "__main__":
    A = Mpro([
        [99999, 9999],
        [99999, 9999]
    ])
    print(A)
    B = Mpro([
        [PolyF([1, 9]), PolyF([5, 2])],
        [PolyF([7, 3]), PolyF([4, 9])]
    ])
    print(B)
    print(A + B)
    print(A - B)
    print(A * B)
    print(B.inverse())
    print(B * B.inverse())
