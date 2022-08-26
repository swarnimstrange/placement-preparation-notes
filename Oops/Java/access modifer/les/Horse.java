package les;
import animal.*;

// When declared protected we can access it through only subclass

// class Pony extends Animal {
//     Pony() {
//         System.out.println(eyes);
//         walk();
//     }

// }

public class Horse {
    public static void main(String args[]){
        // Pony p = new Pony();

        // When declared public we can access it from any package and in any class
        Animal a = new Animal();
        System.out.println(a.eyes);
        a.walk();
    }
}
