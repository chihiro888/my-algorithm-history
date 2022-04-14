#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int kingBlack = 1;
    int queenBlack = 1;
    int rookBlack = 2;
    int bishopBlack = 2;
    int knightBlack = 2;
    int pawnBlack = 8;
    int kingWhite, queenWhite, rookWhite, bishopWhite, knightWhite, pawnWhite;
    cin >> kingWhite >> queenWhite >> rookWhite >> bishopWhite >> knightWhite >>pawnWhite;
    printf(
        "%d %d %d %d %d %d", 
        kingBlack-kingWhite,
        queenBlack-queenWhite,
        rookBlack-rookWhite,
        bishopBlack-bishopWhite,
        knightBlack-knightWhite,
        pawnBlack-pawnWhite
    );
    return 0;
}