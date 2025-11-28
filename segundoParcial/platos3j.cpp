


#include <bits/stdc++.h>
using namespace std;

struct Arista {
    int destino;
    int reversa;
    int capacidad;
    Arista(int _destino, int _reversa, int _capacidad): destino(_destino), reversa(_reversa), capacidad(_capacidad) {}
};

struct Dinic {
    int N;
    vector<vector<Arista>> grafo;
    vector<int> nivel, iterador;
    Dinic(int n): N(n), grafo(n), nivel(n), iterador(n) {}

    void agregarArista(int u, int v, int c) {
        grafo[u].emplace_back(v, (int)grafo[v].size(), c);
        grafo[v].emplace_back(u, (int)grafo[u].size()-1, 0);
    }

    bool bfs(int fuente, int sumidero) {
        fill(nivel.begin(), nivel.end(), -1);
        queue<int> cola;
        nivel[fuente] = 0;
        cola.push(fuente);
        while(!cola.empty()) {
            int u = cola.front(); cola.pop();
            for(const Arista &arista : grafo[u]) {
                if(nivel[arista.destino] < 0 && arista.capacidad > 0) {
                    nivel[arista.destino] = nivel[u] + 1;
                    cola.push(arista.destino);
                }
            }
        }
        return nivel[sumidero] >= 0;
    }

    int dfs(int u, int sumidero, int f) {
        if(u == sumidero) return f;
        for(int &i = iterador[u]; i < (int)grafo[u].size(); ++i) {
            Arista &arista = grafo[u][i];
            if(arista.capacidad > 0 && nivel[arista.destino] == nivel[u] + 1) {
                int retorno = dfs(arista.destino, sumidero, min(f, arista.capacidad));
                if(retorno > 0) {
                    arista.capacidad -= retorno;
                    grafo[arista.destino][arista.reversa].capacidad += retorno;
                    return retorno;
                }
            }
        }
        return 0;
    }

    int flujoMaximo(int fuente, int sumidero) {
        int flujo = 0;
        while(bfs(fuente, sumidero)) {
            fill(iterador.begin(), iterador.end(), 0);
            while(true) {
                int f = dfs(fuente, sumidero, INT_MAX);
                if(f == 0) break;
                flujo += f;
            }
        }
        return flujo;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int numPlatos, numClientes;
    if(!(cin >> numPlatos >> numClientes)) return 0;
    vector<int> cantidadPlatos(numPlatos+1);

    for(int i=1;i<=numPlatos;++i) 
    {cin >> cantidadPlatos[i];}

    int fuente = 0;
    int sumidero = numPlatos + numClientes + 1;
    Dinic dinic(sumidero+1);

    for(int i=1;i<=numPlatos;++i) if(cantidadPlatos[i] > 0) dinic.agregarArista(fuente, i, cantidadPlatos[i]);

    for(int j=1;j<=numClientes;++j) {
        int k; cin >> k;
        int nodoCliente = numPlatos + j;
        for(int t=0; t<k ;++t) {
            int plato; cin >> plato; 
            if(plato >=1 && plato <= numPlatos) {
                dinic.agregarArista(plato, nodoCliente, 1);
            }
        }

        dinic.agregarArista(nodoCliente, sumidero, 1);
    }

    int respuesta = dinic.flujoMaximo(fuente, sumidero);
    cout << respuesta << "\n";
    return 0;
}