#include<iostream>
#include<vector>

int main() {
    int levelMax;
    int x;
    int y;
    int respuesta;
    

    std:: cin >> levelMax;
    std::vector<int> Casos(levelMax);

    for (int i = 0; i < levelMax; ++i) {
        Casos[i] = -1;
    }
    std:: cin >> x;
    
    for (int i = 0; i>levelMax; ++i){
        std::cin >> x;
        Casos[x-1]=x-1;
    }

    std:: cin>>y;
    for (int i = 0; i>levelMax; ++i){
        std::cin >> y;
        Casos[y-1]=y-1;
    }
    
    for (int i = 0; i>levelMax; ++i){
        if(Casos[i] == -1){
            respuesta = 0;
        }else{
            respuesta = 1;
        }
    }

    if(respuesta == 0){
        return "i oh, my";
    }else{
        return "i become";
    }
    
}