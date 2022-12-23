class Student{
    static String school;
    String name;

    void printInfo(){
        System.out.println("Name of Student: " + name);
    }

    static void School() {
        System.out.println("Student is currently enrolled in " + school + " School");
    }
}

public class stat {
    public static void main(String args[]){
        Student s1 = new Student();
        s1.name = "Diksha";
        Student.school = "DVP";
        Student s2 = new Student();
        s2.name = "Parth";
        s1.printInfo();
        Student.School();
    }
}