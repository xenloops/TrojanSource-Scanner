 //Clean example code
public class TrojanSource {
    public static void main(String[] args) {
        boolean isAdmin = false;
        /* begin Admins only */ if(isAdmin) {
            System.out.println("Congrats, you're an admin.");
            /* end Admins only */ }
    }
}