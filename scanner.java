import java.util.Scanner ;
public class scanner {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      long s = 0 ;
      while (sc.hasNext())
         s += sc.nextInt() ;
      System.out.println(s) ;
   }
}
