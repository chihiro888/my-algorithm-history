#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, S;
    cin >> N >> S;
    vector<int> A;
    int x;
    for (int i=0; i<N; i++) {
        cin >> x;
        A.push_back(x);
    }

    bool solve = false;
    for (int i=0; i<A.size(); i++){
        for (int j=i+1; j<A.size(); j++){
            if (A[i] + A[j] == S) {
                solve = true;
                break;
            }
        }
        if (solve) break;
    }

    if (solve) {
        printf("YES");
    } else {
        printf("No");
    }
    
    return 0;
}

/*
    009 - Brute Force 2
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_i
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31265327

    AC x 10
    WA x 14
*/