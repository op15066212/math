public class Main {

    public static void main(String[] args) {
        test1();
    }

    public static void test1() {
        M mat = new M(new long[][]{
                {1, 0, 0, 0, 0},
                {-1, 2, 0, 0, 0},
                {1, -3, 3, 0, 0},
                {-1, 4, -6, 4, 0},
                {1, -5, 10, -10, 5}});

        M mat2 = new M(new long[][]{
                {1, 1, -1, 2},
                {-1, -1, -4, 1},
                {2, 4, -6, 1},
                {1, 2, 4, 2},});

        M mat3 = new M(new long[][]{
                {2, -1, -1, 1, 2},
                {1, 1, -2, 1, 4},
                {4, -6, 2, -2, 4},
                {3, 6, -9, 7, 9},});


        System.out.println(mat);
        System.out.println("求逆");
        System.out.println();
        M inside = mat.inverse();
        System.out.println(inside);
        System.out.println();


        System.out.println(mat2);
        System.out.println("求解行列式");
        System.out.println();
        F det = mat2.determinant();
        System.out.println(det);
        System.out.println();


        System.out.println(mat3);
        System.out.println("求解线性方程组");
        System.out.println();
        M x = mat3.solve();
        System.out.println(x);


//        System.out.println(mat4);
//        System.out.println("求逆pro");
//        System.out.println();
//        M m = mat4.inversepro();
//        System.out.println(m);
    }
}
