#include<iostream>

using namespace std;

int N;
int p[1001];
int dp[1001];

int max(int a, int b){
    if(a >= b)
        return a;
    else 
        return b;
}

int main(){
    cin >> N;
    for(int i = 1;i <= N; i++)
        cin >> p[i];

    dp[1] = p[1];
    for(int i = 2; i <= N; i++){
        dp[i] = p[i];
        for(int j = 1; j < i; j++){
            dp[i] = max(dp[i], dp[i - j] + p[j]);
        }
    }
    cout << dp[N];
}
