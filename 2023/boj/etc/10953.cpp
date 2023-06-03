#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

vector<string> split(string input)
{
    vector<string> result;
    stringstream ss(input);
    string token;

    while (getline(ss, token, ','))
    {
        result.push_back(token);
    }

    return result;
}

int main()
{
    int size;
    cin >> size;

    REP(i, size)
    {
        string data;
        cin >> data;

        vector<string> result = split(data);

        cout << stoi(result[0]) + stoi(result[1]) << endl;
    }
    return 0;
}