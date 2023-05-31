#include <iostream>
#include <string>
#include <stack>
#include <vector>

#define FOR(i, start, end) for(int i = start; i < end; ++i)
#define REP(i,n) FOR(i,0,n)

using namespace std;

int main() {
    string d;
    int l;
    cin >> d;
    cin >> l;
    cin.ignore();

    int cursor = d.size();

    int i;
    REP(i, l) {
        string command;
        getline(cin, command);

        char opcode = command[0];

        char data = command[2];
        string t = "";
        t += data;

        if (opcode == 'P') {
            d.insert(cursor, t);
            cursor++;
        } else if (opcode == 'L' && cursor != 0) {
            cursor--;
        } else if (opcode == 'D' && cursor != d.size()) {
            cursor++;
        } else if (opcode == 'B' && cursor != 0) {
            d.erase(cursor-1, 1);
            cursor--;
        }
    }

    cout << d << endl;

    return 0;
}