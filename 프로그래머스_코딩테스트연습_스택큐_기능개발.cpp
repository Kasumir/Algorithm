#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    while(!progresses.empty()){
        for(int i = 0; i < progresses.size(); i++){
            progresses[i] += speeds[i];
            cout << progresses[i] << " ";
        }
        cout << endl;
        int cnt = 0;
        for(int i = 0; i < progresses.size(); i++){
            if(progresses[i] < 100)
                break;
            else{
                cnt++;
            }
        }
        if(cnt){
            for(int i = 0; i < cnt; i++){
                progresses.erase(progresses.begin());
                speeds.erase(speeds.begin());
            }
            answer.push_back(cnt); 
        } 
    }
    getchar();
    
    return answer;
}

int main(){

    vector<int> pro = {93, 30, 55}; 
    vector<int> speed = {1, 30, 5};
    vector<int> anw = solution(pro, speed);

    for(int i = 0; i < anw.size(); i++)
        cout << anw[i]<< " ";
}