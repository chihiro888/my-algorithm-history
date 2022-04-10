#include <iostream>

using namespace std;

int main() {
    string num;
    cin >> num;
    
    cout << stoi(num, nullptr, 16) << endl;
    return 0;
}