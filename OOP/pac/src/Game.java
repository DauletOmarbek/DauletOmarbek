import java.util.ArrayList;

public class Game {
    private Map map;
    ArrayList<Player> arr=new ArrayList<>();
    public Game(Map m){
        this.map=m;
    }
    public void setMap(Map m){
        this.map=m;
    }
    public void addPlayer(Player p){
        p.setMap(map);
        arr.add(p);
    }
}
