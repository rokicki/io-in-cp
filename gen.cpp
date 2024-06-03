#include <iostream>
#include <cstdlib>
using namespace std ;
using ll = long long ;
int main(int argc, char *argv[]) {
   ll n = atol(argv[1]) ;
   for (int i=0; i<n; i++)
      cout << lrand48() << endl ;
}
