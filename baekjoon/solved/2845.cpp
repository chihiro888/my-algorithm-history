#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int l1, l2;
    int p1, p2, p3, p4, p5;
    cin >> l1 >> l2 >> p1 >> p2 >> p3 >> p4 >> p5;
    int l = l1 * l2;
    printf("%d %d %d %d %d", p1-l, p2-l, p3-l, p4-l, p5-l);
    return 0;
}