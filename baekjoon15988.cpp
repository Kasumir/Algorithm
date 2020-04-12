#include <iostream>
#include <vector>

using namespace std;

int T;
int arr[1000001];
long long dp[1000001];
long long ans[1000001];
vector<int> v;
int main(){
    cin >> T;
    for(int i = 0; i < T; i++){
        cin >> arr[i];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for(int j = 4; j <= arr[i]; j++){
            dp[j] = (dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009;
        }
        ans[i] = dp[arr[i]];
    }
    for(int i = 0; i < T; i++){
        cout << ans[i] << endl;
    }
}