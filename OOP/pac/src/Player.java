public interface Player {
    Position p=new Position(0,0);
    public void setMap(Map m);

    public void moveRight();
    public void moveLeft();
    public void moveUp();
    public void moveDown();
    public Position getPosition();
}
