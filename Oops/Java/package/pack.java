import java.util.Scanner;

// java.util is  a package

class Hello {
    Hello(String name){
        System.out.println("Hello "+ name);
    }
}


public class pack {
    public static void main(String  args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name:");
        String name = sc.nextLine();
        Hello h = new Hello(name);

    }
} 