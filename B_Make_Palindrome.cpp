#include <bits/stdc++.h>
using namespace std;

int main()
{
    string in;
    while(getline(cin,in)){
        vector<vector<int>> dp(in.length(),vector<int>(in.length(),1e6));
        vector<vector<int>> decision(in.length(),vector<int>(in.length()));
        for(int len=0;len<in.length();len++){
            for(int izq=0;izq+len<in.length();izq++){
                int der = izq+len;
                if(in[izq] == in[der]){
                    dp[izq][der] = izq+1>=der-1 ? 0 : dp[izq+1][der-1];
                } else {
                    int izqCost = dp[izq][der-1]; 
                    int derCost = dp[izq+1][der]; 
                    if(izqCost > derCost) {
                        dp[izq][der] = derCost+1;
                        decision[izq][der] = 1;
                    } else {
                        dp[izq][der] = izqCost+1;
                        decision[izq][der] = 2;
                    }
                }
            }
        }
        int izq=0,der=in.length()-1;
        string izqStr="",derStr="";
        while(izq<=der){
            if(in[izq] == in[der]){
                if(izq==der) izqStr += in[izq];
                else {
                    izqStr += in[izq];
                    derStr += in[izq];
                }
                izq++; der--;
            } else if(decision[izq][der] == 1){
                derStr += in[izq];
                izqStr += in[izq];
                izq++;
            } else if(decision[izq][der] == 2){
                
                izqStr += in[der];
                derStr += in[der];
                der--;
            }
        }
        reverse(derStr.begin(),derStr.end());
        cout << dp[0][in.length()-1] << " " << izqStr << derStr << endl;
    }
}