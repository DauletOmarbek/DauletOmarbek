import javax.smartcardio.Card;
import java.io.File;
import java.util.Scanner;
import java.util.Stack;

public class Task2 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
    }

    long getSize(File directory) {
        Scanner scanner = new Scanner(file);
        long size = 0;
        File file = new File("C:\\Users\\Daulet\\Desktop\\" + directory);
        Scanner scanner = new Scanner(file);
        Stack<Card> deck = new Stack<>()
        while (scanner.hasNextLine()) {
            String inp = scanner.nextLine();
            deck.push(inp);
        }
        return size;
    }

}
