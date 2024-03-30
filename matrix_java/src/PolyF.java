public class PolyF {
    Poly x;
    Poly y;

    public PolyF() {
        this.x = new Poly();
        this.y = new Poly(1);
        change();
    }

    public PolyF(Poly x) {
        this.x = x;
        this.y = new Poly(1);
        change();
    }

    public PolyF(Poly x, Poly y) {
        this.x = x;
        this.y = y;
        change();
    }

    public PolyF(long... x) {
        this.x = new Poly(x);
        this.y = new Poly(1);
        change();
    }

    public PolyF(long[] x, long... y) {
        this.x = new Poly(x);
        this.y = new Poly(y);
        change();
    }

    public PolyF(F... x) {
        this.x = new Poly(x);
        this.y = new Poly(1);
        change();
    }

    public PolyF(F[] x, F... y) {
        this.x = new Poly(x);
        this.y = new Poly(y);
        change();
    }

    public PolyF(C... x) {
        this.x = new Poly(x);
        this.y = new Poly(1);
        change();
    }

    public PolyF(C[] x, C... y) {
        this.x = new Poly(x);
        this.y = new Poly(y);
        change();
    }

    public static Poly gcd(Poly a, Poly b) {
        Poly mod = a.remainder(b);
        if (mod.degree() == 0 && mod.coef[0].compare(new C()) == 0) {
            return b;
        } else {
            return gcd(b, mod);
        }
    }

    public void change() {
        Poly gcd = gcd(this.x, this.y);
        this.x = x.divide(gcd);
        this.y = y.divide(gcd);
    }

    public Poly getx() {
        return x;
    }

    public void setx(Poly x) {
        this.x = x;
    }

    public Poly gety() {
        return y;
    }

    public void sety(Poly y) {
        this.y = y;
    }

    public PolyF add(PolyF scd) {
        return new PolyF(this.x.multiply(scd.y).add(scd.x.multiply(this.y)), this.y.multiply(scd.y));
    }

    public PolyF sub(PolyF scd) {
        return new PolyF(this.x.multiply(scd.y).subtract(scd.x.multiply(this.y)), this.y.multiply(scd.y));
    }

    public PolyF multiply(PolyF scd) {
        return new PolyF(this.x.multiply(scd.x), this.y.multiply(scd.y));
    }

    public PolyF divide(PolyF scd) {
        return new PolyF(this.x.multiply(scd.y), this.y.multiply(scd.x));
    }

    public int compare(PolyF scd) {
        if (this.len() - scd.len() == 0) {
            return (int) (this.evaluate(10).len() - scd.evaluate(10).len());
        } else if (this.len() - scd.len() > 0) {
            return 1;
        } else {
            return -1;
        }
    }

    public double len() {
        return x.len() / y.len();
    }

    public C evaluate(long t) {
        return this.x.evaluate(t).divide(this.y.evaluate(t));
    }

    public String toString() {
        if (y.degree() != 0 || y.coef[0].compare(new C(1)) != 0) {
            return String.format("{%s / %s}", this.x, this.y);
        } else {
            return String.format("%s", this.x);
        }
    }
}

