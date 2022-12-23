class IT {
    String dept;
    Integer salary;

    void printInfo(String dept){
        System.out.println(dept + " in IT industry" + " has good salary ");
    }

    void printInfo(Integer salary){
        System.out.println(salary + " is considered as good salary ");
    }

    void printInfo(String dept, Integer salary){
        System.out.println(dept + " in IT industry has " + salary + " salary");
    }
}


public class Poly {
    public static void main(String args[]){
        IT it1 = new IT();
        it1.dept = "Software Development";
        it1.salary = 60000;
        it1.printInfo(it1.dept);
        it1.printInfo(it1.salary);
        it1.printInfo(it1.dept, it1.salary);
    }
}