#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<iostream>
#include<cmath>
#include<cctype>
using namespace std;


#define Para(i,n) for(int i=1;i<=n;i++)
#define ParaK(i,k,n) for(int i=k;i<=n;i++)
#define ParaD(i,n) for(int i=n;i;i--)

#define INF (2139062143)
#define MAXN (10000000+10)  
#define MAXL (10001000+10)  


int arr_sufijos[MAXL];      
int conteo[MAXN];           
int temp_a[MAXL*2]={0};     
int temp_b[MAXL*2]={0};     


bool comparar(int *a, int x, int y, int j) {
    return a[x] == a[y] && a[x+j] == a[y+j];
}


void construir_arreglo_sufijos(char *cadena, int n, int m) {
    int *x = temp_a, *y = temp_b;
    
    
    Para(i, m) conteo[i] = 0;
    Para(i, n) conteo[x[i] = cadena[i]]++;
    ParaK(i, 2, m) conteo[i] += conteo[i-1];
    ParaD(i, n) arr_sufijos[conteo[x[i]]--] = i;

    
    for(int j = 1, p = 0; p < n; j *= 2, m = p) {
        p = 0;
        ParaK(i, n - j + 1, n) y[++p] = i;
        Para(i, n) if (arr_sufijos[i] > j) y[++p] = arr_sufijos[i] - j;
        
        Para(i, m) conteo[i] = 0;
        Para(i, n) conteo[x[i]]++;
        ParaK(i, 2, m) conteo[i] += conteo[i-1];
        ParaD(i, n) arr_sufijos[conteo[x[y[i]]]--] = y[i];
        
        p = 1; y[arr_sufijos[1]] = 1;
        ParaK(i, 2, n)
            y[arr_sufijos[i]] = (p += (!comparar(x, arr_sufijos[i], arr_sufijos[i-1], j)));
        
        int *t = x; x = y; y = t;
    }
}

int ranking[MAXL]; 
int altura[MAXL];  


void calcular_alturas(char *cadena, int n) {
    altura[1] = 0;
    Para(i, n) ranking[arr_sufijos[i]] = i;
    Para(i, n) {
        if (ranking[i] == 1) continue;
        altura[ranking[i]] = max(altura[ranking[i-1]] - 1, 0);
        while (cadena[i + altura[ranking[i]]] == cadena[arr_sufijos[ranking[i]-1] + altura[ranking[i]]])
            altura[ranking[i]]++;
    }
}

int n; 
int indices_inicio[MAXN], longitud[MAXN];
char cadena_concatenada[MAXL]; 
int pertenece_a[MAXL];         
int visitado[MAXN]={0};        
int resultados_temp[2][MAXL]={0}, tamanio_res[2]={0}; 


int verificar(int *lista_resultados, int &tamanio, int len) {
    memset(visitado, 0, sizeof(visitado));
    int grupo_actual = 1;
    int total_encontrados = 1;
    tamanio = 0;

    visitado[pertenece_a[arr_sufijos[1]]] = grupo_actual;

   
    ParaK(i, 2, indices_inicio[n+1] - 1) {
        if (altura[i] >= len) {
            
            if (visitado[pertenece_a[arr_sufijos[i]]] != grupo_actual) {
                visitado[pertenece_a[arr_sufijos[i]]] = grupo_actual;
                total_encontrados++;
            }
        } else {
            
            if (total_encontrados > n / 2) {
                lista_resultados[++tamanio] = arr_sufijos[i-1];
            }
           
            total_encontrados = 1;
            grupo_actual++;
            visitado[pertenece_a[arr_sufijos[i]]] = grupo_actual;
        }
    }
   
    if (total_encontrados > n / 2) {
        lista_resultados[++tamanio] = arr_sufijos[indices_inicio[n+1]-1]; 
        
    }
    return tamanio;
}

char separadores[MAXN]; 

int main() {
    int p = 0;
    Para(i, 'a'-1) separadores[++p] = i;
    for(int i = 'z'+1; p <= 100; i++) separadores[++p] = i;

    bool primera_vez = false;

    while(scanf("%d", &n)) {
        if (n == 0) break;
        if (primera_vez) puts(""); 
        indices_inicio[1] = 1;
        
       
        Para(i, n) {
            scanf("%s", cadena_concatenada + indices_inicio[i]);
            longitud[i] = strlen(cadena_concatenada + indices_inicio[i]);
            
            cadena_concatenada[indices_inicio[i] + longitud[i]] = separadores[i];
            indices_inicio[i+1] = indices_inicio[i] + longitud[i] + 1;
            
            ParaK(j, indices_inicio[i], indices_inicio[i] + longitud[i]) pertenece_a[j] = i;
        }
        
        cadena_concatenada[indices_inicio[n+1]] = 0; 
        
        
        construir_arreglo_sufijos(cadena_concatenada, indices_inicio[n+1] - 1, 200);
        calcular_alturas(cadena_concatenada, indices_inicio[n+1] - 1);
        
        
        int izq = 1, der = indices_inicio[n+1] - 1, mejor_longitud = 0, puntero = 0;
        
        while (izq <= der) {
            int medio = (izq + der) >> 1;
            if (verificar(resultados_temp[puntero], tamanio_res[puntero], medio)) {
                mejor_longitud = medio;
                izq = medio + 1;
                puntero ^= 1; 
            } else {
                der = medio - 1;
            }
        }
        
        if (mejor_longitud == 0) {
            puts("?");
        } else {
            puntero ^= 1; 
            Para(i, tamanio_res[puntero]) {
                
                ParaK(k, resultados_temp[puntero][i], resultados_temp[puntero][i] + mejor_longitud - 1) 
                    cout << cadena_concatenada[k];
                cout << endl;
            }
        }
        primera_vez = true;
    }
    return 0;
}