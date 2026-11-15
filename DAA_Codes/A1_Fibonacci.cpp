#include <iostream>
using namespace std;

int steps = 0;

int fib(int n) {
    steps++;
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n, a = 0, b = 1, count = 0;
    cout << "Enter n: ";
    cin >> n;

    cout << "Iterative: ";
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        int next = a + b;
        a = b;
        b = next;
        count++;
    }
    cout << "\nSteps = " << count << endl;

    cout << "Recursive: ";
    for (int i = 0; i < n; i++)
        cout << fib(i) << " ";
    cout << "\nSteps = " << steps << endl;
    return 0;
}
