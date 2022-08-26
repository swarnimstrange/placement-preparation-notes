class Car {
    String name;
    String color;

    public void drive() {
        System.out.println("Driving");
    }

    public void printchar() {
        System.out.println(this.name);
        System.out.println(this.color);
    }
}

public class Object {
    public static void main(String[] args) {
        Car car1 = new Car();
        car1.color = "Black";
        car1.name = "BMW";
        car1.printchar();
        car1.drive();
    }

}