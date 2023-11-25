import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Poly {
    C[] coef; // ����ʽϵ��

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


    //�����λ����
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
     * ���ض���ʽ�Ĵ�����
     *
     * @return ����ʽ������
     */
    public int degree() {
        int i = coef.length - 1;
        while (i > 0 && coef[i].len() == 0) {
            i--;
        }
        return i;
    }

    /**
     * ���ض���ʽ��ָ���� x ���ĺ���ֵ��
     *
     * @param x �Ա�����ȡֵ��
     * @return ����ֵ��
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
     * ����������ʽ���г�������
     *
     * @param other ��һ������ʽ
     * @return �����õ����̺���������һ������Ϊ2�Ķ���ʽ���鷵�أ�
     * ��һ��Ԫ�����̣�����Ϊ�ն���ʽ�����ڶ���Ԫ��������������Ϊ�ն���ʽ��
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
     * ���ض���ʽ�ĵ�������
     *
     * @return ��������
     */
    public Poly differentiate() {
        C[] derivCoef = new C[coef.length - 1];
        for (int i = 0; i < derivCoef.length; i++) {
            derivCoef[i] = new C(i + 1).multiply(coef[i + 1]);
        }
        return new Poly(derivCoef);
    }

    /**
     * ���ض���ʽ�Ļ��ֺ�������ָ�������
     *
     * @param constant ���ֳ�����
     * @return ���ֺ�����
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
     * ������ʽȡ�����������µĶ���ʽ��
     *
     * @return ȡ������ʽ��
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
