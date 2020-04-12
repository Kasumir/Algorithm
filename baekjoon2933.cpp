#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <string.h>


using namespace std;

int R, C, N;
char cave[101][101];
bool state[101][101];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
bool visited[101][101];
vector<int> spear;
vector<pair<int, int>> cluster;

void input(){
    cin >> R >> C;

    for(int i = R; i >= 1; i--){
        for(int j = 1; j <= C; j++){
            cin >> cave[i][j];
        }
    }

    cin >> N;
    spear = vector<int>(N);
    for(int i = 0; i < N; i++){
        cin >> spear[i];
    }
    for(int i = 1; i <= C; i++){
        state[0][i] = true;
        cave[0][i] = 'x';
    }
}

void check(){
    cluster.clear();
    vector<pair<int,int>> low;
    for(int i = R; i >= 1; i--){
        for(int j = 1; j <= C; j++){
            if(cave[i][j] == 'x' && state[i][j] == false){
                cluster.push_back(make_pair(i, j));
            }
        }
    }
    int ans = 101;
    if(cluster.size() > 0){
        for(int i = 0; i < cluster.size(); i++){
            for(int j = 1; cluster[i].first - i >= 1; i++){
                if(state[cluster[i].first - j -1][cluster[i].second] == true){
                    if(j <= ans)
                        ans = j;
                    break;
                }
            }
        }        
        for(int i = 0; i < cluster.size(); i++){
            cave[cluster[i].first][cluster[i].second] = '.';
        }
        for(int i = 0; i < cluster.size(); i++){
            cave[cluster[i].first - ans][cluster[i].second] = 'x';
        }
    }
    cluster.clear();
}

void updateState(){
    memset(state, false, sizeof(state));
    memset(visited, false, sizeof(visited));
    
    queue<pair<int, int>> q;
    q.push(make_pair(0,1));
    state[0][1] = true;
    visited[0][1] = true;

    int x, y;
    while(!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(0 <=nx && nx <= R && 1 <= ny && ny <= C){
                if(cave[nx][ny] == 'x' && visited[nx][ny] == false){
                    visited[nx][ny] =true;
                    state[nx][ny] = true;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}

int main(){
    input();
    updateState();
    for(int i = 0; i < spear.size(); i++){
        if(i % 2){
            for(int j = C; j >= 1; j--){
                if(cave[spear[i]][j] == 'x'){
                    cave[spear[i]][j] = '.';
                    break;
                }
            }
            updateState();
            check();
        }
        else{
            for(int j = 1; j <= C; j++){
                if(cave[spear[i]][j] == 'x'){
                    cave[spear[i]][j] = '.';
                    break;
                }
            }
            updateState();
            check();
        }
    }
    for(int i = R; i >= 1; i--){
        for(int j = 1; j <= C; j++){
            cout << cave[i][j];
        }
        cout << endl;
    }
}