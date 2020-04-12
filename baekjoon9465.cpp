#include<iostream>

using namespace std;

int T, N;
long long dp[100001][3];
int p[1000001][3];
long long ans[100001];

int big(int num, int idx){
    int b=0;
    for(int i = 0; i <=2; i++){
        if(i == idx)
            continue;

        if(dp[num][i] > b)
            b = dp[num][i]; 
    }
    return b;
}

int main(){
    cin >> T;
    for(int l = 0; l < T; l++){
        cin >> N;
        
        for(int i = 1; i <= 2; i++){
            for(int j = 1; j <= N; j++){
                cin >> p[j][i];
                printf("p[%d][%d] = %ld ", j, i, p[j][i]);
            }
            printf("\n");
        }
        dp[1][0] = 0;
        dp[1][1] = p[1][1];
        dp[1][2] = p[1][2];
        printf("%d %d %d\n", dp[1][0], p[1][1], dp[1][2]);
        for(int i = 2; i <= N; i++){
            dp[i][0] = big(i - 1, 3);
            dp[i][1] = big(i - 1, 1) + p[i][1];
            dp[i][2] = big(i - 1, 2) + p[i][2];
            printf("%ld %ld %ld\n", dp[i][0], dp[i][1], dp[i][2]);
        }
        ans[l] = big(N, 3);
    }
    for(int i = 0; i < T; i++){
        cout << ans[i] << endl;
    }
}
