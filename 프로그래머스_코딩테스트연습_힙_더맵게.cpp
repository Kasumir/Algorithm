#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;


/*
힙에서의 부모 노드와 자식 노드의 관계
왼쪽 자식의 인덱스 = (부모의 인덱스) * 2
오른쪽 자식의 인덱스 = (부모의 인덱스) * 2 + 1
부모의 인덱스 = (자식의 인덱스) / 2
https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
*/


priority_queue<int, vector<int>, greater<int>> pq;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    for(int i = 0; i < scoville.size(); i++){
        pq.push(scoville[i]);
    }
    while(!pq.empty()){
        if(pq.top() < K && pq.size() == 1)
            return -1;
        else if(pq.top() < K){
            int tmp1 = pq.top();
            pq.pop();
            int tmp2 = pq.top();
            pq.pop();
            pq.push(tmp1 + tmp2 * 2);
            answer++;
        }
        else{
            pq.pop();
        }
    }
    return answer;
}

int main(){
    vector<int> scov = {1, 2, 3, 9, 10, 12};
    vector<int> ans;


    cout << solution(scov, 7);

    return 0;
}