import java.util.Scanner ;
public class scannerfloat {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in) ;
      long s = 0 ;
      while (sc.hasNext())
         s += sc.nextDouble() ;
      System.out.println(s) ;
   }
}
