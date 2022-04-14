#include <iostream>

using namespace std;

int main() {
    int album, avg;
    cin >> album >> avg;
    cout << (album * (avg - 1)) + 1 << endl;
    return 0;
}