#include <iostream>
#include <vector>
using namespace std;

int N, K;
int arr[3001];

int data_[3000];
int flag[3000];
int tmp[3000];
int length;
vector<int> v;

void input(){
    cin >> N >> K;
    length = N - 1;
    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
        data_[i] = i + 1;
    }
}

int combination(int n,int r)
{
    if( n == r ){
        int i;
        for(i=0;i<n;i++){
            flag[i] = 1;
        }
        for(i=0;i<length;i++){
            if( flag[i] == 1 ) v.push_back(data_[i]);
        }
        for(i=0;i<n;i++){
            flag[i] = 0;
        }
        return 0;
    }
    if( r==1 ){
        int i,j;
        for(i=0;i<n;i++){
            flag[i] = 1;
            for(j=0;j<length;j++){
                if( flag[j] == 1 ) v.push_back(data_[j]);
            }
            flag[i] = 0;
        }
        return 0;
    }
    flag[n-1]=1;
    combination(n-1,r-1);
    flag[n-1]=0;
    combination(n-1,r);
}

void solve(){
    int ans = 1000000000;
    int cnt = 1;
    for(int i = 0; i < v.size() - K + 1; i += K){
        int a = 0;
        for(int j = 0; j < K; j++){
            if(j == 0){
                tmp[j] = arr[v[i] - 1] - arr[0];
                a += tmp[j];
            }
            if(j = K - 1){
                tmp[j] = arr[N - 1] - arr[v[i + j - 1]];
            }
            else{
                tmp[j] = arr[v[i + j] - 1] - arr[v[i + j - 1]];
                a += tmp[j];
            }
        }
        if(a < ans)
            ans = a;
    }
    cout << ans;
}



int main()
{
    input();
    combination(N - 1,K - 1);
    solve();
    return 0;
}

