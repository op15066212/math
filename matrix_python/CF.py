import random

from F import Fraction
from IF import IF

limit = int(1e6)


class CF:
    def __init__(self, x=0.0):
        self.nums = []
        self.x = x
        self.g = IF()
        self.p = Fraction()
        self.sign = True
        self.init()

    def init(self):
        if self.x < 0:
            self.x *= -1
            self.sign = False
        else:
            self.sign = True
        self.change()

    def change(self):
        copy = self.x
        for i in range(0, 30):
            tr = int(copy)
            if tr < 0 or tr > limit:
                return
            self.nums.append(tr)
            copy -= tr
            if copy == 0:
                break
            copy = 1 / copy

    def ToFraction1(self):
        return IF(self.ToFraction2())

    def ToFraction2(self):
        if len(self.nums) == 0:
            return
        res = Fraction(self.nums[-1])
        one = Fraction(1)
        zero = Fraction(0)
        end = len(self.nums) - 2
        for i in range(end, -1, -1):
            next = one // res
            next += Fraction(self.nums[i])
            if next < zero or next > Fraction(limit):
                break
            res = next
        if not self.sign:
            res *= Fraction(-1)
        return res

    def __str__(self):
        res = ""
        if self.sign:
            res += "正数，"
        else:
            res += "负数，"
        res += str(self.nums)
        return res


if __name__ == "__main__":
    # 创建一个随机数生成器对象
    # 生成一个在 1 到 9999 之间的随机整数
    x = random.randint(-9999, 9999)
    y = random.randint(-9999, 9999)
    num = x / y
    it = CF(num)

    print(Fraction(x, y))
    print(num)
    print(it)
    print(it.ToFraction2())
