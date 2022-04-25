#include <iostream>
#include <cmath>

using namespace std;

void printPrimeFactors(int n) {
   while (n%2 == 0){
      cout<<"2 ";
      n = n/2;
   }
   for (int i = 3; i <= sqrt(n); i = i+2){
      while (n%i == 0){
         cout<<i<<" ";
         n = n/i;
      }
   }
   if (n > 2)
   cout<<n<<" ";
}

int main() {
    int N;
    cin >> N;
    printPrimeFactors(N);
    return 0;
}

/*
    014 - Factorization
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_n
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31267873
    
    AC x 3
    WA x 21
*/