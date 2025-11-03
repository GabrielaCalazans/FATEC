#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;



int main() {
	cout << "HELLO WORLD!" << endl;

    cout << "******** EX 3 *********" << endl;
    double x = 0, a = 10, b = 4, *pta, *ptb;
    pta = &a;
    ptb = &b;
    x = *pta + *ptb;
    cout << "ex 3 x = " << x << endl;

    cout << "******* EX 4 *********" << endl;
    int x = 10;

    cout << "******* EX 5 *********" << endl;

    cout << "******* EX 6 *********" << endl;

    cout << "******* EX 7 *********"  << endl;
    int x7 = 10;
    int *ptx7;
    ptx7 = &x7;
    free(ptx7); // Note: This is incorrect, as ptx points to a stack variable.

    cout << "******* EX 8 *********"  << endl;
    cout << "******* EX 9 *********"  << endl;
    cout << "******* EX 10 *********" << endl;
	return 0;
}