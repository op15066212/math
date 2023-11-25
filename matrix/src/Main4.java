import java.math.BigInteger;

public class Main4 {

    static long[][] C = new long[9999][9999];
    static long[][] A = new long[9999][9999];
    static long[] H = new long[9999];
    static F[] B = new F[999];
    static F[] fai = new F[999];
    static F[] zeta1 = new F[999];
    static BigInteger[][] C2 = new BigInteger[9999][9999];
    static PolyF[] powsum = new PolyF[999];
    static PolyF[] powmulc = new PolyF[999];
    static F[] basaier = new F[999];

    public static long C(int n, int m) {
        if (C[n][m] != 0) {
            return C[n][m];
        }
        if (n == 0 || m == 0 || n == 1 || m == n) {
            return 1;
        }
        if (m == 1 || m == n - 1) {
            return n;
        }
        if (m > n - m) {
            return C(n, n - m);
        }
        int k = m / 2;
        long v1 = C(n, k);
        long v2 = C(m, k);
        long v3 = C(n - k, m - k);
        C[n][m] = v1 * v3 / v2;
        return C[n][m];
    }

    public static long fact(int n) {
        return A(n, n);
    }

    public static long A(int n, int m) {
        if (A[n][m] != 0) {
            return A[n][m];
        }
        if (n == 0 || m == 0 || n == 1) {
            return 1;
        }
        if (m == 1) {
            return n;
        }
        int k = m / 2;
        long v1 = A(n, k);
        long v2 = A(n - k, m - k);
        A[n][m] = v1 * v2;
        return A[n][m];
    }

    public static long H(int n) {
        if (H[n] != 0) {
            return H[n];
        }
        long v1 = C(2 * n, n);
        long v2 = n + 1;
        H[n] = v1 / v2;
        return H[n];
    }

    public static F B(int n) {
        if (B[n] != null) {
            return B[n];
        }
        F res = new F();
        for (int j = 1; j <= n - 1; j++) {
            for (int i = 0; i <= n - 1 - j; i++) {
                F v1 = new F(C(n, i));
                F v2 = new F((long) pow(j, n - 1));
                F v3 = new F((long) pow(-1, j + 1));
                F val = v1.multiply(v2).multiply(v3);
                res = res.add(val);
            }
        }
        F p1 = new F((long) pow(2, n));
        F p2 = new F((long) pow(2, n) - 1);
        res = res.divide(p1).divide(p2).multiply(new F(n));
        B[n] = res;
        return B[n];
    }

    public static F fai(int n) {
        if (n == 0) {
            return new F(1, 2);
        }
        if (fai[n] != null) {
            return fai[n];
        }
        F res = new F();
        for (int j = 1; j <= n; j++) {
            for (int i = 0; i <= n - j; i++) {
                F v1 = new F(C(n + 1, i));
                F v2 = new F((long) pow(j, n));
                F v3 = new F((long) pow(-1, j + 1));
                F val = v1.multiply(v2).multiply(v3);
                res = res.add(val);
            }
        }
        F p1 = new F((long) pow(2, n + 1));
        res = res.divide(p1);
        fai[n] = res;
        return fai[n];
    }

    public static F zeta1(int n) {
        if (zeta1[n] != null) {
            return zeta1[n];
        }
        F res = fai(n);
        F p1 = new F(1);
        F p2 = new F((long) pow(2, n + 1));
        res = res.divide(p1.sub(p2));
        zeta1[n] = res;
        return zeta1[n];
    }

    public static F zeta2(int n) {
        F res = B(n);
        F p1 = new F((long) pow(-1, (double) n / 2 + 1));
        F p2 = new F((long) pow(2, n), 2 * fact(n));//2pi
        res = res.multiply(p1).multiply(p2);
        return res;
    }

    public static BigInteger zeta3(int x, int n, int j) {
        if (j < 1 || j > n) {
            System.out.println("1 <= j <= n");
            return null;
        }
        BigInteger res = new BigInteger("0");
        for (int k = 0; k <= n; k++) {
//            D(n, k) * pow(x - k, n) * pow(-1, k);
            BigInteger v1 = C2(n, k);
            BigInteger v2 = pow2(x - k, n - j);
            BigInteger v3 = pow2(-1, k);
            res = res.add(v1.multiply(v2).multiply(v3));
        }
        return res;
    }

    public static BigInteger C2(int n, int m) {
        if (C2[n][m] != null) {
            return C2[n][m];
        }
        if (n == 0 || m == 0 || n == 1 || m == n) {
            return BigInteger.valueOf(1);
        }
        if (m == 1 || m == n - 1) {
            return BigInteger.valueOf(n);
        }
        if (m > n - m) {
            return C2(n, n - m);
        }
        int k = m / 2;
        BigInteger v1 = C2(n, k);
        BigInteger v2 = C2(m, k);
        BigInteger v3 = C2(n - k, m - k);
        C2[n][m] = v1.multiply(v3).divide(v2);
        return C2[n][m];
    }

    public static BigInteger pow2(int b, int n) {
        BigInteger res = new BigInteger("1");
        BigInteger a = BigInteger.valueOf(b);
        while (n != 0) {
            if (n % 2 == 1) {
                res = res.multiply(a);
            }
            a = a.multiply(a);
            n /= 2;
        }
        return res;
    }

    public static double pow(double x, double y) {
        return Math.pow(x, y);
    }

