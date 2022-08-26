class Mail {
    String name;
    String email_id;
    private String password;

    void setPassword(String pass){
        this.password = pass;
    }

    public String getPassword() {
        return password;
    }

} 

public class Encap{
public static void main(String args[]) {
    Mail mail = new Mail();
    mail.name = "Swarnim Rai";
    mail.email_id = "swarnimstrange@gmail.com";

    System.out.println(mail.name);
    System.out.println(mail.email_id);
    mail.setPassword("Hello@1234");
    System.out.println(mail.getPassword());
}
}