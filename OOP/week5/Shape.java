public class Shape {
    protected String color = "red";
    protected boolean filled = true;
    Shape(){

    }
    Shape(String color, boolean filled){
        this.color = color;
        this.filled = filled;
    }
    public String getColor(){ return color;}
    public void setColor(String color){ this.color = color;}
    public boolean isFilled(){ return filled;}
    public void setFilled(boolean filled){ this.filled = filled;}
    public String toString(){ return "Shape[" + color + ", " + filled + "]";}
}

class Circle extends Shape{
    protected double radius = 1.0;
    Circle(String color, boolean filled, double radius){
        super(color,filled);
        this.radius = radius;
    }
    public double getRadius(){ return radius;}
    public  void setRadius(double radius){this.radius = radius;}
    public double getArea(){ return radius * radius * 3.14;}
    public double getPerimeter(){ return 2 * radius * 3.14;}
    public String toString(){ return "Circle[Shape[" + color + ", " + filled + "], " + radius + "]";}
}

class Rectanglee extends Shape{
    protected double width = 1.0;
    protected double length = 1.0;
    Rectanglee(){
    }

    Rectanglee(String color, boolean filled, double width, double length){
        super(color, filled);
        this.width = width;
        this.length = length;
    }
    public double getWidth(){ return width;}
    public void setWidth(double width){this.width = width;}
    public double getLength(){ return length;}
    public void setLength(double length){this.length = length;}
    public double getArea(){ return length * width;}
    public double getPerimeter(){ return 2 * (length + width);}
    public String toString(){ return "Rectangle[Shape[" + color + ", " + filled + "]," + width + ", " + length + "]";}
}

class Square extends Rectanglee{
    protected double side = 1.0;
    Square(double side, String color, boolean filled){
        this.width = side;
        this.length = side;
        this.color= color;
        this.filled = filled;
    }

    public double getSide(){return side;}
    public void setSide(double side){
        this.width = side;
        this.length = side;
        this.side = side;
    }
    public String toString(){ return "Square[Rectangle[Shape[" + color + ", " + filled + "]," + width + ", " + length + "]]";}
}
