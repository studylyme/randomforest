#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    float v[20], w[20], r[20], W, total = 0;
    cout << "Enter number of items: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter value and weight: ";
        cin >> v[i] >> w[i];
        r[i] = v[i] / w[i];
    }
    cout << "Enter capacity: ";
    cin >> W;

    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (r[j] < r[j + 1]) {
                swap(r[j], r[j + 1]);
                swap(v[j], v[j + 1]);
                swap(w[j], w[j + 1]);
            }

    for (int i = 0; i < n; i++) {
        if (W >= w[i]) {
            W -= w[i];
            total += v[i];
        } else {
            total += v[i] * (W / w[i]);
            break;
        }
    }
    cout << "Maximum value = " << total << endl;
    return 0;
}
