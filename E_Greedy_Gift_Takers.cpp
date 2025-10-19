#include <bits/stdc++.h>
using namespace std;

struct SegTree {
    int n;
    vector<int> tree, lazy;
    SegTree(int n) : n(n), tree(4 * n + 4), lazy(4 * n + 4) {
        build(1, 1, n);
    }
    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = -l;
            return;
        }
        int mid = (l + r) >> 1;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        tree[node] = max(tree[node << 1], tree[node << 1 | 1]);
    }
    void push(int node) {
        if (lazy[node]) {
            int val = lazy[node];
            tree[node << 1] += val;
            tree[node << 1 | 1] += val;
            lazy[node << 1] += val;
            lazy[node << 1 | 1] += val;
            lazy[node] = 0;
        }
    }
    void update(int node, int l, int r, int ql, int qr, int val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        push(node);
        int mid = (l + r) >> 1;
        update(node << 1, l, mid, ql, qr, val);
        update(node << 1 | 1, mid + 1, r, ql, qr, val);
        tree[node] = max(tree[node << 1], tree[node << 1 | 1]);
    }
    int queryMax() const { return tree[1]; }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<int> c(N + 1);
    for (int i = 1; i <= N; ++i) cin >> c[i];
    vector<int> p(N + 1);
    for (int i = 1; i <= N; ++i) p[i] = N - c[i];
    SegTree seg(N);
    int processed = N;
    bool stopped = false;
    for (int i = 1; i <= N; ++i) {
        seg.update(1, 1, N, p[i], N, 1);
        if (seg.queryMax() >= 0) {
            processed = i;
            stopped = true;
            break;
        }
    }
    if (!stopped) processed = N;
    cout << (N - processed) << '\n';
    return 0;
}