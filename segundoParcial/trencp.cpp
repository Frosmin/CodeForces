// #include <bits/stdc++.h>
// using namespace std;

// int cantidadVagones, largoTren;
// string engancheLocomotora;
// vector<string> enganchesVagones;
// int cantidadTipo[4];
// int maxTipo0, maxTipo1, maxTipo2, maxTipo3;
// int engancheInicial, engancheFinal;
// vector<long long> memo;

// int obtenerIndice(int u0, int u1, int u2, int u3, int lado) {
//     int id = (((u0 * maxTipo1 + u1) * maxTipo2 + u2) * maxTipo3 + u3) * 2 + lado;
//     return id;
// }

// long long contarFormas(int usados0, int usados1, int usados2, int usados3, int ladoActual) {
//     int usadosTotales = usados0 + usados1 + usados2 + usados3;
//     if (usadosTotales == largoTren) return ladoActual == engancheFinal ? 1LL : 0LL;
//     int id = obtenerIndice(usados0, usados1, usados2, usados3, ladoActual);
//     if (memo[id] != -1) return memo[id];

//     long long formas = 0;

//     if (ladoActual == 0) {
//         if (usados0 < cantidadTipo[0]) formas += contarFormas(usados0 + 1, usados1, usados2, usados3, 0);
//         if (usados1 < cantidadTipo[1]) formas += contarFormas(usados0, usados1 + 1, usados2, usados3, 1);
//     } else {
//         if (usados2 < cantidadTipo[2]) formas += contarFormas(usados0, usados1, usados2 + 1, usados3, 0);
//         if (usados3 < cantidadTipo[3]) formas += contarFormas(usados0, usados1, usados2, usados3 + 1, 1);
//     }

//     memo[id] = formas;
//     return formas;
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     cin >> cantidadVagones >> largoTren;
//     cin >> engancheLocomotora;

//     enganchesVagones.resize(cantidadVagones);
//     for (int i = 0; i < cantidadVagones; i++) cin >> enganchesVagones[i];

//     memset(cantidadTipo, 0, sizeof(cantidadTipo));

//     for (auto &s : enganchesVagones) {
//         if (s == "XX") cantidadTipo[0]++;
//         else if (s == "XY") cantidadTipo[1]++;
//         else if (s == "YX") cantidadTipo[2]++;
//         else cantidadTipo[3]++;
//     }

//     maxTipo0 = cantidadTipo[0] + 1;
//     maxTipo1 = cantidadTipo[1] + 1;
//     maxTipo2 = cantidadTipo[2] + 1;
//     maxTipo3 = cantidadTipo[3] + 1;

//     int totalEstados = maxTipo0 * maxTipo1 * maxTipo2 * maxTipo3 * 2;
//     memo.assign(totalEstados, -1);

//     engancheInicial = (engancheLocomotora[1] == 'X') ? 0 : 1;
//     engancheFinal = (engancheLocomotora[0] == 'X') ? 0 : 1;

//     long long resultado = contarFormas(0, 0, 0, 0, engancheInicial);

//     cout << resultado << "\n";
//     return 0;
// }



#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int vagones, tam_tren;
string acople;
long long dp[51][51][51][51][2];
map<string, int> conteo_tipos;

long long convinaciones(int c0, int c1, int c2, int c3, int ultimo_acople) {
    if (c0 + c1 + c2 + c3 == tam_tren) {
        int acople_final = (acople[0] == 'X') ? 0 : 1;
        return ultimo_acople == acople_final ? 1 : 0;
    }

    if (dp[c0][c1][c2][c3][ultimo_acople] != -1) {
        return dp[c0][c1][c2][c3][ultimo_acople];
    }

    long long total_formas = 0;

    // Si el último acople es 'X' (representado por 0)
    if (ultimo_acople == 0) {
        // Podemos añadir un vagón "XX" si hay disponibles
        if (c0 < conteo_tipos["XX"]) {
            total_formas += convinaciones(c0 + 1, c1, c2, c3, 0);
        }
        // Podemos añadir un vagón "XY" si hay disponibles
        if (c1 < conteo_tipos["XY"]) {
            total_formas += convinaciones(c0, c1 + 1, c2, c3, 1);
        }
    } else {
        // Podemos añadir un vagón "YX" si hay disponibles
        if (c2 < conteo_tipos["YX"]) {
            total_formas += convinaciones(c0, c1, c2 + 1, c3, 0);
        }
        // Podemos añadir un vagón "YY" si hay disponibles
        if (c3 < conteo_tipos["YY"]) {
            total_formas += convinaciones(c0, c1, c2, c3 + 1, 1);
        }
    }

    return dp[c0][c1][c2][c3][ultimo_acople] = total_formas;
}

void inicializar_dp() {
    for (int i = 0; i <= conteo_tipos["XX"]; ++i) {
        for (int j = 0; j <= conteo_tipos["XY"]; ++j) {
            for (int k = 0; k <= conteo_tipos["YX"]; ++k) {
                for (int l = 0; l <= conteo_tipos["YY"]; ++l) {
                    dp[i][j][k][l][0] = -1;
                    dp[i][j][k][l][1] = -1;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> vagones >> tam_tren;
    cin >> acople;

    conteo_tipos["XX"] = 0;
    conteo_tipos["XY"] = 0;
    conteo_tipos["YX"] = 0;
    conteo_tipos["YY"] = 0;

    for (int i = 0; i < vagones; i++) {
        string vagon;
        cin >> vagon;
        conteo_tipos[vagon]++;
    }

    inicializar_dp();

    int acople_inicial = (acople[1] == 'X') ? 0 : 1;

    long long resultado = convinaciones(0, 0, 0, 0, acople_inicial);

    cout << resultado << "\n";

    return 0;
}