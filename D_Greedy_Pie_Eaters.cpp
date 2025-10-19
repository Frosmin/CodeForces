#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin("pieaters.in");
    ofstream fout("pieaters.out");
    if (!fin) { fout << 0 << "\n"; return 0; }

    int n, m;
    fin >> n >> m;
    const int stride = n + 1;
    const int size = stride * stride;

    vector<vector<int>> best(n + 1, vector<int>(size, 0));

    for (int i = 0; i < m; ++i) {
        int w, l, r;
        fin >> w >> l >> r;
        int idx = l * stride + r;
        for (int pivot = l; pivot <= r; ++pivot) {
            best[pivot][idx] = max(best[pivot][idx], w);
        }
    }

    for (int pivot = 1; pivot <= n; ++pivot) {
        auto &arr = best[pivot];
        for (int length = 1; length <= n; ++length) {
            int min_l = max(1, pivot - length + 1);
            int max_l = min(pivot, n - length + 1);
            if (min_l > max_l) continue;
            for (int l = min_l; l <= max_l; ++l) {
                int r = l + length - 1;
                int idx = l * stride + r;
                int val = arr[idx];
                if (l < pivot) val = max(val, arr[(l + 1) * stride + r]);
                if (r > pivot) val = max(val, arr[l * stride + (r - 1)]);
                arr[idx] = val;
            }
        }
    }

    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));
    for (int length = 1; length <= n; ++length) {
        for (int l = 1; l + length - 1 <= n; ++l) {
            int r = l + length - 1;

            long long best_split = 0;
            for (int k = l; k < r; ++k) {
                best_split = max(best_split, dp[l][k] + dp[k + 1][r]);
            }

            long long res = best_split;
            int idx = l * stride + r;
            for (int pivot = l; pivot <= r; ++pivot) {
                int w = best[pivot][idx];
                if (w == 0) continue;
                long long total = w;
                if (pivot > l) total += dp[l][pivot - 1];
                if (pivot < r) total += dp[pivot + 1][r];
                res = max(res, total);
            }

            dp[l][r] = res;
        }
    }

    fout << dp[1][n] << "\n";
    return 0;
}