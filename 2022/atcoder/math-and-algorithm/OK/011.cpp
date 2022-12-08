#include <iostream>
#include <bitset>

using namespace std;

bitset<500001> Primes;
void SieveOfEratosthenes(int n)
{
    Primes[0] = 1;
    for (int i = 3; i*i <= n; i += 2) {
        if (Primes[i / 2] == 0) {
            for (int j = 3 * i; j <= n; j += 2 * i)
                Primes[j / 2] = 1;
        }
    }
}

int main() {
    int N;
    cin >> N;
    SieveOfEratosthenes(N);
    for (int i = 1; i <= N; i++) {
        if (i == 2)
            cout << i << ' ';
        else if (i % 2 == 1 && Primes[i / 2] == 0)
            cout << i << ' ';
    }
    
    return 0;
}

/*
    011 - Print Prime Numbers
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_k
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31266904
*/