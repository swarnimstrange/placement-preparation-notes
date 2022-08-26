class Human {
    String name;
    String nature;
    Integer age;

    Human(Human h) {
        this.name = h.name;
        this.nature = h.nature;
        this.age = h.age;
    }

    void printInfo() {
        System.out.println("Human's name is " + this.name + " with " + this.nature + " nature and age is " + this.age);
    }

    Human() {}
}

public class CopyCon {
    public static void main(String args[]) {
        Human h1 = new Human();
        h1.name = "Swarnim";
        h1.nature = "Kind";
        h1.age = 22;
        Human h2 = new Human(h1);
        h2.printInfo();
    }

}
