class Student {
    String name;
    int age;

    void PrintAbout() {
        System.out.println("Name: " + this.name);
        System.out.println("Age: " + this.age);
    }

    Student() {
        System.out.println("Student constructor");
    }

    // Student(String name, int age) {
    // this.name = name;
    // this.age = age;
    // }

}

public class Constructor {
    public static void main(String[] args) {
        Student s1 = new Student();
        // Student s1 = new Student("Gayatri", 22);
        s1.name = "Gayatri";
        s1.age = 21;
        s1.PrintAbout();
    }
}
