public class test {
    public static void main(String[] args){
        int [][] A = new int[10][10];
        for (int i=0; i < 10; i++){
            for (int j=0; j < 10; j++){
                A[i][j] = i + j;
            }
        }

        for (int i=0; i < 10; i++){
            for (int j=0; j < 10; j++){
                System.out.print(A[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }

    }
}
