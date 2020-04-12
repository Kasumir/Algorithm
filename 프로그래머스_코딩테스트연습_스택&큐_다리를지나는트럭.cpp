#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

queue<int> q;

bool desc(int a, int b){
    return a > b;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int time = 0;
    for(int i = 0; i < bridge_length; i++)
        q.push(0);
    int wsum = 0;

    sort(truck_weights.begin(), truck_weights.end(), desc);

    while(!truck_weights.empty()){
        int a = 0;
        wsum -= q.front();
        q.pop();
        for(int i = 0; i < truck_weights.size(); i++){
            if(wsum + truck_weights[i] <= weight){
                q.push(truck_weights[i]);
                wsum += truck_weights[i];
                answer++;
                a++;
                truck_weights.erase(truck_weights.begin() + i);
                break;
            }
        }
        if(a == 0){
            q.push(0);
            answer++;
        }  
    }
    while(wsum != 0){
        answer++;
        wsum -= q.front();
        q.pop();
    }
    return answer;
}