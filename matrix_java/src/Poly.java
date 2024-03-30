import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Poly {
    C[] coef; // 多项式系数

    public Poly() {
        coef = new C[]{new C()};
    }

    public Poly(long... coe) {
        coef = new C[coe.length];
        for (int i = 0; i < coe.length; i++) {
            coef[i] = new C(coe[i]);
        }
        change();
    }

    public Poly(F... coe) {
        coef = new C[coe.length];
        for (int i = 0; i < coe.length; i++) {
            coef[i] = new C(coe[i]);
        }
        change();
    }

    public Poly(C... coe) {
        coef = coe;
        change();
    }


    //清理高位的零
    public void change() {
        int m = degree() + 1;
        int n = coef.length;
        C[] temp = new C[m];
        if (n > m) {
            System.arraycopy(coef, 0, temp, 0, m);
            coef = temp;
        }
    }

    /**
     * 返回多项式的次数。
     *
     * @return 多项式次数。
     */
    public int degree() {
        int i = coef.length - 1;
        while (i > 0 && coef[i].len() == 0) {
            i--;
        }
        return i;
    }

    /**
     * 返回多项式在指定点 x 处的函数值。
     *
     * @param x 自变量的取值。
     * @return 函数值。
     */
    public C evaluate(long x) {
        C y = new C(x);
        C res = new C();
        for (int i = coef.length - 1; i >= 0; i--) {
            res = res.multiply(y).add(coef[i]);

        }
        return res;
    }

    public C evaluate(F x) {
        C y = new C(x);
        C res = new C();
        for (int i = coef.length - 1; i >= 0; i--) {
            res = res.multiply(y).add(coef[i]);

        }
        return res;
    }

    public C[] getCoef() {
        return coef;
    }

    public void setCoef(C[] coe) {
        this.coef = coe;
        change();
    }

    public void setCoef(F[] coe) {
        coef = new C[coe.length];
        for (int i = 0; i < coe.length; i++) {
            coef[i] = new C(coe[i]);
        }
        change();
    }


    public Poly add(Poly other) {
        int n = Math.max(coef.length, other.coef.length);
        C[] newCoef = new C[n];
        for (int i = 0; i < n; i++) {
            C a = i < coef.length ? coef[i] : new C();
            C b = i < other.coef.length ? other.coef[i] : new C();
            newCoef[i] = a.add(b);
        }
        return new Poly(newCoef);
    }

    public Poly subtract(Poly other) {
        int n = Math.max(coef.length, other.coef.length);
        C[] newCoef = new C[n];
        for (int i = 0; i < n; i++) {
            C a = i < coef.length ? coef[i] : new C();
            C b = i < other.coef.length ? other.coef[i] : new C();
            newCoef[i] = a.subtract(b);
        }
        return new Poly(newCoef);
    }


    public Poly multiply(Poly other) {
        int n = coef.length + other.coef.length;
        C[] coe = new C[n];
        for (int i = 0; i < n; i++) {
            coe[i] = new C();
        }
        for (int i = 0; i < coef.length; i++) {
            for (int j = 0; j < other.coef.length; j++) {
                coe[i + j] = coe[i + j].add(coef[i].multiply(other.coef[j]));
            }
        }
        return new Poly(coe);
    }

    public Poly pow(long n) {
        Poly bas = this;
        Poly res = new Poly(1);
        while (n != 0) {
            if (n % 2 != 0) {
                res = res.multiply(bas);
            }
            bas = bas.multiply(bas);
            n /= 2;
        }
        return res;
    }

    /**
     * 对两个多项式进行除法运算
     *
     * @param other 另一个多项式
     * @return 相除后得到的商和余数，用一个长度为2的多项式数组返回，
     * 第一个元素是商（可能为空多项式），第二个元素是余数（可能为空多项式）
     */
    public Poly divide(Poly other) {
        int m = degree();
        int n = other.degree();
        if (m < n) {
            return new Poly();
        }
        C[] quotient = new C[m - n + 1];
        C[] remainder = Arrays.copyOf(coef, m + 1);
        for (int i = m - n; i >= 0; i--) {
            C q = remainder[i + n].divide(other.coef[n]);
            quotient[i] = q;
            for (int j = 0; j <= n; j++) {
                remainder[i + j] = remainder[i + j].subtract(q.multiply(other.coef[j]));
            }
        }
        return new Poly(quotient);
    }

    public Poly remainder(Poly other) {
        int m = degree();
        int n = other.degree();
        if (m < n) {
            return this;
        }
        C[] quotient = new C[m - n + 1];
        C[] remainder = Arrays.copyOf(coef, m + 1);
        for (int i = m - n; i >= 0; i--) {
            C q = remainder[i + n].divide(other.coef[n]);
            quotient[i] = q;
            for (int j = 0; j <= n; j++) {
                remainder[i + j] = remainder[i + j].subtract(q.multiply(other.coef[j]));
            }
        }
        return new Poly(remainder);
    }

    /**
     * 返回多项式的导函数。
     *
     * @return 导函数。
     */
    public Poly differentiate() {
        C[] derivCoef = new C[coef.length - 1];
        for (int i = 0; i < derivCoef.length; i++) {
            derivCoef[i] = new C(i + 1).multiply(coef[i + 1]);
        }
        return new Poly(derivCoef);
    }

    /**
     * 返回多项式的积分函数，并指定常数项。
     *
     * @param constant 积分常数。
     * @return 积分函数。
     */
    public Poly integrate(F constant) {
        C[] integrCoef = new C[coef.length + 1];
        integrCoef[0] = new C(constant);
        for (int i = 0; i < coef.length; i++) {
            integrCoef[i + 1] = coef[i].divide(new C(i + 1));
        }
        return new Poly(integrCoef);
    }

    public Poly integrate(long constant) {
        C[] integrCoef = new C[coef.length + 1];
        integrCoef[0] = new C(constant);
        for (int i = 0; i < coef.length; i++) {
            integrCoef[i + 1] = coef[i].divide(new C(i + 1));
        }
        return new Poly(integrCoef);
    }

    /**
     * 将多项式取反，并返回新的多项式。
     *
     * @return 取反多项式。
     */
    public Poly negate() {
        C[] newCoef = new C[coef.length];
        for (int i = 0; i < coef.length; i++) {
            newCoef[i] = coef[i].multiply(new C(-1));
        }
        return new Poly(newCoef);
    }


    public int compare(Poly scd) {
        if (this.len() - scd.len() == 0) {
            return (int) (evaluate(10).len() - scd.evaluate(10).len());
        } else if (this.len() - scd.len() > 0) {
            return 1;
        } else {
            return -1;
        }
    }

    public double len() {
        return degree();
    }


    @Override
    public String toString() {
        List<pair> list = new ArrayList<>();
        for (int i = 0; i < coef.length; i++) {
            if (coef.length > 1 && coef[i].len() == 0) {
                continue;
            }
            if (i == 0) {
                list.add(new pair(coef[i], ""));
            } else if (i == 1) {
                list.add(new pair(coef[i], "x"));
            } else {
                list.add(new pair(coef[i], "x^" + i));
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = list.size() - 1; i >= 0; i--) {
            if (i == 0) {
                sb.append(list.get(i));
            } else {
                sb.append(list.get(i)).append(" + ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    static class pair {
        C c;
        String x;

        public pair(C c, String x) {
            this.c = c;
            this.x = x;
        }

        @Override
        public String toString() {
            if (!x.isEmpty()) {
                if (c.len() == 1) {
                    return x;
                }
                if (c.len() == -1) {
                    return "-" + x;
                }
            }
            return c + x;
        }
    }
}
