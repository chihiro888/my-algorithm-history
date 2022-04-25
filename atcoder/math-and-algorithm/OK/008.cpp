#include <iostream>

using namespace std;

int main() {
    int N, S;
    int solve = 0;
    cin >> N >> S;
    
    for (int i=1; i<N+1; i++) {
        for (int j=1; j<N+1; j++) {
            if (i+j <= S) {
                solve++;
            }
        }
       
    }
    printf("%d", solve);
    return 0;
}

/*
    008 - Brute Force 1
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31265088
*/