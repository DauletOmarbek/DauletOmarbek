public class Point {
    protected float x = 0.0f;
    protected float y = 0.0f;
    Point(float x,float y){
        this.x=x;
        this.y=y;
    }

    public float getX(){
        return x;
    }

    public float getY(){
        return y;
    }

    public void setX(float xx){
        x = xx;
    }

    public void setY(float yy){
        y = yy;
    }

    public void setXY(float xx, float yy){
        x = xx;
        y = yy;
    }

    public float[] getXY(){
        float[] nums = new float[2];
        nums[0] = x;
        nums[1] = y;
        return nums;
    }

    public String toString(){
        return ("(" + x + "," + "y" + ")");
    }
}

class MovablePoint extends Point{
    protected float xSpeed = 0.0f;
    protected float ySpeed = 0.0f;
    MovablePoint(float xSpeed,float ySpeed,float x,float y){
        super(x,y);
        this.xSpeed=xSpeed;
        this.ySpeed=ySpeed;

    }

    public float getXSpeed(){
        return xSpeed;
    }

    public float getYSpeed(){
        return ySpeed;
    }

    public void setXSpeed(float xx){
        x = xx;
    }

    public void setYSpeed(float yy){
        y = yy;
    }

    public void setXYSpeed(float xx, float yy){
        xSpeed = xx;
        ySpeed = yy;
    }

    public float[] getSpeed(){
        float[] nums = new float[2];
        nums[0] = xSpeed;
        nums[1] = ySpeed;
        return nums;
    }

    public String toString(){
        return ("(" + xSpeed + "," + ySpeed + "),speed=(xs,ys)");
    }
    public void move(){
        x += xSpeed;
        y += ySpeed;
    }
}
