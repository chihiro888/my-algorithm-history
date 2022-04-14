#include <iostream>

using namespace std;

int main() {
    int ax, ay, az;
    int bx, by, bz;
    cin >> ax >> ay >> az;
    cin >> bx >> by >> bz;
    printf("%d %d %d", bx-az, by/ay, bz-ax);
    return 0;
}