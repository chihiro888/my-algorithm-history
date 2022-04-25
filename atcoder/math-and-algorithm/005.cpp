#include <iostream>

using namespace std;

int main() {
    int N, a;
    int sum = 0;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a;
        sum += a;
    }
    printf("%d", sum % 100);
    return 0;
}

/*
    005 - Modulo 100
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_e

    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31264707
*/