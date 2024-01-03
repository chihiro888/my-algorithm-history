#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <stack>
#include <vector>
#include <math.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FOREACH(i, container) for (auto i = container.begin(); i != container.end(); ++i)
#define ALL(container) container.begin(), container.end()

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    REP(i, t) {
        int x1, y1, r1, x2, y2, r2;
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        int result;
        double distanse = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
        double subtract = r1 > r2 ? r1 - r2 : r2 - r1;
        if(distanse == 0 && r1 == r2) result = -1;
        else if(distanse < r1 + r2 && (subtract < distanse)) result = 2;
        else if(distanse == r1 + r2 || distanse == subtract) result = 1;
        else result = 0;
        printf("%d\n", result);
    }
    return 0;
}