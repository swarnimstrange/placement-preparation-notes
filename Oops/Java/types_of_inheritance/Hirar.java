class Traingle {
    Integer side1;
    Integer side2;
    Integer side3;
}

class Equilateral extends Traingle {
    void printInfo() {
        if (side1 == side2 && side2 == side3) {
            System.out.println("This is an Equilateral Traingle");
        }
    }
}

class Scalane extends Traingle {
    void printInfo() {
        if ((side1 != side2) || (side2 != side3) || (side1 != side3)) {
            System.out.println("This is an Scalane Traingle");
        }
    }
}

public class Hirar {
    public static void main(String args[]) {
        Equilateral et1 = new Equilateral();
        et1.side1 = 6;
        et1.side2 = 6;
        et1.side3 = 6;
        et1.printInfo();
        Scalane et2 = new Scalane();
        et2.side1 = 6;
        et2.side2 = 7;
        et2.side3 = 8;
        et2.printInfo();
    }

}