#include <iostream>

using namespace std;

int main() {
    int N, T, C, P;
    cin >> N >> T >> C >> P;

    int X;
    if (N % T == 0) {
        X = (N/T)-1;
    } else {
        X = (N/T);
    }
    cout << X * C * P << endl;
    
    return 0;
}