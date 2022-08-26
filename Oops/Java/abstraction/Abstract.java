abstract class Bike{
    Integer price;
    Integer milage;
    static Integer wheels=2;

    abstract void drive();
}

class HeroBike extends Bike{
    String model;

    void drive(){
        System.out.println("Hero " + model + " drives");
    }

    void printinfo(){
        System.out.println("No of wheels: " + wheels);
        System.out.println("Price: " + price);
        System.out.println("Milage: " + milage);
    }
}

public class Abstract{
public static void main(String args[]){
    HeroBike hb = new HeroBike();
    hb.model = "Glamour";
    hb.price = 45000;
    hb.milage = 75;
    hb.drive();
    hb.printinfo();
}
}