#include <iostream>
using namespace std;

int main() {
    int n, k, C[20][20];
    cout << "Enter n and k: ";
    cin >> n >> k;

    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= i && j <= k; j++)
            if (j == 0 || j == i)
                C[i][j] = 1;
            else
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];

    cout << "C(" << n << "," << k << ") = " << C[n][k] << endl;
    return 0;
}
