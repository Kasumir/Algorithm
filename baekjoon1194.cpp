#include<iostream>
#include<vector>
#include<string.h>

using namespace std;

int N, M;
char miro[51][51];

void printm(){
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            cout << miro[i][j] << " ";
        }
        cout << endl;
    }
}

void input(){
    cin >> N >> M;
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            cin >> miro[i][j];
        }
    }
}
bool visited[51][51];

void solution(){
    memset(visited, true, sizeof(visited));
}

int main(){
    input();

}