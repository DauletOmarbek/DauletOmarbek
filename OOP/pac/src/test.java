import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Player player = new MyPlayer();

        Game game = null;

        try{
            game = new Game(new Map(input));
        }
        catch(InvalidMapException e){ // custom exception
            System.out.println(e.getMessage());
            System.exit(0);
        }

        game.addPlayer(player);


        String moves = input.next();
        char move;
        for(int i=0; i<moves.length(); i++){
                move = moves.charAt(i);
            switch (move) {
                case 'R' -> player.moveRight();
                case 'L' -> player.moveLeft();
                case 'U' -> player.moveUp();
                case 'D' -> player.moveDown();
            }
            }

        Position playerPosition = player.getPosition();
        System.out.println("Player final position");
        System.out.println("Row: " + playerPosition.getX());
        System.out.println("Col: " + playerPosition.getY());
        }
    }
