#include<iostream>
#include<vector>

using namespace std;

 int N;
 int dp[1000000];

 int main(){
     cin >> N;
     int ans = 0;
     dp[1] = 0;
     for(int i = 2; i <= N; i++){
         int tmp[3] = {1000000,1000000,1000000};
         dp[i] = 1000000;
         if(i % 3 == 0){
             tmp[0] = dp[i / 3] + 1;
         }
         if(i % 2 == 0){
             tmp[1] = dp[i / 2] + 1;
         }  
        tmp[2] = dp[i - 1] + 1;
         
         for(int j = 0; j < 3; j++){
             if(dp[i] > tmp[j]){
                 dp[i] = tmp[j];
             }
         }
     }
     cout << dp[N];
 }