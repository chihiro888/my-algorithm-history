#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
    string d;
    cin >> d;
    
    stack<char> s;
    int count = 0;

    for (int i=0; i<d.size(); i++) {
        char curr = d[i];
        char prev = d[i-1];

        if (curr == '(') {
            s.push(curr);
        } else {
            if (prev == '(') {
                s.pop();
                count += s.size();
            } else {
                s.pop();
                count += 1;
            }
        }
    }

    cout << count;

    return 0;
}