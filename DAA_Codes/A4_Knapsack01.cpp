#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, W, wt[20], val[20], dp[21][101];
    cout << "Enter number of items: ";
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cout << "Enter weight and value: ";
        cin >> wt[i] >> val[i];
    }
    cout << "Enter capacity: ";
    cin >> W;

    for (int i = 0; i <= n; i++)
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i] <= w)
                dp[i][w] = max(val[i] + dp[i - 1][w - wt[i]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }

    cout << "Maximum value = " << dp[n][W] << endl;
    return 0;
}
