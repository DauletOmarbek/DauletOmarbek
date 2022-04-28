import java.util.Scanner;

public class Map {
    private int StartX;
    private int StartY;
    private char[][] map = {
        {'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'},
        {'W','P','B','B','B','B','B','B','B','W','W','B','B','B','B','B','B','B','B','W'},
        {'W','B','W','W','W','W','W','W','B','W','W','B','W','W','W','W','W','W','B','W'},
        {'W','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','W'},
        {'W','E','W','B','W','W','W','W','B','W','W','W','W','B','W','W','W','W','B','W'},
        {'W','B','W','B','W','B','B','W','B','W','B','B','W','B','W','B','B','W','B','W'},
        {'W','B','W','B','W','W','W','W','B','W','W','W','W','B','W','B','B','W','B','W'},
        {'W','B','W','B','B','B','B','W','B','W','B','B','W','B','W','B','B','W','B','W'},
        {'W','B','W','B','B','B','B','W','B','W','W','W','W','B','W','W','W','W','B','W'},
        {'W','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','B','W'},
        {'W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'},
    };

    int getStartX(){
        return StartX;
    }
    int getStartY(){
        return StartY;
    }

    char getValueAt(int i,int j){
        return map[i][j];
    }

    void setValueAt(int i, int j){
        this.map[i][j] = 'E';
    }
    public void print(){
        for (int i=0;i<11;i++){
            for (int j=0;j<19;j++){
                System.out.print(map[i][j]+" ");
            }
            System.out.println();
        }

    }
}
