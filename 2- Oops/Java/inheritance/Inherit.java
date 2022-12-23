class Shape {
    String name;

    void printInfo(){
        System.out.println(name +" is graphical representation of an object");
    }
}

class Traingle extends Shape {

}




public class Inherit {
    public static void main(String args[]){
        Traingle t1 = new Traingle();
        t1.name = "Traingle";
        t1.printInfo();
    }
}