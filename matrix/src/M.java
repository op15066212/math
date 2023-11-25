public class M {
    int rows; // ��������
    int cols; // ��������
    F[][] data; // �洢�������ݵĶ�ά����

    public M(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        this.data = new F[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                set(i, j, 0);
            }
        }
    }

    public M(long[][] data) {
        this.rows = data.length;
        this.cols = data[0].length;
        this.data = new F[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                set(i, j, data[i][j]);
            }
        }
    }

    public M(F[][] data) {
        this.rows = data.length;
        this.cols = data[0].length;
        this.data = data;
    }

    public F[][] getData() {
        return data;
    }

    // ��ȡ������ĳ��λ�õ�ֵ
    public F get(int i, int j) {
        return data[i][j];
    }


    // ���þ�����ĳ��λ�õ�ֵ
    public void set(int i, int j, F val) {
        data[i][j] = val;
    }

    // ���þ�����ĳ��λ�õ�ֵ
    public void set(int i, int j, long val) {
        set(i, j, new F(val));
    }

    public M add(M B) {
        M A = this;
        if (A.rows != B.rows || A.cols != B.cols) {
            throw new IllegalArgumentException("The matrixs can not add");
        }
        int n = A.rows;
        int m = A.cols;
        M C = new M(n, m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                C.set(i, j, A.get(i, j).add(B.get(i, j)));
            }
        }
        return C;
    }

    public M sub(M B) {
        M A = this;
        if (A.rows != B.rows || A.cols != B.cols) {
            throw new IllegalArgumentException("The matrixs can not sub");
        }
        int n = A.rows;
        int m = A.cols;
        M C = new M(n, m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                C.set(i, j, A.get(i, j).sub(B.get(i, j)));
            }
        }
        return C;
    }

    public M multiply(M B) {
        M A = this;
        if (A.cols != B.rows) {
            throw new IllegalArgumentException("The matrixs can not multiply");
        }
        int n = A.rows;
        int m = B.cols;
        int p = A.cols;
        M C = new M(n, m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                F sum = new F(0);
                for (int k = 0; k < p; k++) {
                    sum = sum.add(A.get(i, k).multiply(B.get(k, j)));
                }
                C.set(i, j, sum);
            }
        }
        return C;
    }

    public M pow(long n) {
        M res = new M(rows, cols);
        res.eye();
        M it = this;
        if (n < 0) {
            it = it.inverse();
            n = n * -1;
        }
        while (n != 0) {
            if (n % 2 == 1) {
                res = res.multiply(it);
            }
            it = it.multiply(it);
            n /= 2;
        }
        return res;
    }

    public M divie(M B) {
        M A = this;
        M invB = B.inverse();
        if (A.cols != invB.rows) {
            throw new IllegalArgumentException("The matrixs can not divide");
        }
        return this.multiply(invB);
    }

    public M inverse() {
        M A = this;
        // �жϾ����Ƿ�Ϊ����
        if (A.rows != A.cols) {
            throw new IllegalArgumentException("The matrix is not square");
        }
        int n = A.rows;
        M E = new M(n, n);
        // ��ʼ��Ϊ��λ����
        E.eye();
        // ��ʼ��ΪA��һ������
        M U = this.copy();
        // ��˹-Լ����Ԫ
        for (int k = 0; k < n; k++) {
            F max = U.abs(k, k);
            int pivot = k;
            //�Ҿ���ֵ������
            for (int i = k + 1; i < n; i++) {
                if (U.abs(i, k).compare(max) > 0) {
                    max = U.abs(i, k);
                    pivot = i;
                }
            }
            //�������ֵ���Ϊ0�����޽�
            if (max.len() == 0) {
                System.out.println("ԭ�����޷���һ������");
                System.out.println(U);
                throw new RuntimeException("Matrix is not invertible");
            }
            // ������
            if (k != pivot) {
                U.swapRow(pivot, k);
                E.swapRow(pivot, k);
            }
            // ����Ԫ��һ
            F divisor = U.get(k, k);
            for (int j = 0; j < n; j++) {
                U.set(k, j, U.get(k, j).divide(divisor));
                E.set(k, j, E.get(k, j).divide(divisor));
            }
            // ��Ԫ
            for (int i = 0; i < n; i++) {
                if (i != k) {
                    F factor = U.get(i, k);
                    for (int j = 0; j < n; j++) {
                        U.set(i, j, U.get(i, j).sub(factor.multiply(U.get(k, j))));
                        E.set(i, j, E.get(i, j).sub(factor.multiply(E.get(k, j))));
                    }
                }
            }
        }
        return E;
    }


    public F determinant() {
        M A = this;
        // �жϾ����Ƿ�Ϊ����
        if (A.rows != A.cols) {
            throw new IllegalArgumentException("The matrix is not square");
        }
        int n = A.rows;
        // ��ʼ��ΪA��һ������
        M U = this.copy();
        // ��˹-Լ����Ԫ
        F det = new F(1);
        for (int k = 0; k < n; k++) {
            F max = U.abs(k, k);
            int pivot = k;
            //�Ҿ���ֵ������
            for (int i = k + 1; i < n; i++) {
                if (U.abs(i, k).compare(max) > 0) {
                    max = U.abs(i, k);
                    pivot = i;
                }
            }
            //�������ֵ���Ϊ0��������ʽΪ0
            if (max.len() == 0) {
                return max;
            }
            // ������
            if (k != pivot) {
                U.swapRow(pivot, k);
                det = det.multiply(new F(-1));
            }
            F divisor = U.get(k, k);
            det = det.multiply(divisor);
            // ����Ԫ��һ
            for (int j = 0; j < n; j++) {
                U.set(k, j, U.get(k, j).divide(divisor));
            }
            // ��Ԫ
            for (int i = k + 1; i < n; i++) {
                F factor = U.get(i, k);
                for (int j = 0; j < n; j++) {
                    U.set(i, j, U.get(i, j).sub(factor.multiply(U.get(k, j))));
                }
            }
        }
        return det;
    }

    public M solve() {
        M A = this;
        int n = A.rows;
        int m = A.cols;
        // ����һ�ݡ�
        M U = A.copy();
        // ��˹-Լ����Ԫ
        for (int k = 0, T = 0; k < n && T < m; k++, T++) {
            F max = U.abs(k, T);
            int pivot = k;
            // �Ҿ���ֵ������
            for (int i = k + 1; i < n; i++) {
                if (U.abs(i, T).compare(max) > 0) {
                    max = U.abs(i, T);
                    pivot = i;
                }
            }
            // �������ֵ���Ϊ0�����޽�
            if (max.len() == 0) {
                k--;
                continue;
            }
            // ������
            if (k != pivot) {
                U.swapRow(pivot, k);
            }
            // ����Ԫ��һ
            F divisor = U.get(k, T);
            for (int j = 0; j < m; j++) {
                U.set(k, j, U.get(k, j).divide(divisor));
            }
            // ��Ԫ
            for (int i = 0; i < n; i++) {
                if (i != k) {
                    F factor = U.get(i, T);
                    for (int j = 0; j < m; j++) {
                        U.set(i, j, U.get(i, j).sub(factor.multiply(U.get(k, j))));
                    }
                }
            }
        }
        return U;
    }

    public M inversepro() {
        M A = this;
        int n = A.rows;
        int m = A.cols;
        // ��ʼ��ΪA��һ������
        M U = this.copy();
        //���ⵥλ����
        M E = new M(n, m);
        E.eye();
        // ��˹-Լ����Ԫ
        for (int k = 0, T = 0; k < n && T < m; k++, T++) {
            F max = U.abs(k, T);
            int pivot = k;
            //�Ҿ���ֵ������
            for (int i = k + 1; i < n; i++) {
                if (U.abs(i, T).compare(max) > 0) {
                    max = U.abs(i, T);
                    pivot = i;
                }
            }
            //�������ֵ���Ϊ0�����޽�
            if (max.len() == 0) {
                k--;
                continue;
            }
            // ������
            if (k != pivot) {
                U.swapRow(pivot, k);
                E.swapRow(pivot, k);
            }
            // ����Ԫ��һ
            F divisor = U.get(k, T);
            for (int j = 0; j < m; j++) {
                U.set(k, j, U.get(k, j).divide(divisor));
                E.set(k, j, E.get(k, j).divide(divisor));
            }
            // ��Ԫ
            for (int i = 0; i < n; i++) {
                if (i != k) {
                    F factor = U.get(i, T);
                    for (int j = 0; j < m; j++) {
                        U.set(i, j, U.get(i, j).sub(factor.multiply(U.get(k, j))));
                        E.set(i, j, E.get(i, j).sub(factor.multiply(E.get(k, j))));
                    }
                }
            }
        }
        return E;
    }

    public M transpose() {
        M A = this;
        int n = A.rows;
        int m = A.cols;
        M B = new M(m, n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                B.set(i, j, A.get(j, i));
            }
        }
        return B;
    }

    public void swapRow(int a, int b) {
        int n = cols;
        for (int j = 0; j < n; j++) {
            F temp = this.get(a, j);
            this.set(a, j, this.get(b, j));
            this.set(b, j, temp);
        }
    }

    public void swapCol(int a, int b) {
        int n = rows;
        for (int j = 0; j < n; j++) {
            F temp = this.get(j, a);
            this.set(j, a, this.get(j, b));
            this.set(j, b, temp);
        }
    }

    public void eye() {
        M e = this;
        int n = e.rows;
        int m = e.cols;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                e.set(i, j, 0);
            }
            e.set(i, i, 1);
        }
    }

    public M copy() {
        M e = new M(rows, cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                e.set(i, j, this.get(i, j));
            }
        }
        return e;
    }

    public F abs(int i, int j) {
        F f = this.get(i, j);
        if (f.compare(new F()) < 0) {
            f = f.multiply(new F(-1));
        }
        return f;
    }


    public String toString() {
        return print();
    }

    // ��ӡ����
    public String print() {
        int maxLen = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols - 1; j++) {
                maxLen = Math.max(maxLen, String.valueOf(data[i][j]).length());
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < rows; i++) {
            StringBuilder line = new StringBuilder();
            for (int j = 0; j < cols; j++) {
                int key = maxLen + 1;
                String str = String.format("%-" + key + "s", data[i][j]);
                line.append(str).append(" ");
            }
            line.append("\n");
            sb.append(line);
        }
        return sb.toString();
    }
}
