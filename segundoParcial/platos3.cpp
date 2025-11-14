#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;
    int rev;
    int cap;
    Edge(int _to, int _rev, int _cap): to(_to), rev(_rev), cap(_cap) {}
};

struct Dinic {
    int N;
    vector<vector<Edge>> G;
    vector<int> level, it;
    Dinic(int n): N(n), G(n), level(n), it(n) {}

    void addEdge(int u, int v, int c) {
        G[u].emplace_back(v, (int)G[v].size(), c);
        G[v].emplace_back(u, (int)G[u].size()-1, 0);
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s] = 0;
        q.push(s);
        while(!q.empty()) {
            int u = q.front(); q.pop();
            for(const Edge &e : G[u]) {
                if(level[e.to] < 0 && e.cap > 0) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] >= 0;
    }

    int dfs(int u, int t, int f) {
        if(u == t) return f;
        for(int &i = it[u]; i < (int)G[u].size(); ++i) {
            Edge &e = G[u][i];
            if(e.cap > 0 && level[e.to] == level[u] + 1) {
                int ret = dfs(e.to, t, min(f, e.cap));
                if(ret > 0) {
                    e.cap -= ret;
                    G[e.to][e.rev].cap += ret;
                    return ret;
                }
            }
        }
        return 0;
    }

    int maxflow(int s, int t) {
        int flow = 0;
        while(bfs(s,t)) {
            fill(it.begin(), it.end(), 0);
            while(true) {
                int f = dfs(s,t, INT_MAX);
                if(f == 0) break;
                flow += f;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if(!(cin >> n >> m)) return 0;
    vector<int> c(n+1);
    for(int i=1;i<=n;++i) cin >> c[i];

    int S = 0;
    int T = n + m + 1;
    Dinic D(T+1);

    for(int i=1;i<=n;++i) if(c[i] > 0) D.addEdge(S, i, c[i]);

    for(int j=1;j<=m;++j) {
        int k; cin >> k;
        int customerNode = n + j;
        for(int t=0;t<k;++t) {
            int p; cin >> p; 
            if(p >=1 && p <= n) {
                D.addEdge(p, customerNode, 1);
            }
        }

        D.addEdge(customerNode, T, 1);
    }

    int ans = D.maxflow(S, T);
    cout << ans << "\n";
    return 0;
}
