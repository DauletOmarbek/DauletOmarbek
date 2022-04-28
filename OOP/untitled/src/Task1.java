import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Task1 {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        File file = new File("C:\\Users\\Daulet\\Desktop\\" + s);
        Scanner scanner = new Scanner(file);
        ArrayList<String> strings = new ArrayList<>();
        while (scanner.hasNextLine()){
            String inp = scanner.nextLine();
            strings.add(inp);
        }
        Collections.sort(strings);
        System.out.println(strings);
    }
}
