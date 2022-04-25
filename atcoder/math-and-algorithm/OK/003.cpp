#include <iostream>

using namespace std;

int main() {
    int N;
    int A;
    int sum = 0;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> A;
        sum += A;
    }
    printf("%d", sum);
    return 0;
}

/*
    003 - Sum of N Integers
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_c

    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31264626
*/