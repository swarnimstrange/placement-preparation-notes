class ParaConstructor {
    String model;
    Integer milage; 

    ParaConstructor(String model, Integer milage) {
        this.model = model;
        this.milage = milage;
    }

    void printi() {
        System.out.println("Car's model is "+ this.model + " and milage is " + this.milage);
    }
}


public class Para {
    public static void main(String[] args) {
        ParaConstructor pc = new ParaConstructor("Maruti Suzuki", 27);
        pc.printi();
    }
    
}
