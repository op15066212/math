public class F {
    long x;//分子
    long y;//分母

    public F() {
        this.x = 0;
        this.y = 1;
        change();
    }

    public F(long x) {
        this.x = x;
        this.y = 1;
        change();
    }

    public F(long x, long y) {
        this.x = x;
        if (y == 0) {
            throw new ArithmeticException("分母不能为零");
        } else {
            this.y = y;
        }
        change();
    }

    public void change() {
        long gcd = this.gcd(this.x, this.y);
        this.x /= gcd;
        this.y /= gcd;
        if (y < 0) {
            y *= -1;
            x *= -1;
        }
    }

    public long gcd(long a, long b) {
        long mod = a % b;
        if (mod == 0) {
            return b;
        } else {
            return gcd(b, mod);
        }
    }

    public long getx() {
        return x;
    }

    public void setx(long x) {
        this.x = x;
    }

    public long gety() {
        return y;
    }

    public void sety(long y) {
        this.y = y;
    }

    public F add(F scd) {
        return new F(this.x * scd.y + scd.x * this.y, this.y * scd.y);
    }

    public F sub(F scd) {
        return new F(this.x * scd.y - scd.x * this.y, this.y * scd.y);
    }

    public F multiply(F scd) {
        return new F(this.x * scd.x, this.y * scd.y);
    }

    public F divide(F scd) {
        return new F(this.x * scd.y, this.y * scd.x);
    }

    public F pow(long n) {
        F bas = this;
        F res = new F(1);
        while (n != 0) {
            if (n % 2 == 1) {
                res = res.multiply(bas);
            }
            bas = bas.multiply(bas);
            n /= 2;
        }
        return res;
    }

    public int compare(F scd) {
        if (this.len() - scd.len() == 0) {
            return 0;
        } else if (this.len() - scd.len() > 0) {
            return 1;
        } else {
            return -1;
        }
    }


    public double len() {
        return (double) this.x / (double) this.y;
    }

    public String toString() {
        if (y != 1) {
            return String.format("(%d/%d)", this.x, this.y);
        } else {
            return String.format("%d", this.x);
        }
    }
}

