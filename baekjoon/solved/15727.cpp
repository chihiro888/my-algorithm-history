#include <iostream>

using namespace std;

int main() {
    int L;
    cin >> L;
    if (L%5 == 0) {
        cout << L/5 << endl;
    } else {
        cout << (L/5) + 1 << endl;
    }
    return 0;
}