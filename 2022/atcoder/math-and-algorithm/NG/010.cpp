#include <iostream>

using namespace std;

int factorial(unsigned long long N) {
    if (N == 1) return 1;
    return factorial(N-1) * N;
}

int main() {
    unsigned long long N;
    cin >> N;
    printf("%d", factorial(N));
    return 0;
}

/*
    010 - Factorial
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_j
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31265564

    AC x 13
    WA x 8
*/