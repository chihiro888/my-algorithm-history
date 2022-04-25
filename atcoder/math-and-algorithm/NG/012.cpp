#include <iostream>

using namespace std;

bool isPrime(long long n)
{
    // Corner case
    if (n <= 1)
        return false;
  
    // Check from 2 to n-1
    for (long long i = 2; i < n; i++)
        if (n % i == 0)
            return false;
  
    return true;
}

int main() {
    long long N;
    cin >> N;
    isPrime(N) ? cout << "YES\n" : cout << "No\n";
    
    return 0;
}

/*
    012 - Primality Test
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_l
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31267256

    AC x 16
    WA x 11
    TLE x 6  
*/