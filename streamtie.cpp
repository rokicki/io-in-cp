#include <iostream>
using namespace std ;
using ll = long long ;
int main(int argc, char *argv[]) {
   ios_base::sync_with_stdio(false) ;
   cin.tie(NULL) ;
   ll s = 0 ;
   ll v ;
   while (cin >> v)
      s += v ;
   cout << s << endl ;
}
