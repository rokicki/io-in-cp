import java.util.Scanner ;
public class nextline {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      long s = 0 ;
      try {
         while (true)
            s += Integer.parseInt(sc.nextLine()) ;
      } catch (Exception e) {}
      System.out.println(s) ;
   }
}
