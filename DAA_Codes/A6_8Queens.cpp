#include <iostream>
#include <cstdlib>
using namespace std;

int board[8];

bool isSafe(int row, int col) {
    for (int r = 0; r < 8; r++)
        if (r != row && board[r] != -1)
            if (board[r] == col || abs(board[r] - col) == abs(r - row))
                return false;
    return true;
}

bool solve(int row) {
    if (row == 8) return true;
    if (board[row] != -1) return solve(row + 1);
    for (int col = 0; col < 8; col++)
        if (isSafe(row, col)) {
            board[row] = col;
            if (solve(row + 1)) return true;
            board[row] = -1;
        }
    return false;
}

int main() {
    int r, c;
    cout << "Enter row and column of first queen (0-7): ";
    cin >> r >> c;
    for (int i = 0; i < 8; i++) board[i] = -1;
    board[r] = c;

    if (solve(0))
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++)
                cout << (board[i] == j ? "Q " : ". ");
            cout << endl;
        }
    else
        cout << "No solution" << endl;
    return 0;
}
