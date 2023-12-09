public class PolyAndPolyFTest {
    public static void main(String[] args) {
        test2();
        System.out.println();
    }

    public static void test1() {
        C c1 = new C(1, 2);
        C c2 = new C(1, 2);
        System.out.println(c1.add(c2));
        System.out.println(c1.subtract(c2));
        System.out.println(c1.multiply(c2));
        System.out.println(c1.divide(c2));
    }

    public static void test2() {
        // 构造多项式 f(x) =  6 + 11x + 6x^2 + x^3
        Poly f = new Poly(6, 11, 6, 1);
        // 构造多项式 p(x) = 3 + x
        Poly p = new Poly(3, 1);


        System.out.println("f(x) = " + f);
        System.out.println("p(x) = " + p);

        System.out.println();
        System.out.println("f(0) = " + f.evaluate(0));

        System.out.println("f'(x) = " + f.differentiate());
        System.out.println("∫f'(x) dx = " + f.differentiate().integrate(6));
        System.out.println();

        System.out.println("f(x) + p(x) = " + f.add(p));
        System.out.println("f(x) - p(x) = " + f.subtract(p));
        System.out.println("f(x) * p(x) = " + f.multiply(p));
        System.out.println("f(x) / p(x) = " + f.divide(p));
        System.out.println("f(x) % p(x) = " + f.remainder(p));
        System.out.println();
    }

    public static void test3() {
        Poly x1 = new Poly(1, 1);
        Poly x2 = new Poly(2, 1);
        Poly x3 = new Poly(3, 1);
        Poly y1 = new Poly(1, 1);
        Poly y2 = new Poly(4, 1);

        Poly p = x1.multiply(x2).multiply(x3);
        Poly q = y1.multiply(y2);
        Poly gcd = PolyF.gcd(p, q);

        System.out.println(p);
        System.out.println(q);
        System.out.println(gcd);

        System.out.println();
        PolyF f = new PolyF(p, q);
        System.out.println(f);
    }
}

