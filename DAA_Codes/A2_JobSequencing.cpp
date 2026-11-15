#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, id[20], d[20], p[20], slot[20] = {0}, maxD = 0, total = 0;
    cout << "Enter number of jobs: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter id, deadline, profit: ";
        cin >> id[i] >> d[i] >> p[i];
        if (d[i] > maxD) maxD = d[i];
    }

    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (p[j] < p[j + 1]) {
                swap(p[j], p[j + 1]);
                swap(d[j], d[j + 1]);
                swap(id[j], id[j + 1]);
            }

    for (int i = 0; i < n; i++)
        for (int t = d[i]; t >= 1; t--)
            if (slot[t] == 0) {
                slot[t] = id[i];
                total += p[i];
                break;
            }

    cout << "Sequence: ";
    for (int t = 1; t <= maxD; t++)
        if (slot[t] != 0) cout << "J" << slot[t] << " ";
    cout << "\nTotal profit = " << total << endl;
    return 0;
}
