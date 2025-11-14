#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

void solve() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    std::vector<long long> prefijo(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        prefijo[i + 1] = prefijo[i] + a[i];
    }

    long long original = prefijo[n];
    long long maximos = 0;

    for (int l = 0; l < n; ++l) {
        for (int r = l; r < n; ++r) {
            long long tam = r - l + 1;
            long long nuevo = (long long)(l + 1) + (r + 1);
            long long subarray_sum = prefijo[r + 1] - prefijo[l];
            long long improvement = tam * nuevo - subarray_sum;
            maximos = std::max(maximos, improvement);
        }
    }

    std::cout << original + maximos << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
