#include <cstdio>
using namespace std ;
using ll = long long ;
int main(int argc, char *argv[]) {
   ll s = 0 ;
   double v ;
   while (scanf("%lg", &v) == 1)
      s += v ;
   printf("%lld\n", s) ;
}
