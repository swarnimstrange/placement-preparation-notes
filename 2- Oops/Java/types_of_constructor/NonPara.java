class NonParaConstructor {
    String name;
    String address;

    void printInfo() {
        System.out.println("Name: " + this.name);
        System.out.println("Address: " + this.address);
    }

    NonParaConstructor() {
        System.out.println("Non-Parameterized Constructor called");
    }
}

public class NonPara {
    public static void main(String[] args) {
        NonParaConstructor npc1 = new NonParaConstructor();
        npc1.name = "Swarnim";
        npc1.address = "Pune";
        npc1.printInfo();
        System.out.println();

        NonParaConstructor npc2 = new NonParaConstructor();
        npc2.name = "Piyush";
        npc2.address = "Pune";
        npc2.printInfo();
    }
}
