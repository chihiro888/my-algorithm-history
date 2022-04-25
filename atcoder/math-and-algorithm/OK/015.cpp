#include <iostream>

using namespace std;

int gcd(int a, int b)
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int main() {
    int A, B;
    cin >> A >> B;
    cout << gcd(A, B);
    return 0;
}

/*
    015 - Greatest Common Divisor
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_o
    
    submit
    https://atcoder.jp/contests/math-and-algorithm/submissions/31268101
*/