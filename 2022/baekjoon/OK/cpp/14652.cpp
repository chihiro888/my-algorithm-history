#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m, idx;
    cin >> n >> m >> idx;

    for (int i = 1; i < n+1; i++) {
        if (m * i > idx) {
            printf("%d %d", i - 1, m - ((m * i) - idx));
            break;
        }
    }
    
    return 0;
}