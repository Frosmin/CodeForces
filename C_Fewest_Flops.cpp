// #include <bits/stdc++.h>
// using namespace std;

// int t,k;
// string str;

// vector<vector<int>> memo; 
// int n; 
// vector<unordered_set<int>> partitions;

// int solve(int idx,int lastCharacter){
//     if(idx == n) return 0;
//     else if(memo[idx][lastCharacter] != -1) return memo[idx][lastCharacter];
//     int numUnique = partitions[idx].size();
//     int best = INT_MAX;
//     for(auto first=partitions[idx].begin(); first!=partitions[idx].end(); first++){
//         for(auto last=partitions[idx].begin(); last!=partitions[idx].end(); last++){
//             if(numUnique == 1 || first != last){
//                 int cost = solve(idx+1,*last) + numUnique;
//                 if(lastCharacter == *first) cost--;
//                 best = min(best, cost);
//             }
//         }
//     }
//     return memo[idx][lastCharacter] = best;
// }

// int main()
// {
//     scanf("%d",&t);
//     while(t--){
//         cin >> k >> str;
//         n = str.length()/k;
//         memo.assign(n,vector<int>(27,-1));
//         partitions.assign(n,unordered_set<int>());
//         for(int i=0;i<n;i++){
//             for(int j=0;j<k;j++){
//                 int pos = i*k+j;
//                 partitions[i].insert(str[pos]-'a');
//             }
//         }
//         printf("%d\n",solve(0,26));
//     }
// }


#include <bits/stdc++.h>
using namespace std;

int casos, tam_bloque;
string cadena;
int n; 

vector<vector<int>> memoria; 

vector<vector<int>> bloques; 

int resolver(int indice, int ultimo_caracter_previo) {
  
    if (indice == n) return 0;
    
    if (memoria[indice][ultimo_caracter_previo] != -1) {
        return memoria[indice][ultimo_caracter_previo];
    }

    int num_unicos = bloques[indice].size();
    int mejor_costo = INT_MAX;

    bool previo_existe_en_actual = false;
    for (int c : bloques[indice]) {
        if (c == ultimo_caracter_previo) {
            previo_existe_en_actual = true;
            break;
        }
    }
     for (int nuevo_ultimo : bloques[indice]) {
        int costo_actual = resolver(indice + 1, nuevo_ultimo) + num_unicos;
        
      
        
        if (previo_existe_en_actual) {
            if (num_unicos == 1) {
                
                if (nuevo_ultimo == ultimo_caracter_previo) {
                    costo_actual--;
                }
            } else {
              
                if (nuevo_ultimo != ultimo_caracter_previo) {
                    costo_actual--;
                }
                
            }
        }
        
        mejor_costo = min(mejor_costo, costo_actual);
    }

    return memoria[indice][ultimo_caracter_previo] = mejor_costo;
}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> casos;
    while (casos--) {
        cin >> tam_bloque >> cadena;
        n = cadena.length() / tam_bloque;
        
        
        memoria.assign(n, vector<int>(27, -1));
        bloques.assign(n, vector<int>());

        for (int i = 0; i < n; i++) {
            set<int> unicos; 
            for (int j = 0; j < tam_bloque; j++) {
                int pos = i * tam_bloque + j;
                unicos.insert(cadena[pos] - 'a');
            }
            
            bloques[i].assign(unicos.begin(), unicos.end());
        }

     
        cout << resolver(0, 26) << "\n";
    }
    return 0;
}