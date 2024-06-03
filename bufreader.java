import java.io.* ;
public class bufreader {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in)) ;
      long s = 0 ;
      String str ;
      while ((str = br.readLine()) != null)
         s += Integer.parseInt(str) ;
      System.out.println(s) ;
   }
}
