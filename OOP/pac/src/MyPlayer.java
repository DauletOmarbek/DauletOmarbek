public class MyPlayer implements Player{
    private Map map;
    public void setMap(Map m){
        map=m;
        p.setX(m.getStartX());
        p.setY(m.getStartY());
    }
    public void moveRight(){
        if (p.getY()!=19 && map.getValueAt(p.getX(), p.getY()+1)!='W'){
            p.setY(p.getY()+1);
            if (map.getValueAt(p.getX(), p.getY()+1) == 'B'){
                map.setValueAt(p.getX(), p.getY()+1);
            }
        }
    }
    public void moveLeft(){
        if (p.getY()!=0 && map.getValueAt(p.getX(), p.getY()-1)!='W'){
            p.setY(p.getY()-1);
            if (map.getValueAt(p.getX(), p.getY()-1) == 'B'){
                map.setValueAt(p.getX(), p.getY()-1);
            }
        }

    }
    public void moveUp(){
        if (p.getX()!=0 && map.getValueAt(p.getX()-1, p.getY())!='W'){
            p.setX(p.getX()-1);
            if (map.getValueAt(p.getX()-1, p.getY()) == 'B'){
                map.setValueAt(p.getX()-1, p.getY());
            }
        }

    }
    public void moveDown(){
        if (p.getX()!=10 && map.getValueAt(p.getX()+1, p.getY())!='W'){
            p.setX(p.getX()+1);
            if (map.getValueAt(p.getX()+1, p.getY()) == 'B'){
                map.setValueAt(p.getX()+1, p.getY());
            }
        }

    }
    public Position getPosition(){
        return p;
    }
}
