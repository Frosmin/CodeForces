#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>
using namespace std;

bool bfs(vector<vector<int>>& graph, int source, int sink, vector<int>& parent) {
    int n = graph.size();
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(source);
    visited[source] = true;
    parent[source] = -1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] > 0) {
                if (v == sink) {
                    parent[v] = u;
                    return true;
                }
                q.push(v);
                visited[v] = true;
                parent[v] = u;
            }
        }
    }
    return false;
}

int edmondsKarp(vector<vector<int>>& graph, int source, int sink) {
    int n = graph.size();
    vector<int> parent(n);
    int maxFlow = 0;

    while (bfs(graph, source, sink, parent)) {
        int pathFlow = INT_MAX;
        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            pathFlow = min(pathFlow, graph[u][v]);
        }

        for (int v = sink; v != source; v = parent[v]) {
            int u = parent[v];
            graph[u][v] -= pathFlow;
            graph[v][u] += pathFlow;
        }
        maxFlow += pathFlow;
    }
    return maxFlow;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> capacities(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> capacities[i];
    }

    int totalNodes = n + m + 2;
    vector<vector<int>> graph(totalNodes, vector<int>(totalNodes, 0));
    int source = 0;
    int sink = totalNodes - 1;

    for (int i = 1; i <= n; i++) {
        graph[source][i] = capacities[i];
    }

    for (int i = 1; i <= m; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int plate;
            cin >> plate;
            graph[plate][n + i] = 1;
        }
        graph[n + i][sink] = 1;
    }

    int maxFlow = edmondsKarp(graph, source, sink);
    cout << maxFlow << endl;

    return 0;
}