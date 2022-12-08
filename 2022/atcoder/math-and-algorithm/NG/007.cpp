#include <iostream>

using namespace std;

int main() {
    int N, X, Y;
    cin >> N >> X >> Y;
    
    printf("%d", (N/X)+(N/Y)-(N/(X*Y)));
    return 0;
}

/*
    007 - Number of Multiples 1
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_g
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31264848

    AC x 22
    WA x 1
*/