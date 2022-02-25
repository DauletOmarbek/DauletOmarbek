import java.time.Year;

public class Person {
    protected String name;
    protected String address;
    Person(String name, String address){
        this.name = name;
        this.address = address;
    }
    public String getName(){ return name;}
    public String getAddress(){ return  address;}
    public void setAddress( String address){ this.address = address;}
    public String toString(){ return "Person" +"[" + name + ", " + address + "]";}
}
class Student extends Person {
    protected String program;
    protected int year;
    protected double fee;
    Student(String name, String address, String program, int year, double fee){
        super(name, address);
        this.program = program;
        this.year = year;
        this.fee = fee;
    }
    public String getProgram(){return program;}
    public void setProgram(String program){this.program = program;}
    public int getYear(){return year;}
    public void setYear(int year ){this.year = year;}
    public double getFee(){return fee;}
    public void setFee(double fee ){this.fee = fee;}
    public String toString(){ return "Student[Person[" + name + ", " + address + "], " + program + ", " + year + ", " + fee + "]";}
}

class Staff extends Person{
    protected String school;
    protected double pay;
    Staff(String name, String address, String school, double pay){
        super(name, address);
        this.school = school;
        this.pay = pay;
    }
    public String getSchool(){ return school;}
    public void setSchool(String school){this.school = school;}
    public double getPay(){ return pay;}
    public void setPay(double pay){this.pay = pay;}
    public String toString(){ return "Staff[Person[" + name + ", " + address + "], " + school + ", " + pay + "]";}
}
