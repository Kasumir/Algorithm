#include<iostream>
using namespace std;

int N, M, T;

int tmp[10][51][51];
int arr[51][51];
string ans[10];

void solve(int num);

void input(){
    cin >> T;

    for(int k = 0; k < T; k++){
        cin >> N >> M;
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= M; j++){
             cin >> arr[i][j];
            }
        }
        solve(k);    
    }
}
void solve(int num){
    for(int i = 1; i < N; i++){
        for(int j = 1; j < M; j++){
            if(arr[i][j] != 0 && arr[i + 1][j + 1] != 0 && arr[i][j+1] != 0 && arr[i+1][j] != 0){
                tmp[num][i][j] = 1;
                tmp[num][i + 1][j] = 1;
                tmp[num][i][j + 1] = 1;
                tmp[num][i + 1][j + 1] = 1;
            }
        }
    }
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            if(tmp[num][i][j] != arr[i][j]){
                ans[num] = "NO";
                return;
            }
        }
    }
    ans[num] = "YES";
}

int main(){
    input();
    for(int i = 0; i < T; i++)
        cout << ans[i] << endl;
    return 0;
}

