#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

priority_queue<int, vector<int>, less<int>> pq;
int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    int num = 0;
    while(stock < k){
        for(int i = num; i < dates.size() && stock >= dates[i]; i++){
            pq.push(supplies[i]);
            idx += 1;
        }
        stock += pq.top();
        pq.pop();
        answer++;
    }
    return answer;
}

int main(){
    vector<int> dates = {1,2,3,4};
    vector<int> sup = {1,1,1,1};
    cout << "answer : " << solution(4, dates, sup, 6) << endl;
}
