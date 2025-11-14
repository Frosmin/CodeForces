#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, a;
        cin >> n >> a;
        vector<int> v(n);
        int left = 0, right = 0;
        for (int i = 0; i < n; i++) {
            cin >> v[i];
            if (v[i] < a) left++;
            else if (v[i] > a) right++;
        }
        if (left == 0 && right == 0) {
            cout << 1337 << endl;
        } else if (right > left) {
            cout << a + 1 << endl;
        } else {
            cout << a - 1 << endl;
        }
    }
    return 0;
}