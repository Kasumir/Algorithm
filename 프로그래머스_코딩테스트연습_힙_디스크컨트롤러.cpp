#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> j1;
    priority_queue<int, vector<int>, greater<int>> j2;
    int comp = 0;
    int jobsize = jobs.size();
    int start = 0;
    int len = 0;
    int time = 0;
    while(comp < jobsize)
    {
        for(int i = 0; i < jobs.size(); i++)
        {
            if(jobs[i][0] <= time)
            {
                j1.push(jobs[i][0]);
                j2.push(jobs[i][1]);
                jobs.erase(jobs.begin() + i);
                i--;
            }
        }
        if(time - start - len == 0){
            if(j1.size() == 0 && j2.size() == 0){
                start++;
            }
            else if(j1.size() == j2.size()){
                start = time;
                len = j2.top();
                j2.pop();
            }
            else if(j1.size() == 1 && j2.size() == 0){
                start++;
                answer += (time - j1.top());
                j1.pop();
                comp++;  
            }
            else if(j1.size() - j2.size() == 1){
                
                    start = time;
                    len = j2.top();
                    j2.pop();
                
                
                    answer += (time - j1.top());
                    j1.pop();
                    comp++;  
                 
            
        }
        cout << time << " " << start << " " << len << " j1:" << j1.size() << " j2:" << j2.size() << endl;
        time++;
    }
    answer /= jobsize;
    return answer;
}

int main(){
    vector<vector<int>> a = {{1, 3}, {1, 9}, {2, 6}, {20, 4}};
    cout << solution(a);
}