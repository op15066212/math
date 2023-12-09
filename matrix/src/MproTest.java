public class MproTest {
    public static void main(String[] args) {
        //�ӵʹ������
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

        //���m1,m2
        System.out.println("���m1, m2");
        System.out.println(m1);
        System.out.println(m2);
        System.out.println();

        //������ʽ
        System.out.println("������ʽ");
        System.out.println(m1.determinant());
        System.out.println();
        //������Է���(ֻ�ǰѷ���Ϊ��������)
        System.out.println("������Է���(ֻ�ǰѷ���Ϊ��������)");
        System.out.println(m1.solve());

        //����
        System.out.println("����");
        System.out.println(m1.inverse());
        System.out.println();

        //�Ӽ��˳�
        System.out.println("��");
        System.out.println(m1.add(m2));
        System.out.println();
        System.out.println("��");
        System.out.println(m1.sub(m2));
        System.out.println();
        System.out.println("��");
        System.out.println(m1.multiply(m2));
        System.out.println();
        System.out.println("��");
        System.out.println(m1.divide(m2));
    }
}
