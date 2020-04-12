#include <string>
#include <vector>
#include <iostream>

using namespace std;

int addall(vector<int> budgets, int M){
    int cnt = 0;
        for(int i = 0; i < budgets.size(); i++){
            if(budgets[i] >= M)
                cnt += M;
            else
            {
                cnt += budgets[i];
            }
        }
    return cnt;
}

int solution(vector<int> budgets, int M) {
    int answer = 0;
    int min, max = budgets[0];
    for(int i = 1; i < budgets.size(); i++){
        if(budgets[i] > max)
            max = budgets[i];    
    }
    min = 0;
    int cnt;
    while(1){
        if(answer == (min + max) / 2){
            break;
        }
        answer = (min + max) / 2;
        cnt = addall(budgets, answer);
        if(cnt < M){
            min = answer+1;
        }
        else if(cnt > M){
            max = answer-1;
        }
        else if(cnt == M){
            break;
        }
    }
    if(cnt > M){
        answer--;
    }


    return answer;
}

int main(){
    vector<int> b = {120, 110, 140, 150};
    int M = 485;
    cout << solution(b, M);
}