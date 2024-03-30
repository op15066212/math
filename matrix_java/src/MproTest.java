public class MproTest {
    public static void main(String[] args) {
        //从低次项到高项
        Mpro m1 = new Mpro(new Poly[][]{
                {new Poly(1), new Poly(0, 1), new Poly(1)},
                {new Poly(0, 1), new Poly(1), new Poly(1)},
                {new Poly(1), new Poly(-1), new Poly(3)},
        });


        Mpro m2 = new Mpro(new Poly[][]{
                {new Poly(1), new Poly(0, 1), new Poly(1)},
                {new Poly(0, 1), new Poly(1), new Poly(1)},
                {new Poly(1), new Poly(-1), new Poly(3)},
        });

        //输出m1,m2
        System.out.println("输出m1, m2");
        System.out.println(m1);
        System.out.println(m2);
        System.out.println();

        //解行列式
        System.out.println("解行列式");
        System.out.println(m1.determinant());
        System.out.println();
        //求解线性方程(只是把方阵化为行最简矩阵)
        System.out.println("求解线性方程(只是把方阵化为行最简矩阵)");
        System.out.println(m1.solve());

        //求逆
        System.out.println("求逆");
        System.out.println(m1.inverse());
        System.out.println();

        //加减乘除
        System.out.println("加");
        System.out.println(m1.add(m2));
        System.out.println();
        System.out.println("减");
        System.out.println(m1.sub(m2));
        System.out.println();
        System.out.println("乘");
        System.out.println(m1.multiply(m2));
        System.out.println();
        System.out.println("除");
        System.out.println(m1.divide(m2));
    }
}
