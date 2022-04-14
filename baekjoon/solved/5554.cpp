#include <iostream>

using namespace std;

int main() {
    int h, s, p, a;
    cin >> h >> s >> p >> a;
    int sum = h + s + p + a;
    cout << sum/60 << endl;
    cout << sum%60 << endl;
    return 0;
}