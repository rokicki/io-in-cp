import java.io.* ;
public class bufreaderfloat {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
      long s = 0 ;
      String str ;
      while ((str = br.readLine()) != null)
         s += Double.parseDouble(str) ;
      System.out.println(s) ;
   }
}
