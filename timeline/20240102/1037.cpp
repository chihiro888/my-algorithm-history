#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <algorithm>
#include <cstdio>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);

    vector<int> d;
    REP(i, n) {
        int t;
        scanf("%d", &t);
        d.push_back(t);
    }

    int min_value = *min_element(d.begin(), d.end());
    int max_value = *max_element(d.begin(), d.end());
    
    cout << min_value * max_value;

    return 0;
}
