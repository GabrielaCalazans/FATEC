// 1 b
// 2 c
// 3 c
// 4 c
// 5 d
// 6 c
// 7 a
// 8 b
// 9 c
// 10 a

// // 2
// #include "iostream"
// #include "math.h"
// using namespace std;
// bool igual(float a, float b) {
// return a==b;          }
// int main() {  cout << igual(10,"10"); } 
// b


// // 3
// #include "iostream"
// #include "math.h"
// using namespace std;
// int main ( ){
// int x=8;
// int y = 8; 
// float z = sqrt(x+y);
// x = z;
// y = sqrt(z);
// cout << x << endl  << y << endl << z << endl;}
// c


// // 4
// #include "iostream"
// #include "math.h"
// using namespace std;
// int main ( ) {
// double aux = 5, x =-1, y=2;
// aux=pow(x, x);
// y = x + aux;
// x = sqrt(aux);
// cout << x << endl << y << endl << aux;}
// c

// // // 5
// #include "iostream"
// #include "math.h"
// using namespace std;
// double  prod (double a, double b )
// { double x = sqrt(sqrt(a) + sqrt(b) );
//  return x;  }
// int main() {  double x = 9, y = 4;
// cout << prod(x,y)  - 1;   }
// d


// // 6
// #include "iostream"
// using namespace std;
// int getValor ( int pos ) {  int i; for (i=3; i<=5; i++)  if ( i % 2 == 0 ) break;
// return ( pos % i);    }
// int main(){ cout << getValor ( 15 ); }


// #include "iostream"
// using namespace std;
// int getValor ( int pos ) {  int i; for (i=3; i<=5; i++)  if ( i % 2 == 0 ) break;
// return ( pos % i);    }
// int main(){ cout << getValor ( 15 ); }
// c

// // // 7

// #include "iostream"
// using namespace std;
// int main(){  double  media =0, i=1;
// for (i=1; i<=4; i++)
// media += i;
// cout << media<< endl;}
// a

// // // 8
// #include <iostream>
// #include "math.h"
// using namespace std;
// int main(){ 
// int x [] = {1, 2, 8, 4, 5};  cout << sqrt( x [1] *  x[2]  );}
// b


// // 9

// #include <iostream>
// #include "math.h"
// using namespace std;
// struct me {int x; int y; int media;}  me1;
// int main(){  me1.x = 10; me1.y = pow(me1.x, 2);  cout << me1.x + me1.y << endl; }
// c

// // 10
// // #include “iostream”
// // using namespace std;
// int main(){ int x[] = {1,2,3,4,5};  cout << x[2] + x[3];}
// a


#include <iostream>
using namespace std;
int main(){ int x[] = {1,2,3,4,5};  cout << x[2] + x[3];}