    public static PolyF powsum(int n) {
        if (powsum[n] != null) {
            return powsum[n];
        }
        long[][] m = new long[n + 1][n + 1];
        PolyF[][] p = new PolyF[n + 1][1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= i; j++) {
                m[i][j] = C(i + 1, j);
                if ((i - j) % 2 == 1) {
                    m[i][j] *= -1;
                }
            }
        }
        for (int i = 0; i <= n; i++) {
            long[] q = new long[i + 2];
            q[i + 1] = 1;
            p[i][0] = new PolyF(q);
        }
        Mpro a = new Mpro(m);
        Mpro b = new Mpro(p);
        Mpro t = a.inverse().multiply(b);
        for (int i = 0; i <= n; i++) {
            powsum[i] = t.get(i, 0);
        }
        return powsum[n];
    }

    public static PolyF powmulc(int n) {
        if (n == 0) {
            return new PolyF(1);
        }
        if (powmulc[n] != null) {
            return powmulc[n];
        }
        PolyF[][] a = new PolyF[n][n];
        PolyF[][] b = new PolyF[n][1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = new PolyF();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (i - j != 0) {
                    a[i][j] = powsum(i - j);
                } else {
                    a[i][j] = new PolyF(i + 1);
                }
                if (j % 2 == 1) {
                    a[i][j] = a[i][j].multiply(new PolyF(-1));
                }
            }
        }
        for (int i = 0; i < n; i++) {
            b[i][0] = powsum(i + 1);
        }
        Mpro m = new Mpro(a);
        Mpro p = new Mpro(b);
        Mpro t = m.inverse().multiply(p);
        for (int i = 0; i < n; i++) {
            powmulc[i + 1] = t.get(i, 0);
        }
        return powmulc[n];
    }

    public static F zeta1mulc(int n) {
        F[][] a = new F[n][n];
        F[][] b = new F[n][1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = new F();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (i - j != 0) {
                    a[i][j] = zeta1(i - j);
                } else {
                    a[i][j] = new F(i + 1);
                }
                if (j % 2 == 1) {
                    a[i][j] = a[i][j].multiply(new F(-1));
                }
            }
        }
        for (int i = 0; i < n; i++) {
            b[i][0] = zeta1(i + 1);
        }
        M m = new M(a);
        M p = new M(b);
        M t = m.inverse().multiply(p);
        return t.get(n - 1, 0);
    }

    public static F zeta2mulc(int n) {
        F[][] a = new F[n][n];
        F[][] b = new F[n][1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = new F();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (i - j != 0) {
                    a[i][j] = zeta2(i - j);
                } else {
                    a[i][j] = new F(i + 1);
                }
                if (j % 2 == 1) {
                    a[i][j] = a[i][j].multiply(new F(-1));
                }
            }
        }
        for (int i = 0; i < n; i++) {
            b[i][0] = zeta2(i + 1);
        }
        M m = new M(a);
        M p = new M(b);
        M t = m.inverse().multiply(p);
        return t.get(n - 1, 0);
    }

    //偶然
    public static void ouran() {
        for (int i = 2; i < 11; i++) {
            System.out.println(powmulc(i).getx().coef[1]);
        }
        System.out.println("--------------------");
        for (int i = 1; i < 10; i++) {
            System.out.println(zeta1(i));
        }
    }

    //矩阵的方式求黎曼函数正整数的值
    public static F basaier(int n) {
        if (n == 1) {
            return basaierT(1);
        }
        if (basaier[n] != null) {
            return basaier[n];
        }
        F[][] a = new F[n][n];
        F[][] b = new F[n][1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = new F();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (i - j != 0) {
                    a[i][j] = basaier(i - j);
                } else {
                    a[i][j] = new F(i + 1);
                }
                if (j % 2 == 1) {
                    a[i][j] = a[i][j].multiply(new F(-1));
                }
            }
        }
        for (int i = 0; i < n; i++) {
            b[i][0] = basaierT(i + 1);
        }
        M m = new M(a);
        M p = new M(b);
        System.out.println(m);
        System.out.println(p);
        M t = m.multiply(p);
        F res = t.get(n - 1, 0);
        basaier[n] = res;
        return basaier[n];
    }

    public static F basaierT(int n) {
        int i = n * 2 + 1;
        return new F(1, fact(i));
    }

    public static void main(String[] args) {
        for (int i = 2; i < 11; i++) {
            System.out.println("第" + i + "个伯努利数：" + B(i));
        }
        System.out.println();
        for (int i = 0; i < 11; i++) {
            System.out.println("黎曼函数自变量(" + -i + ")：" + zeta1(i));
        }
        System.out.println();
        for (int i = 2; i < 11; i += 2) {
            System.out.println("黎曼函数自变量(" + i + ")：" + zeta2(i) + " * (pi)^" + i);
        }
        System.out.println();
        for (int i = 0; i < 11; i++) {
            System.out.println("S(" + i + "):" + powsum(i));
        }
        System.out.println();
        for (int i = 0; i < 11; i++) {
            System.out.println("系数T(" + i + "):" + powmulc(i));
        }
        System.out.println();
        for (int i = 1; i < 11; i++) {
            System.out.println("黎曼函数系数T(" + -i + "):" + zeta1mulc(i));
        }
        System.out.println();
        for (int i = 1; i < 11; i++) {
            System.out.println("黎曼函数系数T(" + i + "):" + zeta2mulc(i));
        }
        System.out.println();
//        for (int i = 800; i < 805; i++) {
//            for (int j = 800; j < 805; j++) {
//                System.out.print(zeta3(i, j, 800) + " ");
//            }
//            System.out.println();
//        }
    }
}
