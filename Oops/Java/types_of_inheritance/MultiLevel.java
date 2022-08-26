
class Shape {
    Shape(){
    System.out.println("Printing Outline");
    }
}

class Traingle extends Shape{
    Integer length;
    Integer height;

}

class EquiTraingle extends Traingle{
    EquiTraingle(){
    if (length == height){
        System.out.println("this is a Equilateral Traingle.");        
        }
    }
    void area(){
        System.out.println(height*length*1/2);
    } 
}


public class MultiLevel {
    public static void main(String args[]){
        EquiTraingle et1 = new EquiTraingle();
        et1.length = 6;
        et1.height = 6;
        et1.area();
    }
}