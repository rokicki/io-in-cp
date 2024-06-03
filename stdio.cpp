#include <cstdio>
using namespace std ;
using ll = long long ;
int main(int argc, char *argv[]) {
   ll s = 0 ;
   ll v ;
   while (scanf("%lld", &v) == 1)
      s += v ;
   printf("%lld\n", s) ;
}
