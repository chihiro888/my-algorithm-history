#include <iostream>

using namespace std;

int main() {
    long long N;
    cin >> N;
    for (int i=1; i<N+1; i++) {
        if (N % i == 0) {
            printf("%d\n", i);
        }
    }    
    return 0;
}

/*
    013 - Divisor Enumeration
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_m#
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31267749

    AC x 12
    TLE x 11
*/