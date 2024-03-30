public class C {

    F real; // ʵ��
    F imag; // �鲿

    public C() {
        this.real = new F();
        this.imag = new F();
    }

    public C(F real) {
        this.real = real;
        this.imag = new F();

    }

    public C(F real, F imag) {
        this.real = real;
        this.imag = imag;
    }


    public C(long real) {
        this.real = new F(real);
        this.imag = new F();

    }

    public C(long real, long imag) {
        this.real = new F(real);
        this.imag = new F(imag);
    }


    // ��ȡʵ��
    public F getReal() {
        return real;
    }

    // ����ʵ��
    public void setReal(F real) {
        this.real = real;
    }

    // ��ȡ�鲿
    public F getImag() {
        return imag;
    }

    // �����鲿
    public void setImag(F imag) {
        this.imag = imag;
    }

    public double len() {
        double r = real.multiply(real).add(imag.multiply(imag)).len();
        return Math.sqrt(r);
    }


    // ���㹲���
    public C conjugate() {
        return new C(this.real, this.imag.multiply(new F(-1)));
    }

    // �����ӷ�
    public C add(C value) {
        return new C(this.real.add(value.real), this.imag.add(value.imag));
    }

    // ��������
    public C subtract(C value) {
        return new C(this.real.sub(value.real), this.imag.sub(value.imag));
    }

    // �����˷�
    public C multiply(C value) {
        F realPart = this.real.multiply(value.real).sub(this.imag.multiply(value.imag));
        F imagPart = this.real.multiply(value.imag).add(this.imag.multiply(value.real));
        return new C(realPart, imagPart);
    }

    public C inverse() {
        F denominator = real.multiply(real).add(imag.multiply(imag));
        if (denominator.len() == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return new C(real.divide(denominator), imag.divide(denominator).multiply(new F(-1)));
    }

    // ��������
    public C divide(C value) {
        return this.multiply(value.inverse());
    }


    public int compare(C scd) {
        if (this.len() - scd.len() == 0) {
            return 0;
        } else if (this.len() - scd.len() > 0) {
            return 1;
        } else {
            return -1;
        }
    }

    @Override
    public String toString() {
        if (imag.len() > 0) {
            if (imag.len() == 1) {
                return "(" + real + " + " + "i" + ")";
            }
            return "(" + real + " + " + imag + "i" + ")";
        } else if (imag.len() < 0) {
            if (imag.len() == -1) {
                return "(" + real + " - " + "i" + ")";
            }
            return "(" + real + " - " + (imag.multiply(new F(-1))) + "i" + ")";
        } else {
            return String.valueOf(real);
        }
    }
}
