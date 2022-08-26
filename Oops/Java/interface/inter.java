interface Laptop{
    String screen = "24 cm";
    void charge();

}

class HP implements Laptop{
    String model;
    Integer price;
    public void charge(){
        System.out.println("Laptop is getting charged");
    }

    void printInfo(){
        System.out.println("Hp " + model + " with " + screen);
        System.out.println("Price: " + price);
    }
}



public class inter {
    public static void main(String args[]){
        HP hp = new HP();
        hp.model = "Pavilion";
        hp.price = 750000;
        hp.charge();
        hp.printInfo();
    }
}